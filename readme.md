# AI SQL Query **[ASQ]**  - Assistant

## Deploy by Streamlit && Assist by OpenAI (ChatGPT)

### Description 😁

> AI SQL Query Assistant는 우리FISA 과정 내 특정 Database 에 대해, 
> 사용자가 SQL Query를 요청하면, 
> 해당 Query를 제작해 보여주는 서비스입니다.

### How to use 🤔

1. Local 환경에서 실행하기

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

2. Docker 환경에서 실행하기

  a) Build Docker Image

  ```bash
  docker build -t asq .
  ```

  b) Run Docker Container

  ```bash
  docker run -p 8501:8501 asq
  ```

3. Docker Compose 환경에서 실행하기

  a) Run Docker Compose

  ```bash
  docker-compose up
  ```


