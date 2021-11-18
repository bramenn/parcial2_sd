import socket
import os
import time
import threading

# Se inicializan las varibles para abrir los sockets
TCP_IP = "localhost"
TCP_PORT = 5004
BUFFER_SIZE = 1024
# RUTA = "D:/Universidad/Sistemas distribuidos/Parcial 2/"
CONT = 1

# Se define un diccionario con los puertos para los servidores lideres
dicLideres = {
    1: {1: 5006},
    2: {1: 5027},
    3: {1: 5048},
    4: {1: 5069},
    5: {1: 5080},
    6: {1: 5100},
    7: {1: 5120},
}

# Se define un diccionario para crear grupos
dicGrupos = {}

# Se abre el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se agrega bind para que se conecten los clientes
sock.bind((TCP_IP, TCP_PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.listen(5)

print("Servidor escuchando....")


def ejecutar():
    """Se ejecuta el archivo que se creo con los datos del nuevo servidor"""
    os.system("S" + str(CONT) + ".py")


def CrearArchivoServidor(puerto):
    """Se crea un archivo servidor (S[CONT].py)"""
    # Se coloca la variable global para que sea editable ne esta funcion
    global CONT
    # Se abre la plantilla SPlantilla.txt
    archivo1 = open("SPlantilla.txt", "r")
    # Se lee el archivo en la variable aux
    aux = archivo1.read()
    # Se abre la plantilla SPlantilla2.txt
    archivo2 = open("SPlantilla2.txt", "r")
    # Se lee el archivo en la variable aux2
    aux2 = archivo2.read()

    # Se crea el archivo S[CONT].py
    archivo3 = open("S" + str(CONT) + ".py", "w")
    # Se fusiona la plantilla SPlantilla.txt y SPlantilla2.txt y se define el puerto
    archivo3.write(aux + str(puerto) + "\n" + aux2)

    # Se cierran los archivos
    archivo1.close()
    archivo2.close()
    archivo3.close()

    # Se suma 1 al contador para que le siguiente archivo sea SÑCONT]+1.py
    CONT += 1
    print("Servidor creado..")

def creaHiloServidor(crearS):
    aux = len(dicGrupos.__getitem__(crearS))
    (dicGrupos[crearS])[aux + 1] = (dicGrupos[crearS])[aux] + 1
    print(dicGrupos)

    puerto = (dicGrupos[crearS])[aux] + 1
    CrearArchivoServidor(puerto)
    thread1 = threading.Thread(target=ejecutar)
    thread1.start()

def crearServidor(crearS):
    """Se crea un servidor basado en la opcion del cliente"""
    if dicGrupos.__contains__(crearS):

        if crearS == 1:
            creaHiloServidor(crearS)

        elif crearS == 2:
            creaHiloServidor(crearS)

        elif crearS == 3:
            creaHiloServidor(crearS)

        elif crearS == 4:
            creaHiloServidor(crearS)

        elif crearS == 5:
            creaHiloServidor(crearS)

        elif crearS == 6:
            creaHiloServidor(crearS)

        elif crearS == 7:
            creaHiloServidor(crearS)

    elif True:
        print("El grupo no existe...")


def unirAGrupo(tipoGrupo, conn):
    """Une un servidor a un grupo"""

    #
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
    """Lista todos los grupos que existan"""

    # Verifica sis existe la varible crear en el diccionario grupo
    if dicGrupos.__contains__(crear):
        # Se saca una varaible auxiliar
        dicAux = dicGrupos[crear]
        # Se envia el diccionario auxialiar
        conn.send(str(dicAux).encode("UTF-8"))
        # Se crea un grupo tipo suma
        if crear == 1:
            print("Grupo suma: ", dicAux)
            return dicAux
        # Se crea un grupo tipo resta
        elif crear == 2:
            print("Grupo resta: ", dicAux)
            return dicAux
        # Se crea un grupo tipo multiplicacion
        elif crear == 3:
            print("Grupo multiplicacion: ", dicAux)
            return dicAux
        # Se crea un grupo tipo division
        elif crear == 4:
            print("Grupo division: ", dicAux)
            return dicAux
        # Se crea un grupo tipo potencia
        elif crear == 5:
            print("Grupo potencia: ", dicAux)
            return dicAux
        # Se crea un grupo tipo logaritmo
        elif crear == 6:
            print("Grupo logaritmo: ", dicAux)
            return dicAux
        # Se crea un grupo tipo raiz
        elif crear == 7:
            print("Grupo raiz: ", dicAux)
            return dicAux
    elif True:
        print("El grupo solicitado no existe...")


while True:
    # Se acepta una conexion
    conn, addr = sock.accept()
    # Se recibe una data para procesarla
    data = eval(conn.recv(BUFFER_SIZE).decode("UTF-8"))
    print("datos recibidos ", data, "Desde ", addr)
    # Se envia una respuesa al cliente conectado
    conn.send("Recibido".encode("UTF-8"))

    # Se saca el operando de la data
    operando = int(data.get("Operando"))
    # Se saca el numero1 de la data
    num1 = str(data.get("Numero1"))
    # Se saca el numero2 de la data
    num2 = str(data.get("Numero2"))
    # Se saca la variable crearS
    crearS = int(data.get("CrearS"))

    # Se verifica si es una operacion matematica
    if operando >= 1 and operando <= 7:
        # Se revisa que exista el operenado
        if dicGrupos.__contains__(operando):
            # Se crea un segundo socket
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Se conecta al servidor lider dato el operando
            sock2.connect((TCP_IP, int(dicGrupos.get(operando).__getitem__(1))))

            # Se crea un diccionario para realizar la operacion
            datos = {
                "Operando": operando,
                "Numero1": num1,
                "Numero2": num2,
                "Servidores": dicGrupos.get(operando),
            }

            # Se envia esta operacion al servidor lider
            sock2.send(str(datos).encode("UTF-8"))
            print("Datos enviados: ", datos)
            # Se recibe una respuesta del servidor lider
            total = sock2.recv(BUFFER_SIZE).decode("UTF-8")
            # Se recibe una respuesta del servidor lider
            total = sock2.recv(BUFFER_SIZE).decode("UTF-8")
            # Se envia la respuesta al cliente
            conn.send(total.encode("UTF-8"))
            print("Total enviado...")
            conn.close()

    # Entra aqui si es se tiene que crear un servidor
    elif operando == 8:
        crearServidor(crearS)

    # Entra aqui si es se tiene que unir un grupo
    elif operando == 9:
        unirAGrupo(crearS, conn)

    # Entra aqui si es se tiene que crear un grupo
    elif operando == 10:
        crearGrupo(crearS)

    # Entra aqui si es se tiene que eliminar un grupo
    elif operando == 11:
        eliminarGrupo(crearS)

    # Entra aqui si es se tiene que listar los grupos
    elif operando == 12:
        listarGrupos(crearS)

    conn.close()
