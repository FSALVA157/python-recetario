import json
from servicio import *

class Usuarios:
    nombre_archivo = "usuariosDB.json"
    

    def __init__(self):
        self.userService = FileManager(Usuarios.nombre_archivo)
    

    def crearDB(self):
        try: 
            self.userService.create({"xxavier": "123456"})
        except Exception as e:
            return {
                "status": False, 
                "message": str(e)
            }
        else:
            return {
                "status": True,
                "message": "El Archivo de Usuario ha sido creado con Exito"
            }

    def login(self, username, clave):
        try:
            usuario_activo = self.userService.getOne(username)            
            if(clave != usuario_activo["data"][username]):
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


    
    def mostrar_usuarios(self)->dict:
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
            #dato = self.userService.getOne(username)            
            dato = self.userService.addOne(username, clave)
            if(dato['status'] == False):
               return {
                    "status": False,
                    "message": "El usuario ya existe"
                    }                             
        except Exception as e:            
            return {
                "status": False,
                "message": str(e)
            }
        else:
            return{
                    "status": True,
                    "message": f"El usuario {username} ha sido creado con Exito!"
            }

  
    def eliminar_usuario(self, username):
        try:
            res = self.userService.getOne(username)
            if(res['status'] == False):
                return{
                    "status": False,
                    "message": f"El usuario {username} no existe"
            }
            self.userService.deleteOne(username)
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:
            return{
                    "status": True,
                    "message": f"El usuario {username} ha sido ELIMINADO"
            }

        
        
