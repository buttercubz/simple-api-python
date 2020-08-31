from flask import Flask, jsonify, request
from db import DB

App = Flask(__name__)
database = DB()


class Server:  # handlers methods not use 'self argument'
    def __init__(self, **config):
        self.__config = config

    # run server
    def start(self):
        App.run(debug=self.__config['debug'], port=self.__config['port'])

    @App.route("/products", methods=['GET'])
    # pylint: disable=no-method-argument
    def get_all():
        return jsonify(database.get_all())

    @App.route("/products/<string:item_id>", methods=["GET"])
    # pylint: disable=no-self-argument
    def get_item(item_id):
        if len(database.get_all()) > 0:
            if database.Get(int(item_id)) != None:
                return jsonify(database.Get(int(item_id)))
            else:
                return jsonify({"err": "database", "msg": "item not found"})
        else:
            return jsonify({"err": "database", "msg": "database is empty"})

    @App.route("/products", methods=["POST"])
    # pylint: disable=no-method-argument
    def add_item():
        item = request.json
        return jsonify({"done": True, "item": database.add(item)})

    @App.route("/products/<string:item_id>", methods=["PUT"])
    # pylint: disable=no-self-argument
    def update(item_id):
        item = request.json
        update_item = database.update(int(item_id), item)
        if update_item != None:
            return jsonify({"done": True, "item": update_item})
        else:
            return jsonify({"err": "database", "msg": "not updated maybe this item not exist"})

    @App.route("/products/<string:item_id>", methods=["DELETE"])
    # pylint: disable=no-self-argument
    def delete(item_id):
        to_delete = database.remove(int(item_id))
        if to_delete != None:
            return jsonify({"done": True, "item": to_delete})
        else:
            return jsonify({"err": "database", "msg": "not deleted maybe this item not exist"})
