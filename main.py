import funciones as funcionMaestra

while True:
    try:
        print("Bienvenido a Gaxplosive (Gas Explosivo de calidad)!")
        print("1. Registrar pedido")
        print("2. Listar los todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")

        opc = int(input("Ingrese una opcion: "))

        if opc == 1:
            print("Opcion 1 ingresada")
            funcionMaestra.RegistrarPedido()
        
        elif opc == 2:
            print("Opcion 2 ingresada")
            funcionMaestra.ListarPedidos()
        
        elif opc == 3:
            print("Opcion 3 ingresada")
            funcionMaestra.ImprimirHojaRuta()
        
        elif opc == 4:
            print("Saliendo del programa...")
            break

    except ValueError:
        print("opcion no valida")