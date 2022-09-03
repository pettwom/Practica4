from app import app
from flask import render_template
from flask import jsonify
from flask import request
from app.models.empleado import Empleados
from flask import jsonify


empleados = Empleados()

@app.route('/', methods = ['GET'])
def index():
    items = empleados.listarEmpleados()
    return render_template('empleados.html', items=items)

@app.route('/empleados', methods = ['GET'])
def listarEmpleados():
    items = empleados.listarEmpleadosJSON()
    return jsonify(items), 200

@app.route('/empleados/<int:id>', methods = ['GET'])
def mostrarEmpleados(id):
    item = empleados.mostrarEmpleadoJSON(id)
    return jsonify(item), 200

@app.route('/empleados', methods = ['POST'])
def agregarEmpleados():
    empleados.nuevoEmpleadoJSON(request.json)
    return jsonify({"mensaje": "Agregacion satisfactoria"}), 201

@app.route('/empleados/<int:id>', methods = ['DELETE'])
def eliminarEmpleado(id):
    empleados.eliminarEmpleado(id)
    return jsonify({"mensaje": "Eliminacion satisfactoria"}), 201

@app.route('/salarios/total_ganado', methods = ['GET'])
def salariosTotal():
    total = empleados.sumarSalario()
    return jsonify({
        "total": total,
        "status": 200,
        "Message": "Salario Total Ganado"
    }), 200
