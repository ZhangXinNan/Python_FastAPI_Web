# 【示例5.7】 第五章 第5.7节 code5_6.py
from fastapi import Depends, FastAPI
import uvicorn
app = FastAPI()

class PetQueryChecker:                     # 定义依赖类
    def __init__(self, pet_name: str):  # 构造方法
        self.pet_name = pet_name

    def __call__(self, q: str = ""):         # 使类的实例可调用
        if q:
            return self.pet_name in q   # 检测参数值
        return False

checkcat = PetQueryChecker("cat")          # 创建依赖类的可调用实例
checkdog = PetQueryChecker("dog")          # 创建依赖类的可调用实例

@app.get("/pet/")                          # 注册路由路径
async def read_query_check(                # 定义路径操作函数
        has_cat: bool = Depends(checkcat),  # 依赖项1，参数中有cat
        has_dog: bool = Depends(checkdog),  # 依赖项2，参数中是否有dog
):
    return {"has_cat": has_cat, "has_dog": has_dog}

if __name__ == '__main__':
    uvicorn.run(app)