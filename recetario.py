import json
from servicio import *
from ingrediente import *
from receta import *

class Recetario:
    nombre_archivo = "recetasDB.json"

    def __init__(self):
        self.recetarioService = FileManager(Recetario.nombre_archivo)
    
    def crearDB(self):
       try: 
           self.recetarioService.create({"guiso": {
               "ingredientes": [{
                    "nombre" : "papa",
                    "cantidad" : "1",
                    "unidad_de_medida" : "kg"
               },
               {
                    "nombre" : "carne",
                    "cantidad" : "0.5",
                    "unidad_de_medida" : "kg"
               }
               ],
               "preparacion": ["picar papa","picar carne"],
               "imagenes": ["ruta imagen 1","ruta imagen 2"],
               "duracion": "30 min",
               "coccion": "60 min",
               "fecha": "03/03/2023",
               "etiquetas": ["guiso", "carne","caliente"],
               "favorita": "True"}
               })
       except Exception as e:
           raise Exception(f"errof: {e}")
       
