'''
def sumar(a,b): #a = x = 5 ; b = y = 3
    r = a+b
    return r

x = int(input("ingrese N1: ")) #5
y = int(input("ingrese N2: ")) #3

resultado = sumar(x,y) #x = 5, y = 3

print(resultado)
'''
'''
#DADO UN NUMERO N, HACER UNA FUNCION, QUE RETORNE, LA SUMA DE SUS DIVISORES.
# N = 10, resultado sera = 10+5+2+1 = 18

#SOLUCION DE JUAN

def divisores(n):
    total = 0
    for i in range(1,n + 1):
        if n % i == 0:
            total += i
    return total


numero = int(input("INGRESE SU NUMERO N: "))
resultado = divisores(numero)
print(f"la suma de los divisores de {numero} es {resultado}")
'''

#SOLUCION DE BRIAN
def divisores_sum(a):

    sum = 0
    x = 1
    while x <= a:
        if a % x == 0:
            sum += x
        x += 1
    return sum

num = 10
print(f"sumar los divisores de {num} da {divisores_sum(num)}")
