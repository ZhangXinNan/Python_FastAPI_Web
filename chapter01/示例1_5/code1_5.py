# 【示例1.5】 第一章 第1.4.2节 code1_5.py
from typing import Set, Tuple           # 从typing模块中导入Set和Tuple

def process_items(                      # 定义函数
        items_t: Tuple[int, int, str],  # 元组泛型参数
        items_s: Set[bytes]             # 集合泛型参数
    ):
    return items_t, items_s
