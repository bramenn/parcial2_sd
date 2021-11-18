import socket
import os
import time
import threading

TCP_IP = "localhost"
TCP_PORT = 5004
BUFFER_SIZE = 1024
# RUTA = "D:/Universidad/Sistemas distribuidos/Parcial 2/"
CONT = 1

dicLideres = {
    1: {1: 5006},
    2: {1: 5027},
    3: {1: 5048},
    4: {1: 5069},
    5: {1: 5080},
    6: {1: 5100},
    7: {1: 5120},
}

dicGrupos = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)

print("Servidor escuchando....")


def ejecutar():
    os.system("S" + str(CONT) + ".py")


def CrearArchivoServidor(puerto, cont):
    archivo1 = open("./id_eider/SPlantilla.txt", "r")
    aux = archivo1.read()

    archivo2 = open("./id_eider/SPlantilla2.txt", "r")
    aux2 = archivo2.read()

    archivo3 = open("./id_eider/S" + str(cont) + ".py", "w")
    archivo3.write(aux + str(puerto) + "\n" + aux2)

    archivo1.close()
    archivo2.close()
    archivo3.close()

    cont += 1
    print("Servidor creado..")

    return cont


def crearServidor(crearS, cont):
    if dicGrupos.__contains__(crearS):

        if crearS == 1:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont

        elif crearS == 2:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont

        elif crearS == 3:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont

        elif crearS == 4:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont

        elif crearS == 5:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont

        elif crearS == 6:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont

        elif crearS == 7:
            aux = len(dicGrupos.__getitem__(crearS))
            (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
            print(dicGrupos)

            puerto = (dicGrupos[crearS])[aux] + 1
            cont = CrearArchivoServidor(puerto, cont)
            thread1 = threading.Thread(target=ejecutar)
            thread1.start()
            return cont
    elif True:
        print("El grupo no existe...")


def unirAGrupo(tipoGrupo, conn):
    dicAux = listarGrupos(tipoGrupo)
    print(dicAux, type(dicAux))
    conn.send(str(dicAux).encode("UTF-8"))

    data = eval(conn.recv(BUFFER_SIZE).decode("UTF-8"))

    puerto = int(data.get("Puerto"))
    servidor = int(data.get("Servidor"))

    dicAux = listarGrupos(servidor)
    dicAux[len(dicAux) + 1] = puerto
    dicGrupos[servidor] = dicAux


def crearGrupo(tipoGrupo):
    if dicGrupos.__contains__(tipoGrupo):
        print("El grupo ya existe...")
    elif tipoGrupo == 1:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)
    elif tipoGrupo == 2:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)
    elif tipoGrupo == 3:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)
    elif tipoGrupo == 4:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)
    elif tipoGrupo == 5:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)
    elif tipoGrupo == 6:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)
    elif tipoGrupo == 7:
        dicGrupos[tipoGrupo] = dicLideres.get(tipoGrupo)


def eliminarGrupo(tipoGrupo):
    if dicGrupos.__contains__(tipoGrupo):
        dicGrupos.pop(tipoGrupo)
    elif True:
        print("El servidor no se encuentra...")


def listarGrupos(crear):
    if dicGrupos.__contains__(crear):
        dicAux = dicGrupos[crear]
        conn.send(str(dicAux).encode("UTF-8"))
        if crear == 1:
            print("Grupo suma: ", dicAux)
            return dicAux
        elif crear == 2:
            print("Grupo resta: ", dicAux)
            return dicAux
        elif crear == 3:
            print("Grupo multiplicacion: ", dicAux)
            return dicAux
        elif crear == 4:
            print("Grupo division: ", dicAux)
            return dicAux
        elif crear == 5:
            print("Grupo potencia: ", dicAux)
            return dicAux
        elif crear == 6:
            print("Grupo logaritmo: ", dicAux)
            return dicAux
        elif crear == 7:
            print("Grupo raiz: ", dicAux)
            return dicAux
    elif True:
        print("El grupo solicitado no existe...")


while True:
    conn, addr = s.accept()
    data = eval(conn.recv(BUFFER_SIZE).decode("UTF-8"))
    print("datos recibidos ", data, "Desde ", addr)
    conn.send("Recibido".encode("UTF-8"))

    op = int(data.get("Operando"))
    num1 = str(data.get("Numero1"))
    num2 = str(data.get("Numero2"))
    crearS = int(data.get("CrearS"))

    if op >= 1 and op <= 7:
        if dicGrupos.__contains__(op):
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2.connect((TCP_IP, int(dicGrupos.get(op).__getitem__(1))))

            datos = {
                "Operando": op,
                "Numero1": num1,
                "Numero2": num2,
                "Servidores": dicGrupos.get(op),
            }

            s2.send(str(datos).encode("UTF-8"))
            print("Datos enviados: ", datos)
            total = s2.recv(BUFFER_SIZE).decode("UTF-8")

            total = s2.recv(BUFFER_SIZE).decode("UTF-8")
            conn.send(total.encode("UTF-8"))
            print("Total enviado...")
            conn.close()
    elif op == 8:
        CONT = crearServidor(crearS, CONT)

    elif op == 9:
        unirAGrupo(crearS, conn)

    elif op == 10:
        crearGrupo(crearS)

    elif op == 11:
        eliminarGrupo(crearS)

    elif op == 12:
        listarGrupos(crearS)

    conn.close()
