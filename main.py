from fastapi import FastAPI
from fastapi.responses import FileResponse

# 이 부분이 없거나 대문자(App)이면 올려주신 에러가 발생합니다.
app = FastAPI()

# 1. 기본 웹사이트 화면을 보여주는 경로
@app.get("/")
def read_index():
    return FileResponse("index.html")

# 2. 백엔드 데이터 확인용 임시 경로
@app.get("/items")
def read_items():
    return {"message": "데이터 요청 성공"}