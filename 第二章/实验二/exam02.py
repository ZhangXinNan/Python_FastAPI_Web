# 第二章 实验代码 exam02.py
from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
class Fruit(BaseModel):
    id: Optional[int]
    name: str = '菠萝'
    amount: int = 10
    price: Optional[float] = 9.0

app = FastAPI()

@app.post("/additem/{item_id}", response_model=Fruit)
async def additem(item_id: int, amount: Optional[int], item: Fruit):
    result = {'item_id': item_id, **item.dict()}
    if amount:
        result.update({'amount': amount})
    return result
if __name__ == "__main__":
    uvicorn.run(app=app)