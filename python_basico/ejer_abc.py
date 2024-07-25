a = int(input("Ingrese primer valor "))
b = int(input("Ingrese segundo valor "))
c = int(input("Ingrese tercer valor "))

#JOEL
if a > b:
    if b > c:
        print(a,b,c)
    else:
        print(a,c,b)
else:
    if b > c:
        if c > a:
            print(b,c,a)
        else:
            print(b,a,c)
    else:
        if b > a:
            print(c,b,a)
        else:
            print(c,a,b)

#PABLO
a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

# Verificar y ordenar los números
if a > b and a > c:
    if b > c:
        print('El orden de los números es:', a, b, c)
    else:
        print('El orden de los números es:', a, c, b)
elif b > c and b > a:
    if a > c:
        print('El orden de los números es:', b, a, c)
    else:
        print('El orden de los números es:', b, c, a)
else:
    if a > b:
        print('El orden de los números es:', c, a, b)
    else:
        print('El orden de los números es:', c, b, a)