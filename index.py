from servicio import *
from usuarios import *
from recetario import *
import json

recet = Recetario()
llave = "sopa"
valor = {
        "ingredientes": [
            {
                "nombre": "papa",
                "cantidad": "1",
                "unidad_de_medida": "kg"
            },
            {
                "nombre": "carne",
                "cantidad": "0.5",
                "unidad_de_medida": "kg"
            }
        ],
        "preparacion": [
            "picar papa",
            "picar carne"
        ],
        "imagenes": [
            "sopa.jpg",
            "/img/plato.png",
        ],
        "duracion": "30 min",
        "coccion": "60 min",
        "fecha": "03/03/2023",
        "etiquetas": [
            "sopa",
            "carne",
            "caliente"
        ],
        "favorita": True
    }

#   llave = "guiso" 
#   valor =  {
#     "ingredientes": [
#       { "nombre": "papa", "cantidad": "1", "unidad_de_medida": "kg" },
#       { "nombre": "carne", "cantidad": "0.5", "unidad_de_medida": "kg" }
#     ],
#     "preparacion": ["picar papa", "picar carne"],
#     "imagenes": ["ruta imagen 1", "ruta imagen 2"],
#     "duracion": "30 min",
#     "coccion": "60 min",
#     "fecha": "03/03/2023",
#     "etiquetas": ["guiso", "carne", "caliente"],
#     "favorita": True
#   },

#recet.filterByLabel('guiso')
#print(recet.filterByLabel('jamon'))
#recet.crearDB()
#print(recet.getOne('guiso')['receta'])
#print(recet.updateOne('sopa',valor)['message'])
#print(recet.getAll()['recetas'])
#print(recet.delOne("sopa"))
print(recet.addOne(llave,valor))
#archivo1 = FileManager('genericoDB.json')
#archivo1.create({"Guiso": "Receta de Guiso","Sopa": "Receta de Sopa","Empanada": "Receta de Empanada"})
#print(archivo1.getAll())
#print(archivo1.getOne("Sopa de arroz"))

#archivo1.borrar("Sopa")
#datos = archivo1.leer()
#print(archivo1.addOne("Pizza", 12545))

# if archivo1.addOne("Sopa Crema","sopa crema de arvejas"):
#     print("EXITO")
# else:
#     print("YA EXISTE LA RECETA")    

#print(archivo1.deleteOne("Pizza"))
#print(archivo1.updateOne("Sopa","sopa de cabello de angel"))

# yo = Usuarios()
# print(yo.crear_usuario("pepe120", "123456"))
#yo.crearDB()
# print(yo.login("xxavier","123456"))
#data = yo.mostrar_usuarios()["usuarios"]
# print(type(data))
#print(data)
#res = yo.crear_usuario("marcus","pin1547")
#print(res)
# res = yo.eliminar_usuario("marcus")
# print(res)
# cocinera = Recetario()
# cocinera.crearDB()
