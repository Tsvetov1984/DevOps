from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        text = request.json.get('text')
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        return "OK"

    if request.method == 'GET':
        try:
            with open('data.txt', 'r', encoding='utf-8') as f:
                return {"result": f.read()}
        except FileNotFoundError:
            return {"result": ""}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)