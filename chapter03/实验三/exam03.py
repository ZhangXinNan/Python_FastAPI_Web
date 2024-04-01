# 第三章 实验代码 exam03.py
from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
class FishBase(BaseModel):
    name: str = '三纹鱼'
    amount: int = 10
    unit: str = '斤'

class CreateFish(FishBase):
    price: float = 9.0

class Fish(FishBase):
    pass

app = FastAPI()
@app.post("/additem/", response_model=Fish)
async def additem(name: str, fish: CreateFish):
    return fish

if __name__ == "__main__":
    uvicorn.run(app=app)