class Empleado:
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        print(f"{self.nombre} está supervisando al equipo.")

    def supervisarAEquipo(self):
        print(f"{self.nombre} está supervisando a {len(self.equipo)} empleados.")

class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, lenguajeDeProgramacion: str):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")

    def escribirCodigo(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")
