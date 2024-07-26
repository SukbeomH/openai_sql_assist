import pymysql
from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st
import os
from openai import OpenAI

pymysql.install_as_MySQLdb() #파이썬 전용 데이터베이스 커넥터

engine = create_engine('mysql+pymysql://fisaai:woorifisa3!W@118.67.131.22/MySQL')

def get_databases():
    with engine.connect() as connection:
        result = connection.execute(text("SHOW DATABASES"))
        return [row[0] for row in result]

# 테이블 목록을 가져오는 쿼리
def get_tables(db_name):
    with engine.connect() as connection:
        connection.execute(text(f"USE {db_name}"))
        result = connection.execute(text("SHOW TABLES"))
        return [row[0] for row in result]

# Streamlit 앱 구성
st.write("fisaai에 Databases 목록:")
databases = get_databases()
st.write(" | ".join(databases))

# Streamlit 입력 필드
db = st.text_input('db명 입력해주세요')


if db:
    if db in databases:
        tables = get_tables(db)
        st.write(f"{db} 데이터베이스의 테이블 목록:")
        st.write(" | ".join(tables))

        table = st.text_input('테이블명을 입력해주세요')

        if table:
            if table in tables:
                key = st.text_input('openai 키 입력 : ')

                if key:
                    sql = f'SELECT * FROM {db}.{table}'
                    df = pd.read_sql(sql, con=engine)

                    os.environ['OPENAI_API_KEY'] = key
                    client = OpenAI()

                    def table_definition_prompt(df):
                        prompt = '''Given the following MySQL Query definition,
                                    write queries based on the request
                                    \n### MySQL Query, with its properties:
                                    
                                    #
                                    # df의 컬럼명({})
                                    #
                                    '''.format(",".join(str(x) for x in df.columns))
                        
                        return prompt

                    nlp_text = st.text_input('질문을 입력하세요: ')

                    accept = st.button('요청')

                    if accept:
                        full_prompt = str(table_definition_prompt(df)) + str(nlp_text)
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": f"You are an assistant that generates MySQL query based on the given df definition\
                                and a natural language request. The answer should contain only code, not any explanation or ``` for copy.\
                                And you have to add the result of the answer query.\
                                 The name of database is {db} and the name of table is {table}.\
                                Statement 'FROM' must include {db}.{table}"},
                                {"role": "user", "content": f"A query to answer: {full_prompt}"}
                            ],
                            max_tokens=200,
                            temperature=1.0,
                            stop=None
                            )

                        answer = response.choices[0].message.content
                        try:
                            answer_df = pd.read_sql(answer, con=engine)
                            st.code(full_prompt)
                            st.code(answer)
                            st.write(answer_df)
                        except Exception as e:
                            st.error(f"쿼리 실행 오류: {e}")
            else:
                st.error('옳지 않은 테이블명입니다.')
    else:
        st.error('옳지 않은 db 명입니다.')
