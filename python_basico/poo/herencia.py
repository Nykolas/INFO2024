class Vehiculo:
    def __init__(self, ruedas, marca, modelo, color):
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando.")
    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando.")

class Auto(Vehiculo):
    def __init__(self,ruedas,marca,modelo,color,polarizado):
        super().__init__(ruedas,marca,modelo,color)
        self.esta_polarizado = polarizado

    def acelerar(self):
        super().acelerar()
        print(f'El auto {self.marca} esta pisando el acelerador.')
    def bajar_vidrio(self):
        print(f'El auto {self.marca} esta bajando su vidrio')

class Moto(Vehiculo):
    def acelerar(self):
        super().acelerar()
        print(f'La moto {self.marca} esta girando el acelerador')
    def poner_pata(self):
        print(f'La moto {self.marca} esta bajando la pata.')

auto1 = Auto(4,'toyota','yaris','negro',True)
moto1 = Moto(2,'honda','bis','blanca')
#AUTO
auto1.acelerar()
#auto1.bajar_vidrio()
#MOTO
moto1.acelerar()
#moto1.poner_pata()