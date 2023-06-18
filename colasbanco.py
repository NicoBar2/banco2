import random
import time

class Banco:
    def __init__(self):
        self.colaClientes = []
        self.random = random.Random()

    def llegadaCliente(self, cliente):
        self.colaClientes.append(cliente)
        print("Cliente", cliente, "ha llegado al banco.")

    def atencionCliente(self):
        if self.colaClientes:
            cliente = self.colaClientes.pop(0)
            print("Atendiendo al cliente", cliente, ".")
            tiempoAtencion = self.random.randint(5, 15)
            time.sleep(tiempoAtencion)
            print("El cliente", cliente, "ha sido atendido.")
        else:
            print("No hay clientes en la cola.")

if __name__ == '__main__':
    banco = Banco()
    tiempoSimulacion = 60

    print("Bienvenido al Banco")
    print("Iniciando simulación por", tiempoSimulacion, "minutos.")

    for i in range(tiempoSimulacion):
        numeroAleatorio = random.randint(0, 99)
        if numeroAleatorio > 30:
            nuevoCliente = "Cliente " + str(i + 1)
            banco.llegadaCliente(nuevoCliente)
        banco.atencionCliente()

    print("\nGracias por el uso de nuestros servicios.")
