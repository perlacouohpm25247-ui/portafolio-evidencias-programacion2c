"""
Crear una clase con los siguientes atributos: nombre, edad, genero, nacionalidad. Agregar un método para imprimir los datos de la persona y otro metodo para calcular el año de nacimiento de la persona. Crea un objeto de la clase Persona y utiliza los métodos para mostrar su información y calcular su año de nacimiento.
"""
import datetime

class Persona:

    def __init__(self, nombre, edad, genero, nacionalidad = "México"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad


    def información(self):
        print("------Información------")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        print(f"Nacionalidad: {self.nacionalidad}")

    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year - self.edad
    
def main():
    objPersona = Persona("Juan", 30, "Masculino")
    objPersona.información()
    print(f"Año de nacimiento: {objPersona.calcularNacimiento()}")

if __name__ == "__main__":
    main()