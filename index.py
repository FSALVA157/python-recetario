from servicio import *
from usuarios import *
import json

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

yo = Usuarios()
#yo.crearDB()
# print(yo.login("xxavier","123456"))
#data = yo.mostrar_usuarios()["usuarios"]
# print(type(data))
#print(data)
res = yo.crear_usuario("marcus","pin1547")
print(res)
# res = yo.eliminar_usuario("marcus")
# print(res)