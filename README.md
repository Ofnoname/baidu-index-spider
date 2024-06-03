0. py app.py 启动服务器并在浏览器打开 WebUI 界面
1. 时间最早只能为2011年1月
2. 单次 HTTP 请求最多同时请求 5 个关键词，同时一个关键词可以含有多个词条，最多 3 个词，多词会返回的是直接相加的结果。
3. 需要获取账号的 cookie_BDUSS 和 cipherText，存在credential.json处，格式如下：
```json
{
    "cookie_BDUSS": "xxxx",
    "cipherText": "xxxx"
}
```
可放入多个账号，每次会随机选取一个
4. 地区可以选择全国，某城市，或者某省 
5. GUI功能有限，有需求还请修改代码
6. 地区映射表在webui/public下
7. 爬虫类程序随着 api 变动随时可能失效，请注意时效