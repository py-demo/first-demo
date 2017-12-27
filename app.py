# encoding:utf-8
from flask import Flask, render_template

app = Flask(__name__)

listData = [{
    'name': 'php'
}, {
    'name': 'java'
}, {
    'name': 'python'
}]

@app.route('/')
def hello_world():
    return render_template('home.html', **{
        'title': '首页',
        'list': listData
    })

@app.route('/list')
def list():
    return render_template('list.html', **{
        'title': '列表页',
        'list': listData
    })

if __name__ == '__main__':
    app.run(debug=True)
