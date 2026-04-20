# 1. 파이썬 이미지
FROM python:3.11-slim

# 2. 작업 디렉토리 설정 (기본 위치)
WORKDIR /app

# 3. 종속성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 현재 폴더(fastapi/)의 모든 내용을 컨테이너 /app으로 복사
# 이렇게 하면 컨테이너 안에 /app/app/main.py 구조가 유지됩니다.
COPY . .

# 5. 실행 명령어 수정 (중요!)
# 컨테이너 내 위치가 /app 이고 실제 파일은 app/main.py이므로 
# 'app.main'으로 호출해야 정확합니다.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]