
''' es la funcion (que se situa en la capa de aplicacion -proceso-) que calcula el valor del termino n_esimo de 
la serie de Fibonnacci '''


def fibon (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibon (n - 2) + fibon (n - 1)




    