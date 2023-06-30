#!/usr/bin/env python3

from flask import Flask, make_response, abort, jsonify
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal')
def get_animals():
    animals_list = []
    for animal in Animal.query.all():
        animal_dict ={
         "id": animal.id,
         "name": animal.name,
         "species": animal.species,
           
        }
        animals_list.append(animal_dict)

    response = make_response(
        jsonify(animal_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/animal/<id>')
def get_animal(id):
    animal = Animal.query.get(id)
    if not animal:
        abort (404)

    animal_dict = {
         "id": animal.id,
         "name": animal.name,
         "species": animal.species,
    }

    response = make_response(
        jsonify(animal_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/zookeeper/<id>')
def zookeeper_route(id):
    zookeeper = Zookeeper.query.get(id)
    if not zookeeper:
      abort (404)
    
    zookeeper_dict = {
        "id": zookeeper.id,
        "name": zookeeper.name,
        "birthday": zookeeper.birthday,
    }

    response = make_response(
        jsonify (zookeeper_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/enclosure/<id>')
def enclosure_route(id):
    enclosure = Enclosure.query.get(id)
    if not enclosure:
        abort (404) 

    enclosure_dict = {
        "id": enclosure.id,
        "environment": enclosure.environment,
        "open_to_visitors": enclosure.open_to_visitors,
    }

    response = make_response(
        jsonify(enclosure_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response
  


if __name__ == '__main__':
    app.run(port=6000, debug=True)
