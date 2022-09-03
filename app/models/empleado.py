from functools import reduce


class Empleado:
    def __init__(self, nombre, cedula, salario):
        self.nombre = nombre
        self.cedula = cedula
        self.salario = salario

class Empleados:
    def __init__(self):
        self.empleados = []
        # Seeders
        self.nuevoEmpleado(nombre="Petter Meave", cedula="4832802", salario=1500)
        self.nuevoEmpleado(nombre="Jamel Alcoba", cedula="3456789", salario=1600)
        self.nuevoEmpleado(nombre="Mathew Meave", cedula="123400123", salario=1400)
        self.nuevoEmpleado(nombre="Andrew Meave", cedula="1234001456", salario=1000)

    def nuevoEmpleado(self, **params):
        self.empleados.append(Empleado(**params))

    def nuevoEmpleadoJSON(self, data):
        self.nuevoEmpleado(nombre=data["nombre"], cedula=data["cedula"], salario=data["salario"])

    def listarEmpleados(self):
        return self.empleados

    def listarEmpleadosJSON(self):
        lista = []
        for item in self.empleados:
            lista.append({
                "nombre": item.nombre,
                "cedula": item.cedula,
                "salario": item.salario,
            })
        return lista

    def mostrarEmpleado(self, index):
        return self.empleados[index]

    def mostrarEmpleadoJSON(self, index):
        item = self.empleados[index]
        return {
            "nombre": item.nombre,
            "cedula": item.cedula,
            "salario": item.salario,
        }

    def editarEmpleado(self, index, **params):
        self.empleados[index] = Empleado(**params)

    def eliminarEmpleado(self, index):
        del self.empleados[index]

    def sumarSalario(self):
        total_sum = reduce(lambda x, y: x + y.salario, self.empleados, 0)
        return total_sum
