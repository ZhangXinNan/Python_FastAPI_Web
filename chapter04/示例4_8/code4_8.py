# 【示例4.8】 第四章 第4.1节 code4_8.py
from fastapi import FastAPI, Path
import uvicorn
app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., description="某一项的ID", ge=1),
):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app=app)