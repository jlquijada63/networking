
''' Ejercicio que consiste en un esquema cliente-servidor donde el cliente envia al servidor un numero entero n y este le devuelve
el valor del termino n_esimo de la serie de Fibonnacci '''

from socket import *
from argparse import *

parser = ArgumentParser(description="Calcula el valor del termino n_esimo de la serie de fibonacci")
parser.add_argument('-n','--number',type=int, help="n_esimo termino de la serie de Fibonaccci")
params = parser.parse_args()


server_host = 'localhost'    # direcccion del servidor
server_port = 12000         # puerto al que se dirige el cliente

client_socket = socket (AF_INET, SOCK_DGRAM)    # instancia un socket de tipo AF_INET (IP v4) y tipo (UDP)


number = params.number
b_number = number.to_bytes(2, "little")         # convierte el entero en bytes 
client_socket.sendto(b_number, (server_host, server_port))
res, server_add = client_socket.recv(2048)
print (f"El valor del termino {number}_esimo de la serie de Fibonnacci es: {int(res)}")
client_socket.close

