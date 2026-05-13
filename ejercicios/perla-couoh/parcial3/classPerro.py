class Perro:
    # Constructor de la clase Perro
    especie = "Canis lupus familiaris"  # Atributo de clase compartido por todos los perros

    def __init__(self, nombre, raza = "Caramelo", edad = 0):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

# Método para imprimir los datos del perro
    def imprimirDatos(self):
        print("Nombre: {self.nombre}")
        print("Raza: {self.raza}")
        print("Edad: {self.edad} edad")
        print("Especie: {self.especie}")


#Creacion de un objeto de la clase Perro
def main():
    perro1 = Perro("Firulais", "Labrador", 5)
    perro1.imprimirDatos()
    perro2 = Perro("Rex", "Pastor Alemán", 3)
    perro2.imprimirDatos()
    print("Información del perro 2:",perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("Max", "Bulldog", 2)
    perro3.imprimirDatos()
    print("Información del perro 3:",perro3.nombre, perro3.raza, perro3.edad) 
    perro4 = Perro("Dante")
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "Pastor Belga"
    perro2.imprimirDatos()
    perro5 = Perro("Raya", "Siamés", 1)
    perro5.imprimirDatos()
    


    if __name__ == "__main__":
        main()