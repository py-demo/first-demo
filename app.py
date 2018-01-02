# coding:utf-8
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('home.html', **{
        'title': '首页'
    })


@app.route('/list')
def list():
    return render_template('list.html', **{
        'title': '列表页'
    })


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html', **{
            'title': '用户登陆'
        })
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        return jsonify({
            'username': username,
            'password': password
        })


if __name__ == '__main__':
    app.run(debug=True)
