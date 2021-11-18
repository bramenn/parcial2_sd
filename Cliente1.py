import socket

TCP_IP = "localhost"
TCP_PORT = 5004
BUFFER_SIZE = 1024


def lee_entero():
    while True:
        entrada = input("Escribe un numero entero: ")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")


def listar(dic, crear):
    if dic.__contains__(crear):
        if crear == 1:
            print("Grupo suma: ", dic)

        elif crear == 2:
            print("Grupo resta: ", dic)

        elif crear == 3:
            print("Grupo multiplicacion: ", dic)

        elif crear == 4:
            print("Grupo division: ", dic)

        elif crear == 5:
            print("Grupo potencia: ", dic)

        elif crear == 6:
            print("Grupo logaritmo: ", dic)

        elif crear == 7:
            print("Grupo raiz: ", dic)

    elif True:
        print("El grupo solicitado no existe...")


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print(
        "Que desea realizar: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia"
        + "\n6.Logaritmo\n7.Raiz\n8.Crear servidor\n9.Ingresar servidor a un grupo\n10.Crear Grupo\n11.Eliminar Grupo"
        + "\n12.Listar Grupos"
    )

    op = lee_entero()
    if op >= 1 and op <= 7:
        print("Digite numero1: ")
        num1 = lee_entero()
        print("Digite numero2: ")
        num2 = lee_entero()
        crear = 0
        datos = {"Operando": op, "Numero1": num1, "Numero2": num2, "CrearS": crear, "Puerto": 0}

        s.send(str(datos).encode("UTF-8"))
        data = s.recv(BUFFER_SIZE).decode("UTF-8")
        total = s.recv(BUFFER_SIZE).decode("UTF-8")

        print("El resultado de la operacion fue: ", total)
    elif op > 7:
        if op == 8:
            print(
                "Que tipo de servidor desea crear: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Logaritmo\n7.Raiz"
            )
            crear = lee_entero()

            datos = {
                "Operando": op,
                "Numero1": 0,
                "Numero2": 0,
                "CrearS": crear,
            }
            s.send(str(datos).encode("UTF-8"))
            data = s.recv(BUFFER_SIZE).decode("UTF-8")
            print("Servidor creado....")
        if op == 9:
            clave = 1
            print(
                "Ingrese el grupo en donde se encuentra el servidor que desee agregar a un nuevo grupo:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Logaritmo\n7.Raiz "
            )
            crear = lee_entero()

            datos = {"Operando": op, "Numero1": 0, "Numero2": 0, "CrearS": crear}

            s.send(str(datos).encode("UTF-8"))
            data = s.recv(BUFFER_SIZE).decode("UTF-8")

            dic = eval(s.recv(BUFFER_SIZE).decode("UTF-8"))
            aux = len(dic)
            print("seleccione el puerto del servidor al cual desea cambiar de grupo: ")
            while clave < aux:
                print(str(clave) + ":", dic[clave + 1])
                clave += 1

            op = lee_entero()
            puerto = dic[op + 1]

            print(
                "Indique a que servidor lo quiere unir:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Logaritmo\n7.Raiz "
            )
            servidor = lee_entero()

            datos = {"Puerto": puerto, "Servidor": servidor}

            s.send(str(datos).encode("UTF-8"))
            data = s.recv(BUFFER_SIZE).decode("UTF-8")
            print("Se agrego el servidor al nuevo grupo")

        elif op == 10:
            print(
                "Que grupo desea crear: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Logaritmo\n7.Raiz"
            )
            crear = lee_entero()

            datos = {"Operando": op, "Numero1": 0, "Numero2": 0, "CrearS": crear}

            s.send(str(datos).encode("UTF-8"))
            data = s.recv(BUFFER_SIZE).decode("UTF-8")
            print("Se creo el grupo Exitosamente")

        elif op == 11:
            print(
                "Que grupo desea Eliminar: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Logaritmo\n7.Raiz"
            )
            crear = lee_entero()

            datos = {"Operando": op, "Numero1": 0, "Numero2": 0, "CrearS": crear}

            s.send(str(datos).encode("UTF-8"))
            data = s.recv(BUFFER_SIZE).decode("UTF-8")
            print("Grupo eliminado")

        elif op == 12:
            bandera = False
            print(
                "Que grupo desea listar: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Logaritmo\n7.Raiz"
            )
            crear = lee_entero()

            datos = {"Operando": op, "Numero1": 0, "Numero2": 0, "CrearS": crear}

            s.send(str(datos).encode("UTF-8"))
            data = s.recv(BUFFER_SIZE).decode("UTF-8")
            if bandera == False:
                dic = eval(s.recv(BUFFER_SIZE).decode("UTF-8"))
                dict(dic)
                listar(dic, crear)
            elif bandera:
                listar(dic, crear)
