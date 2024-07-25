'''
Niñez: Desde el nacimiento hasta los 12 años.
Adolescencia: 13-18 años.
Adultez: Desde los 18 años hasta los 65 años.
Vejez: 65 años en adelante.
'''

edad = int(input("ingrese su edad: "))

if edad <= 12:
    print("Usted es Niño/a de edad")
else:
    if edad <= 18:
        print("Usted es Adolecente de edad")
    else:
        if edad <= 65:
            print("Usted es Adulto de edad")
        else:
            print("Usted es en la Vejez de edad")

if edad <= 12:
    print("Usted es Niño/a de edad")
elif edad <= 18:
    print("Usted es Adolecente de edad")
elif edad <= 65:
    print("Usted es Adulto de edad")
else:
    print("Usted es en la Vejez de edad")







