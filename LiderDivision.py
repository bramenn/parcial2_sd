import socket
import random

# Se inicializan las varibles para abrir los sockets
TCP_IP = "localhost"
TCP_PORT = 5069
BUFFER_SIZE = 1024

# Se abre el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se agrega bind para que se conecten los clientes
sock.bind((TCP_IP, TCP_PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Se abre el socket para que 5 cliemtes se conecten
sock.listen(5)

print("Servidor escuchando....")

while True:
    # Se acepta una conexion
    conn, addr = sock.accept()
    # Se recibe una data para procesarla
    data = eval(conn.recv(BUFFER_SIZE).decode("UTF-8"))
    print("Datos recibidos ", data, "desde", addr)
    # Se envia una respuesa al cliente conectado
    conn.send("Recibido".encode("UTF-8"))

    # Se saca el operando de la data
    operando = str(data.get("Operando"))
    # Se saca el numero1 de la data
    num1 = str(data.get("Numero1"))
    # Se saca el numero2 de la data
    num2 = str(data.get("Numero2"))
    # Se saca el diccionario de servidores de la data
    dic = dict(data.get("Servidores"))

    # Se elije un servidor de manera aleatoria (dada la cantidad de servidores en este grupo)
    servidorElegido = random.randint(2, len(dic))
    print("El servidor elegido fue el puerto: ", dic.get(servidorElegido))

    # Se abre el socket 2 para el servidor elegido
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Se conecta al servidor elegido
    sock2.connect((TCP_IP, dic.get(servidorElegido)))
    sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Se crea un diccionario con los datos que se trajo en la primera conexion
    datos = {"Operando": operando, "Numero1": num1, "Numero2": num2, "Servidores": dic}
    # Se le envia esta informacion al el servidor elegido
    sock2.send(str(datos).encode("UTF-8"))
    print("Datos enviados ", datos)
    # Se recibe la respuesta de la operacion del servidor elegido
    total = sock2.recv(BUFFER_SIZE).decode("UTF-8")
    # Se recibe la respuesta de la operacion del servidor elegido
    total = sock2.recv(BUFFER_SIZE).decode("UTF-8")

    print("Total: ", total, "recibido")
    # Se envia el resultado al servidor de grupos
    conn.send(total.encode("UTF-8"))
    print("Total enviado...")
    # Se cierra la conexion
    conn.close()
import socket
import random

TCP_IP = "localhost"
TCP_PORT = 5069
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)

print("Servidor escuchando....")

while True:
    conn, addr = s.accept()
    data = eval(conn.recv(BUFFER_SIZE).decode("UTF-8"))
    print("Datos recibidos ", data, "desde", addr)
    conn.send("Recibido".encode("UTF-8"))

    op = str(data.get("Operando"))
    num1 = str(data.get("Numero1"))
    num2 = str(data.get("Numero2"))
    dic = dict(data.get("Servidores"))

    servidorElegido = random.randint(2, len(dic))
    print("El servidor elegido fue el servidor con puerto: ", dic.get(servidorElegido))

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((TCP_IP, dic.get(servidorElegido)))
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    datos = {"Operando": op, "Numero1": num1, "Numero2": num2, "Servidores": dic}
    s2.send(str(datos).encode("UTF-8"))
    print("Datos enviados ", datos)
    total = s2.recv(BUFFER_SIZE).decode("UTF-8")
    total = s2.recv(BUFFER_SIZE).decode("UTF-8")

    print("Total: ", total, "recibido")
    conn.send(total.encode("UTF-8"))
    print("Total enviado...")
    conn.close()
