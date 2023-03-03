class Ingrediente:
    def __init__(self, nombre, cantidad, unidad_de_medida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_de_medida = unidad_de_medida

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} {self.unidad_de_medida}"