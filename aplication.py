from flask import Flask

aplication = Flask(__name__)

@aplication.route('/')
def hello_word():
          return '<h1>Hello word</h1>'

@aplication.route('/usuario')
def nombre():
          return '<h1>Diego Salinas</h1>'

@aplication.route('/usuario/<username>')
def devuelto(username):
          return username