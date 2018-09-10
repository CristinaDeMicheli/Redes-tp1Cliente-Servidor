import socket

mi_socket = socket.socket()
mi_socket.bind( ('localhost',8000) )
mi_socket.listen(5)

While True:
conexion, addr = mi_socket.accept()
print "¡Nueva conexion establecida!"
print addr

conexion.send("Hola, te saludo desde el servidor")
