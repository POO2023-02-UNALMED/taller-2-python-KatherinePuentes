class Asiento:
    def __init__(self, color, precio, registro):
        self.color= color
        self.precio= precio
        self.registro= registro

    def cambiarColor(self, color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color=color


class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo= modelo
        self.precio = precio
        self.asientos =asientos
        self.marca = marca
        self.motor= motor
        self.registro= registro

    def cantidadAsientos(self):
        cantidad= 0
        for asiento in self.asientos:
            if asiento is not None:
                cantidad+=1
        return cantidad
    
    def verificarIntegridad(self):
        if self.esIntegro():
            return "Auto original"
        else:
            return "Las piezas no son originales"


    def esIntegro(self):
        if self.motor.registro!=self.registro:
            return False
        
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return False
        
        return True
    

class Motor:
    def __init__(self, numero, tipo, registro):
        self.numero= numero
        self.tipo= tipo
        self.registro= registro

    def cambiarRegistro(self, registro):
        self.registro= registro

    def asignarTipo(self, tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo=tipo