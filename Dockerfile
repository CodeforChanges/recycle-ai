# Python 베이스 이미지를 사용합니다.
FROM python:3.8

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 현재 디렉토리의 내용을 컨테이너의 작업 디렉토리로 복사합니다.
COPY . /app

# requirements.txt를 사용하여 필요한 패키지를 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# setup.py를 사용하여 패키지를 설치합니다.
RUN pip install -e .

# 컨테이너가 시작될 때 실행될 명령어를 지정합니다.
ENTRYPOINT ["reai"]
