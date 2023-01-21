from flask import Flask, request

aplication = Flask(__name__)

@aplication.route('/')
def hello_word():
          print(request)
          return '<h1>Hello word</h1>'

@aplication.route('/usuario')
def nombre():
          return '<h1>Diego Salinas</h1>'

@aplication.route('/usuario/<username>') #Parametro de entrada <parametro> para pasar lo que tiene en la ruta
def devuelto(username):
          return username

@aplication.post("/")
def hello_word_post():
          return '<h1>Posteadisimo mi pana</h1>'