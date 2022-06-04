from flask import Flask, jsonify, request
app = Flask(__name__)

estudiantes =[{"nombre":"Juan", "cedula":"100", "telefono":"100"},{"nombre":"Camilo", "cedula":"101","telefono":"101"}]

@app.route("/")
def index():
    return '{"mensaje":"Esta Api es de un Listado de Estudiantes"}'


@app.route("/addestudiante/", methods=['POST'])
@app.route("/addestudiante/<estudiante>", methods=['POST'])
def add(estudiante=""):
    if estudiante=="":
        return jsonify('{"mensaje":"ingrese los datos del estudiante separados con :"}')
    else:
        estudiante_dividido=estudiante.split(":")
        estudiante_a_insertar={"nombre":estudiante_dividido[0],"cedula":estudiante_dividido[1],"telefono":estudiante_dividido[2]}
        estudiantes.append(estudiante_a_insertar)
        return jsonify('{"mensaje":"Se ingresó el estudiante correctamente"}')


@app.route("/deleteestudiantes", methods=['DELETE'])
@app.route("/deleteestudiantes/<posicion>", methods=['DELETE'])
def delete(posicion=""):
    if posicion=="":
        return jsonify('{"mensaje":"Debe ingresar la posicion a eliminar"}'),500
    else:
        estudiantes.pop[posicion]
        return jsonify('{"mensaje":"Se eliminó correctamente el estudiante"}')

@app.route("/listaestudiantes", methods=['GET'])
def lista():
    return jsonify(estudiantes)

