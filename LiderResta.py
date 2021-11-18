# lo que quieras




import socket
import random

TCP_IP = "localhost"
TCP_PORT = 5027
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
    print("El servidor elegido fue el puerto: ", dic.get(servidorElegido))

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
