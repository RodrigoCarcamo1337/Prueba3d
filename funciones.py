Comunas = ["chorrillos", "hospital", "centro", "miramar"]


Pedidos = []


def RegistrarPedido():

    Clientes = input("Ingrese nombre del cliente: ")
    Ubicacion = input("Ingrese la direccion de entrega: ")


    while True:
        try:
            Sectores = input("Ingrese el secotr a entregar: ").lower()
            if Sectores in Comunas:
                Direcciones = Sectores
                break
            else:
                print("Sector no encontrado, intentelo de nuevo")
        except ValueError:
            print("Sector no encontrado, intentelo de nuevo")

    while True:
        try:
            Cilindrode5Kg = int(input("Ingrese la cantidad de cilindros de 5Kg: "))
            if Cilindrode5Kg >= 0:
                print("Cantidad valida")
                break
            else:
                print("Cantidad no valida, intentelo de nuevo")
                Cilindrode5Kg = int(input("Ingrese la cantidad de cilindros de 5Kg: "))
        except ValueError:
            print("Ingrese una cantidad valida")

    while True:
        try:
            Cilindrode15Kg = int(input("Ingrese la cantidad de cilindros de 15Kg: "))
            if Cilindrode15Kg >= 0:
                print("Cantidad valida")
                break
            else:
                print("Cantidad no valida, intentelo de nuevo")
        except ValueError:
            print("Ingrese una cantidad valida")

    while True:
        try:
            Cilindrode45Kg = int(input("Ingrese la cantidad de cilindros de 45Kg: "))
            if Cilindrode45Kg >= 0:
                print("Cantidad valida")
                break
            else:
                print("Cantidad no valida, intentelo de nuevo")
        except ValueError:
            print("Ingrese una cantidad mayor a 0")

    Pedidos.append({
        "Cliente: " : Clientes,
        "Direccion: " : Direcciones,
        "Sector: " : Sectores,
        "Cilindro de 5Kg: " : Cilindrode5Kg,
        "Cilindro de 15Kg: " : Cilindrode15Kg,
        "Cilindro de 45Kg: " : Cilindrode45Kg,
    
    })
    print("Pedido registrado con exito")


def ListarPedidos():
    print(Pedidos)

def ImprimirHojaRuta():
    SectorBusqueda = input("Ingrese el sector en el que desea realizar la entrega: ").lower()

    if SectorBusqueda not in Comunas:
        print("Sector no encontrado, Volviendo al menu principal")
    else:
        with open("Pedidos.txt", "w") as archivoPedidos:
            archivoPedidos.write("Pedidos a entregar en el sector de: " + SectorBusqueda + "\n")
            for pedido in Pedidos:
                if pedido["Sector: "] == SectorBusqueda:
                    archivoPedidos.write("Cliente: " + pedido["Cliente: "] + "\n")
                    archivoPedidos.write("Direccion: " + pedido["Direccion: "] + "\n")
                    archivoPedidos.write("Cilindro de 5Kg: " + str(pedido["Cilindro de 5Kg: "]) + "\n")
                    archivoPedidos.write("Cilindro de 15Kg: " + str(pedido["Cilindro de 15Kg: "]) + "\n")
                    archivoPedidos.write("Cilindro de 45Kg: " + str(pedido["Cilindro de 45Kg: "]) + "\n")
                    archivoPedidos.write("-----------------------------------\n")
                else:
                    print("Error")
