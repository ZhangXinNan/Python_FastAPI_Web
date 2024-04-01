# 【示例1.7】 第一章 第1.4.2节 code1_7.py
from typing import Optional             # 从typing模块中导入Optional

def say_my_name(name: Optional[str] = None): # 定义函数，参数类型是可选类型
    if name is not None:                # 当name不为空时，打印 Hye name
        print(f"我是 {name}!")           # 打印字符串
    else:
        print("喵")            # 否则打印默认字符串
say_my_name()                  # 调用函数是不传参数
say_my_name('三酷猫')           # 调用函数时，传入一个名字