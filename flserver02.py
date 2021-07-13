# index.html 로딩 서버
from flask import Flask, render_template

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 최초 url
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=8080)