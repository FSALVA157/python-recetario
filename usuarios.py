#import uuid
import json
from servicio import *

class Usuarios:
    nombre_archivo = "usuariosDB.json"
    #lista_usuarios = [{"username": "Fernando", "clave": "1234", "id": "uuid.uuid4()"}] ## No se como hacer para que el id sea solo para ese username

    def __init__(self):
        self.userService = FileManager(Usuarios.nombre_archivo)
    #     self.username = username
    #     self.clave = clave
    #     self.id = uuid.uuid4()

    def crearDB(self):
        try: 
            self.userService.create({"xxavier": "123456"})
        except Exception as e:
            raise Exception(f"errof: {e}")
        


    def login(self, username, clave):
        try:
            usuario_activo = self.userService.getOne(username)
            if(clave != usuario_activo):
                return {
                "status": False,
                "message": "La clave Ingresada es Erronea"
                     }
        except Exception as e:
            #raise Exception(f"errof: {e}")
            return {
                "status": False,
                "message": str(e)
            }
        else:
            return {
                "status": True,
                "message": "Login Exitoso"
            }


    
    def mostrar_usuarios(self):
        try:
            usuarios = self.userService.getAll()        
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:         
         return {
             "status": True,
             "usuarios": usuarios
         }
    
    
    def crear_usuario(self, username: str, clave: str):
        try:
            dato = self.userService.getOne(username)            
            if(dato['status'] == True):
               return {
                    "status": False,
                    "message": "El usuario ya existe"
                    }                        
            self.userService.addOne(username, clave)
        except Exception as e:            
            return {
                "status": False,
                "message": str(e)
            }
        else:

            return{
                    "status": False,
                    "message": f"El usuario {username} ha sido creado con Exito!"
            }


        # for usuario in self.lista_usuarios:
        #     if usuario["username"] == username:
        #         print("El nombre de usuario esta en uso")
        #     else:
        #         nuevo_usuario = {"username": username, "clave": clave, "id" : uuid.uuid4}
        #         self.lista_usuarios.append(nuevo_usuario)
        #         print("El nuevo usuario se ha creado exitosamente.")
        ##Deberiamos pedir confirmacion de contraseña?? Como hacerlo

#     def eliminar_usuario(self, username):
#         for usuario in self.lista_usuarios:
#             if usuario["username"] == username:
#                 self.lista_usuarios.remove(usuario)
#                 print(f"El usuario {username} ha sido eliminado correctamente.")
#             else:
#                 print(f"El usuario {username} no existe.")
        
# username= input("Ingrese nombre de usuario: ")
# clave= input("Ingrese la clave: ")
# u1=Usuarios(username, clave)

# u1.login()

# u1.mostrar_usuarios()

# u1.crear_usuario(input("Ingrese un nombre de usuario: "), input("Ingrese una clave: "))

# u1.eliminar_usuario(input("Ingrese el nombre de usuario que desea eliminar: "))