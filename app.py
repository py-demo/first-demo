# coding:utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', **{
        'title': '首页'
    })

@app.route('/list')
def list():
    return render_template('list.html', **{
        'title': '列表页'
    })

if __name__ == '__main__':
    app.run(debug=True)
