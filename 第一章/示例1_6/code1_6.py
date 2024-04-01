# 【示例1.6】 第一章 第1.4.2节 code1_6.py
from typing import Dict                          # 从typing模块中引入Dict

def process_items(prices: Dict[str, float]):     # 定义函数，参数是字典泛型
    for item_name, item_price in prices.items(): # 遍历字典的内容
        print(item_name)                         # 打印字典项的键
        print(item_price)                        # 打印字典项的值
