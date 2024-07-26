import pymysql
from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import os
from openai import OpenAI

pymysql.install_as_MySQLdb() #파이썬 전용 데이터베이스 커넥터

engine = create_engine('mysql+pymysql://fisaai:woorifisa3!W@118.67.131.22/MySQL')

db = st.text_input('db명 입력해주세요')
table = st.text_input('테이블명을 입력해주세요')
key = st.text_input('openai 키 입력 : ')

if bool(db) and bool(table) and bool(key):
    sql = f'SELECT * FROM {db}.{table}'

    df = pd.read_sql(sql, con=engine)


    os.environ['OPENAI_API_KEY'] = f'{key}'
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
                {"role": "system", "content": f"You are an assistant that generates MySQL query and table which is result of the query based on the given df definition\
                and a natural language request. The answer should contains only code, not any explanation or ``` for copy.\
                ANd you have to add the result of the answer query.\
                 The name of database is {db} and name of table is {table}\
                Statement 'FROM' must include {db}.{table}"},
                {"role": "user", "content": f"A query to answer: {full_prompt}"}
            ],
            max_tokens=200, # 비용 발생하므로 시도하며 적당한 값 찾아간다. 200이면 최대 200단어까지 생성. 
                            # 영어는 한 단어가 1토큰, 한글은 한 글자가 1토큰 정도
            temperature=1.0, # 창의성 발휘 여부. 0~2 사이. 0에 가까우면 strict하게, 2에 가까우면 자유롭게(창의성 필요)
            stop=None # 특정 문자열이 들어오면 멈춘다든지. None이면 없음. .이면 문장이 끝나면 멈춘다든지
            )

        answer = response.choices[0].message.content
        st.code(full_prompt)
        st.code(answer)
