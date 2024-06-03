import json
import random

from flask import Flask, request, jsonify
import webbrowser

from spider import crawl_request, crawl

credentials = []
port = 5000

app = Flask(__name__, static_folder='webui/dist')

@app.route('/api/crawl', methods=['POST'])
def handle_post():
    data = request.get_json()
    # 这里可以处理你的数据
    print(data)

    # 转发全部参数给 crawl，并加上一个credential，从credentials列表中随机选择一个
    credential = random.choice(credentials)
    result = crawl(**data, credential=credential)
    if result == -1:
        return jsonify({'message': '关键词不存在或组合里有不存在的关键词，请检查'}), 400
    return jsonify({'message': 'Received data', 'data': result}), 200


# 查询账号数量
@app.route('/api/credentials', methods=['GET'])
def get_credentials():
    return jsonify({'count': len(credentials)})


# 访问其他目录，则静态托管html，css，js等文件
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == '':
        return app.send_static_file('index.html')
    return app.send_static_file(path)

def main():
    print('Staring server...')
    global credentials

    # Load credentials from a JSON file
    with open('credential.json') as f:
        credentials = json.load(f)

    print(f'Loaded {len(credentials)} credentials')

    # Start a flask server
    webbrowser.open(f'http://localhost:{port}')
    app.run(port=port, debug=False)


if __name__ == '__main__':
    main()
