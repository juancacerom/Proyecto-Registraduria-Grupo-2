from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import requests
import datetime
import re

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


app = Flask(__name__)
cors = CORS(app)
app.config["JWT_SECRET_KEY"] = "clave-secreta-123"
jwt = JWTManager(app)

def load_file_config():
  with open("config.json") as f:
    return json.load(f)

@app.before_request
def before_request_callback():
  url = limpiar_url(request.path)
  excluded_routes = ["/login"]
  if url in excluded_routes:
    print("Ruta excluida del middleware", url)
  else:
    if verify_jwt_in_request():
      usuario = get_jwt_identity()
      rol = usuario["rol"]
      if rol is not None:
        if request.method.upper() == "GET" or request.method.upper() == "POST" :
            if not validar_permiso(url, request.method.upper(), rol["_id"]):
                print(1)
                return jsonify({"message": "Permission denied"}), 401
      else:
        print(2)
        return jsonify({"message": "Permission denied"}), 401
    else:
      print(3)
      return jsonify({"message" : "Permission denied"}), 401

def limpiar_url(url):
  partes = url.split("/")

  for p in partes:
    if re.search("\\d", p):
      url = url.replace(p, "?")

  return url


def validar_permiso(url, metodo, id_rol):

  config_data = load_file_config()
  url_seguridad = config_data["url-bd-Registraduria-Seguridad"] + "/Permisos-rol/validar-permiso/roles/" + id_rol
  headers = {"Content-Type": "application/json; charset=utf-8"}
  body = {
    "url" : url,
    "metodo" : metodo
  }
  response = requests.post(url_seguridad, headers=headers, json=body)
  return response.status_code == 200


@app.route("/login", methods=["POST"])
def create_token():
  data = request.get_json()
  config_data = load_file_config()
  url = config_data["url-bd-Registraduria-Seguridad"] + "/Usuarios/validate"
  headers = {"Content-Type" : "application/json; charset=utf-8"}
  response = requests.post(url, json=data, headers=headers)

  if response.status_code == 200:
    user = response.json()
    expires = datetime.timedelta(seconds=60 * 60 * 24)
    token = create_access_token(identity=user, expires_delta=expires)
    return jsonify({"token" : token, "user_id" : user["_id"]})
  else:
    return jsonify({"msg" : "Usuario o contraseña incorrecta"}), 401


@app.route("/Candidatos", methods=["GET"])
def listar_Candidatos():
  config_data = load_file_config()
  url = config_data["url-bd-Registraduria-datos"] + "/Candidatos"
  response = requests.get(url)
  return jsonify(response.json())

@app.route("/Candidatos/<string:id>", methods=["GET"])
def mostrar_Candidatos(id):
  config_data = load_file_config()
  url = config_data["url-bd-Registraduria-datos"] + "/Candidatos" + id
  response = requests.get(url)
  return jsonify(response.json())



@app.route("/Candidatos", methods=["POST"])
def crear_candidato():
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/Candidatos"
    info_candidato = request.get_json()
    response = requests.post(url, json=info_candidato)
    return jsonify(response.json())

@app.route("/Candidatos/<string:id>", methods=["PUT"])
def actualizar_candidato(id):
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/Candidatos/" + id
    info_candidato = request.get_json()
    response = requests.put(url, json=info_candidato)
    return jsonify(response.json())


@app.route("/Candidatos/<string:id>", methods=["DELETE"])
def Borrar_candidato(id):
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/Candidatos/" + id
    response = requests.delete(url)
    return jsonify(response.json())



@app.route("/mesaVotacion", methods=["GET"])
def listar_mesa():
  config_data = load_file_config()
  url = config_data["url-bd-Registraduria-datos"] + "/mesaVotacion"
  response = requests.get(url)
  return jsonify(response.json())

@app.route("/mesaVotacion", methods=["POST"])
def crear_mesa():
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/mesaVotacion"
    info_mesa = request.get_json()
    response = requests.post(url, json=info_mesa)
    return jsonify(response.json())


@app.route("/Partidos", methods=["GET"])
def listar_Partido():
  config_data = load_file_config()
  url = config_data["url-bd-Registraduria-datos"] + "/Partidos"
  response = requests.get(url)
  return jsonify(response.json())

@app.route("/Partidos", methods=["POST"])
def crear_Partido():
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/Partidos"
    info_partidos = request.get_json()
    response = requests.post(url, json=info_partidos)
    return jsonify(response.json())

@app.route("/Partidos/<string:id>", methods=["PUT"])
def actualizar_Partido(id):
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/Partidos/" + id
    info_partidos = request.get_json()
    response = requests.put(url, json=info_partidos)
    return jsonify(response.json())


@app.route("/Partidos/<string:id>", methods=["DELETE"])
def Borrar_Partido(id):
    config_data = load_file_config()
    url = config_data["url-bd-Registraduria-datos"] + "/Partidos/" + id
    response = requests.delete(url)
    return jsonify(response.json())

@app.route("/registroVotos", methods=["GET"])
def listar_Registro():
  config_data = load_file_config()
  url = config_data["url-bd-Registraduria-datos"] + "/registroVotos"
  response = requests.get(url)
  return jsonify(response.json())

if __name__ == '__main__' :
  data_config = load_file_config()
  print(f"Server running: http://{data_config['url-backend']}:{data_config['port']}")
  serve(app, host=data_config["url-backend"], port=data_config["port"])