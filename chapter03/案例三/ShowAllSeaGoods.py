#ShowAllSeaGoods.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI()

html_content = """
    <html>
        <head>
            <title>浏览器顶部的标题</title>
        </head>
        <body>
            <h3>三酷猫海鲜店</h3>
            <table border="1">
              <tr>
                 <th> 品   名 </th>
                 <th> 数量 </th>
                 <th> 单位</th>
                 <th> 单价（元）</th>
              </tr>
              <tr>
                 <td>野生大黄鱼</td>
                 <td>20</td>
                 <td>斤</td>
                 <td>168</td>
               </tr>
               <tr>
                 <td>对虾</td>
                 <td>100</td>
                 <td>斤</td>
                 <td>48</td>
               </tr>
               <tr>
                 <td>比目鱼</td>
                 <td>200</td>
                 <td>斤</td>
                 <td>69</td>
               </tr>
               <tr>
                 <td>黄花鱼</td>
                 <td>500</td>
                 <td>斤</td>
                 <td>21</td>
               </tr>
            </table>
        </body>
    </html>
    """
@app.get("/html/", response_class=HTMLResponse)  # 设置响应类为HTML响应
async def read_items1():                                         # 直接返回HTML文本
    return html_content

if __name__ == '__main__':
    uvicorn.run(app=app)