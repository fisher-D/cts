from flask import Flask
from flask import render_template
import test_fun as ts

app = Flask(__name__)


@app.route('/makeBloodInfo')
def hello_world():
    res = ts.hashgenerate_test()
    return res


@app.route('/')
def hell_again():
    return "Welcome to the BloodChain"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
