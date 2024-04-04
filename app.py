# test2 project, app.py
# Mike Colbert 09/20/2019

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world, index'

@app.route('/hien')
def hien():
    return 'Hello hien'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



