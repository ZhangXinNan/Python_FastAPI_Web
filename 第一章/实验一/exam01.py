# 第一章 实验代码 exam01.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello 三酷猫！"}

if __name__ == "__main__":
    uvicorn.run(app=app)