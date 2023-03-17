from ingrediente import *


class Receta:
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos

    def __str__(self):
        return f"{self.nombre} - Ingredientes: {[str(i) for i in self.ingredientes]} - Pasos: {self.pasos}"

    def agregar_ingrediente(self, nombre, cantidad, unidad_de_medida):
        ingrediente = Ingrediente(nombre, cantidad, unidad_de_medida)
        self.ingredientes.append(ingrediente)

#prueba pull request 
