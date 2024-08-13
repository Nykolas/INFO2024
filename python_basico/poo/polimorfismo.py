class Empleado:
    def __init__(self,sueldo):
        self.sueldo = sueldo

    def calcular_salario_anual(self):
        salario =  12 *  self.sueldo * 1.1
        print(f'Mi salario como Empleado es: {salario}')

class Programador(Empleado):
    def calcular_salario_anual(self):
        salario = 12 * self.sueldo * 1.15
        print(f'Mi salario como Programador es: {salario}')
    
class Diseñador(Empleado):
    def calcular_salario_anual(self):
        salario = 12 * self.sueldo * 1.2
        print(f'Mi salario como Diseñador es: {salario}')
    
em1 = Empleado(100)
pr1 = Programador(100)
di1 = Diseñador(100)
lista = [em1,pr1,di1]

for x in lista:
    x.calcular_salario_anual()

    