
# 第9章 企业应用架构 193
## 9.1 应用程序和子应用 193
### 9.1.1 使用环境变量 193
#### 1. 设置环境变量
Windows
```cmd
set MY_NAME=liuyu
echo %MY_NAME%
```

Linux/macOS
```bash
export MY_NAME=liuyu
echo $MY_NAME
```


#### 2. 通过Python设置环境变量
```python
import os
my_name = os.getenv('MY_NAME')
print(f"hello {my_name}")
```


#### 3. 通过Pydantic配置模块管理环境变量
- BaseSettings
  - code9_1.py
- PyCharm里设置环境变量

### 9.1.2 应用事件处理 197
#### 1. 启动事件
#### 2. 停止事件

### 9.1.3 管理子应用 198
### 9.1.4 管理外部Web应用 200

## 9.2 应用模块管理 201
### 9.2.1 路由类 202
### 9.2.2 应用目录结构 202
## 9.3 页面模板技术 204
### 9.3.1 Jinja2模板入门 204
### 9.3.2 管理静态文件 206
## 9.4 案例：三酷猫卖海鲜（八） 207
## 9.5 习题及实验 210



