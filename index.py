from servicio import *
from usuarios import *

#archivo1 = FileManager('db.json')
#archivo1.create({"Guiso": "Receta de Guiso","Sopa": "Receta de Sopa","Empanada": "Receta de Empanada"})
#print(archivo1.getAll())
#print(archivo1.getOne("Guiso majo"))

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
print(yo.login("xxavier","123456"))