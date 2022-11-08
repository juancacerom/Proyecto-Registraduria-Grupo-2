from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Usu-Prueba:relenm71@cluster0.da5ostw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

baseDatos = client["bd-Registraduria"]
print(baseDatos.list_collection_names())

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorPartidos import ControladorPartidos
miControladorCandidato=ControladorCandidatos()
miControladorPartido=ControladorPartidos()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/Candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/Candidatos",methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/Candidatos/<string:id>",methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidatos(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)


@app.route("/Partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/Partidos",methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/Partidos/<string:id>",methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/Partidos/<string:id>",methods=['DELETE'])
def eliminarCPartidos(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


