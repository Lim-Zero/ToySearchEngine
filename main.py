from ast import keyword
from flask import Flask, request
from flask import render_template
from flask import request
from spider import getserarch
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/s')
def s():
    keyword = request.args.get('wd')
    return getserarch(keyword)
if __name__=='__main__':
    app.run()