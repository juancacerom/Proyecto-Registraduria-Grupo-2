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


app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorPartidos import ControladorPartidos
from Controladores.ControladorMesaVotacion import ControladorMesa
from Controladores.ControladorRegistroVotos import ControladorRegistroVotos
miControladorCandidato=ControladorCandidatos()
miControladorPartido=ControladorPartidos()
miControladorMesaVotacion=ControladorMesa()
miControladorRegistro=ControladorRegistroVotos()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/Candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/Candidatos/<string:id>", methods=["GET"])
def get_Candidatos(id):
    json = miControladorCandidato.show(id)
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

@app.route("/Partidos/<string:id>", methods=["GET"])
def get_partido(id):
    json = miControladorPartido.show(id)
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
def eliminarPartidos(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/mesaVotacion",methods=['GET'])
def getMesas():
    json=miControladorMesaVotacion.index()
    return jsonify(json)

@app.route("/mesaVotacion/<string:id>", methods=["GET"])
def get_mesa(id):
    json = miControladorMesaVotacion.show(id)
    return jsonify(json)
@app.route("/mesaVotacion",methods=['POST'])
def crearMesasVotacion():
    data = request.get_json()
    json=miControladorMesaVotacion.create(data)
    return jsonify(json)
@app.route("/mesaVotacion/<string:id>",methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json=miControladorMesaVotacion.update(id,data)
    return jsonify(json)

@app.route("/mesaVotacion/<string:id>",methods=['DELETE'])
def eliminarMesas(id):
    json=miControladorMesaVotacion.delete(id)
    return jsonify(json)

@app.route("/registroVotos",methods=['GET'])
def getRegistro():
    json=miControladorRegistro.index()
    return jsonify(json)
@app.route("/registroVotos/<string:id>",methods=['GET'])
def getRegistroid(id):
    json=miControladorRegistro.show(id)
    return jsonify(json)
@app.route("/registroVotos/Candidatos/<string:id_Cantidato>/Partidos/<string:id_Partido>/mesaVotacion/<string:id_Mesa>",methods=['POST'])
def crearRegistro(id_Cantidato,id_Partido,id_Mesa):
    data = request.get_json()
    json=miControladorRegistro.create(data,id_Cantidato,id_Partido,id_Mesa)
    return jsonify(json)
@app.route("/registroVotos/Candidatos/<string:id_Cantidato>/Partidos/<string:id_Partido>/mesaVotacion/<string:id_Mesa>",methods=['PUT'])
def modificarRegistro(id_Cantidato,id_Partido,id_Mesa):
    data = request.get_json()
    json=miControladorRegistro.update(data,id_Cantidato,id_Partido,id_Mesa)
    return jsonify(json)
@app.route("/registroVotos/<string:id_Registro>",methods=['DELETE'])
def eliminarRegistro(id_Registro):
    json=miControladorRegistro.delete(id_Registro)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


