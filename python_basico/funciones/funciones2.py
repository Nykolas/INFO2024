# VALORES DE PARAMTEROS POR DEFECTO
'''
#EJEMPLO 1
def saludar(nombre, cargo = 'Sin Cargo'):

    print(f"Hola {cargo}, {nombre}")
n = 'Nicolas'
c = 'Docente'
saludar(n,c)
saludar(n)

#EJEMPLO 2
def precioFinal(c,p,iva = None):
    if iva:
        r = (c*p*iva) + (c*p)
    else:
        r = c*p
    return r

res = precioFinal(10,2, 0.21)
print(res)

res = precioFinal(10,2)
print(res)
'''

# PARAMETROS *arg y  **kwargs

def saludar(mensaje, *args):
    print(mensaje)
    for i in args:
        print(i)
    
saludar('Welcome to info','nico','nara','juan','brian')

def saludar(mensaje, **kwargs):
    print(mensaje)
    for k,v in kwargs.items():
        print(f'{k}-->{v}')
    
saludar('Welcome to info', gerentes = 'nico y nara', ventas= 'juan',deposito= 'brian')

