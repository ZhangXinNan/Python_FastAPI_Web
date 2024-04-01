# 【示例1.4】 第一章 第1.4.2节 code1_4.py
from typing import List               # 从typing模块中导入List

def process_items(items: List[str]):  # 定义函数，参数为字符串列表泛型
    for item in items:                # 遍历列表中的元素
        print(item)                   # 打印每一项元素

process_items(['a', 'b', 'c'])        # 调用函数
