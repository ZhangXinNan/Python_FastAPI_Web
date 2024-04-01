# 【示例2.4】 第二章 第2.2.5节 code2_4.py
from enum import Enum

from fastapi import FastAPI
import uvicorn

class ModelName(str, Enum):                 # 定义枚举类，继承str，Enum
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")             # 注册路由路径，包含一个路径参数model_name
async def get_model(model_name: ModelName):  # 参数类型是上面定义的枚举类
    if model_name == ModelName.alexnet:      # 使用枚举类型比较
        return {"model_name": model_name, "message": "深度学习模型精英：AlexNet!"}

    if model_name.value == "lenet":          # 使用值比较
        return {"model_name": model_name, "message": "深度学习模型元老：LeNet！"}

    return {"model_name": model_name, "message": "深度学习模型新秀：ResNet！"}

if __name__ == '__main__':
    uvicorn.run(app=app)