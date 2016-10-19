#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/contact')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)

    
if __name__ == '__main__':
    app.run(debug=True)
