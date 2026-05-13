class Cuenta:
    
    def __init__(self, cliente, cuenta, saldo=0):

        """
        Constructor de la clase Cuenta. Se ejecuta al crear un objeto nuevo.
        
        Parámetros:
        cliente (str): Nombre del titular de la cuenta.
        cuenta (str): Número o identificador de la cuenta.
        saldo (float, opcional): Saldo inicial. Por defecto es 0.
        """

        # Guardamos el nombre del cliente en el atributo self.Cliente
        self.Cliente = cliente  
        
        # Guardamos el número de cuenta en el atributo self.cuenta
        self.cuenta = cuenta  
        
        # Guardamos el saldo inicial en el atributo self.saldo
        self.saldo = saldo  

    def deposito(self, cantidad):

        """
        Método para depositar dinero a la cuenta.
        
        Parámetros:
        cantidad (float): Monto a depositar. Debe ser mayor a 0.
        
        Retorna:
        bool: True si el depósito fue exitoso, False si la cantidad no es válida.
        """

        # Validamos que la cantidad sea positiva para evitar depósitos negativos
        if cantidad > 0:
            # Si es válida, sumamos la cantidad al saldo actual
            self.saldo += cantidad
            # Retornamos True para indicar que la operación fue exitosa
            return True
        # Si la cantidad es 0 o negativa, no hacemos nada y retornamos False
        return False

    def retiro(self, cantidad):

        """
        Método para retirar dinero de la cuenta.
        
        Parámetros:
        cantidad (float): Monto a retirar. Debe ser > 0 y <= saldo actual.
        
        Retorna:
        bool: True si el retiro fue exitoso, False si no hay fondos o es inválido.
        """

        # Validamos 2 cosas: que sea positiva Y que haya saldo suficiente
        if cantidad > 0 and cantidad <= self.saldo:
            # Si pasa la validación, restamos la cantidad del saldo
            self.saldo -= cantidad
            # Retornamos True para indicar éxito
            return True
        # Si no hay saldo suficiente o la cantidad es inválida, retornamos False
        return False
    
def main():

    """
    Función principal donde se prueba la clase Cuenta.
    Aquí iría el código para crear objetos y usar sus métodos.
    """

    pass  # Por ahora está vacía, solo es un placeholder

# Esta condición verifica si el archivo se ejecuta directamente y no cuando es importado desde otro archivo
if __name__ == "__main__":
    main()  # Si se ejecuta directo, llama a la función main()
    

