# AI SQL Query **[ASQ]**  - Assistant

## 😸 Deploy by Streamlit && 💾 Assist by OpenAI (ChatGPT)

### Description 😁

> AI SQL Query Assistant는 우리FISA 과정 내 특정 Database 에 대해, 
> 사용자가 SQL Query를 요청하면, 
> 해당 Query를 제작해 보여주는 서비스입니다.

---

### How to use 🤔

## 0. 환경 변수 설정

- `.env` 파일을 생성하여, 환경 변수를 설정합니다.
  - `DB_PATH` : Database Path를 설정합니다.
  - `OPENAI_API_KEY` : OpenAI API Key를 설정합니다.
```
DB_PATH="mysql+pymysql://{user_name}:{password}@{db_address}/MySQL"
```

## 1. Local 환경에서 실행하기

  a) Clone this repository

  ```bash
  git clone {repository_url} {directory_name}
  ```

  b) Install required packages (Use `pip` or `conda`)

  ```bash
  pip install -r requirements.txt
  ```
  
  `conda` 사용시,
  
  ```bash
  conda install --file requirements.txt
  ```

  c) Run Streamlit

  ```bash
  streamlit run dbconnect.py
  ```

## 2. Docker 환경에서 실행하기

  a) Build Docker Image

  ```bash
  docker build -t asq .
  ```

  b) Run Docker Container

  ```bash
  docker run -p 8501:8501 asq
  ```

3. Docker Compose 환경에서 실행하기

  c) Run Docker Compose

  ```bash
  docker compose up
  ```

---

### 개발 환경 설정 🛠

## 1. Python && Streamlit && OpenAI

- Python 3.11
- OpenAI API Key

## 2. `venv` 환경 설정

```bash
python -m venv ai_sql
source ai_sql/bin/activate
```

- deactivate

```bash
deactivate
```

## 3. `conda` 환경 설정

```bash
conda create -n ai_sql python=3.11 # 3.12 버전도 가능
conda activate ai_sql
```

- deactivate

```bash
conda deactivate
```

---

### 기능 🚀

- SQL Query 생성
- OpenAI ChatGPT를 활용한 대화형 인터페이스
  - API Key를 입력하면, OpenAI와 연동하여 대화형 인터페이스를 제공합니다.
  - 사용자가 질문을 입력하면, ChatGPT가 답변을 생성합니다.
- Streamlit을 활용한 웹 어플리케이션 제작
- Docker를 활용한 배포
  - Docker Compose를 활용한 배포

---

# 📒 Version History

## v0.0.2
- Rollback MySQL DB Connection Path
  - Streamlit 배포를 위해, MySQL DB Connection Path를 다시 하드코딩으로 변경
- 함수의 설명을 한국어로 변경

## v0.0.1
- Add README.md
- Update requirements.txt
- Add Dockerfile
- Add Docker Compose Yaml
- Add .gitignore
- Add venv conf files