
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello FastAPI"
    import uvicorn
    uvicorn.run("main:app", reload = True, host = "0.0.0.0") //reload:만약 바뀌어도 다시 reload 해줌. 호스트주소(0.0.0.0): 어떤 ip든 접속 할 수 있게 해줌. 이거 안 열어놓으면 외부에서 접속 안된담, port:디폴트는 8000번

unicorn main:app --reload


