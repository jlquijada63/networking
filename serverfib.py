
''' servidor que calcula el valor del termino n_enesimo de la serie de Fibonacci '''


from socket import *
from fibon import fibon


server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))   # asocia el socket (server_socket) al puerto 12000. Es decir, cada vez que algo se dirija
                                        # al puerto 12000 de este host sera enviado a este socket
print("El servidor esta listo para la operacion")

while True:     
    b_number, client_add = server_socket.recvfrom(2024)
    int_number = int.from_bytes(b_number,"little")
    result = fibon(int_number)
    server_socket.sendto(result.to_bytes(2,"little"), client_add)
