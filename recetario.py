import json
from servicio import *




class Recetario:
    nombre_archivo = "recetasDB.json"
    def __init__(self):
        self.recetario
    
    def crearDB(self):
       try: 
           self.userService.create({"guiso": "123456"})
       except Exception as e:
           raise Exception(f"errof: {e}")