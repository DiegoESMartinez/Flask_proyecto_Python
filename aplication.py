from flask import Flask, request
from flask import render_template
from flask_cors import CORS
import requests

application=Flask(__name__)

@application.route("/get-users/<username>")
def get_users(username):
    # lógica del problema
    return "alo " + username
"""
#App para hacer TO-DOs
id=0
dic=dict()
aplication = Flask(__name__)
CORS(aplication)
@aplication.post("/create-todo")
def create_todos():
          resp = request.data
          resp=resp.decode()
          id+=1
          dic.update({"id":1,
              "todo":resp,
              "checked":False
          })
          

@aplication.route("/get-todos")
def get_todos():
          dic.update({"id":1,
              "todo":"Tarea 1",
              "checked":False
          })
          id=1
          return dic

@aplication.put("/complete-todo")
def complete_todos():
          pass


--------------------------------------------------------------------------- 
@aplication.route('/')
def hello_word():
          print(request)
          return '<h1>Hello word</h1>'

@aplication.route('/usuario')
def nombre():
          return '<h1>Diego Salinas</h1>'

@aplication.route('/usuario/<username>') #Parametro de entrada <parametro> para pasar lo que tiene en la ruta
def devuelto(username):
          return render_template('hello.html',username=username)

@aplication.post("/")
def hello_word_post():
          return '<h1>Posteadisimo mi pana</h1>'
"""