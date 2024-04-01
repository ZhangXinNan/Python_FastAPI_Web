# 【示例1.8】 第一章 第1.4.2节 code1_8.py
class Person:                             # 定义类
    def __init__(self, name: str):        # 类的构造方法，初始化属性：name
        self.name = name

def get_person_name(one_person: Person):  # 定义函数，参数类型是自定义类
    return one_person.name            # 返回自定义类实例的属性