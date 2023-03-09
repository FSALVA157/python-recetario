import json
class FileManager:
    base_url = 'data/'        

    def __init__(self, archivo: str):
        self.__archivo = archivo        
    

    def create(self, info:dict):
        try:
            with open(FileManager.base_url + self.__archivo, "w") as write_file:
                json.dump(info, write_file, indent=4)
                write_file.close()
        except IOError as e:
            raise Exception(f"Error de Entrada/Salida al crear el archivo: {self.__archivo}, error: {e}")
        except Exception as e:
            raise Exception(f"Error Inesperado al crear el archivo: {self.__archivo}, error: {e}")

    def getAll(self):
        try: 
            with open(FileManager.base_url+self.__archivo, "r") as read_file:
                data = json.load(read_file) 
            # return data
        except FileNotFoundError as e:
            raise Exception(f"No se encontro el archivo: {self.__archivo}")
        except ValueError as e:
            raise Exception(f"Error al leer el archivo: {self.__archivo}, error: {e}")
        except Exception as e:
            raise Exception(f"Error Inesperado al leer el archivo: {self.__archivo}, error: {e}")
        else:
            return data
        
    def getOne(self, key: str) -> dict:
        try:            
            data = self.getAll()
            if(key not in data):
                return {
                    "status": False,
                    "message": "La clave consultada no existe en los datos"
                }                
            obj = data[key]
            # return obj
        except ValueError as e:
            raise Exception(f"Error al leer el archivo: {self.__archivo}, error: {e}")
        except Exception as e:
            raise Exception(f"Error Inesperado al leer el archivo: {self.__archivo}, error: {e}")
        else:
            return {
                "status": True,
                "data": {
                    key: obj
                }
            }

    
    def addOne(self, clave: str, valor) -> str: 
        try:
            data = self.getAll()
            if(clave in  data):
                return {
                    "status": False,
                    "message": "el objeto ya existe"
                }
            else:
                data[clave] = valor
                with open(FileManager.base_url+self.__archivo,"w") as writable_file:
                    json.dump(data, writable_file)                
        except FileNotFoundError as e:
            raise Exception(f"No se encontro el archivo: {self.__archivo}")
        except PermissionError as e:
            raise Exception(f"El archivo {self.__archivo} no tiene permisos de escritura.")
        except OSError as e:
            raise Exception(f"Error al abrir o cerrar el archivo {self.__archivo}. Error: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"El archivo {self.__archivo} no se pudo decodificar correctamente. Error: {e}")
        except ValueError as e:
            raise Exception(f"Se intentó agregar un valor no válido al archivo JSON {self.__archivo}. Error: {e}")
        except Exception as e:
            raise Exception(f"Error Inesperado al escribir el archivo: {self.__archivo}, error: {e}")
        else:
            return {
                "status": True,
                "message": "Objeto agregado exitosamente"
            }
    
    def deleteOne(self, llave: str)->str:
        try:
            info = self.getAll()
            if(llave in info):
                del info[llave]
                self.create(info)                
            else:
                raise Exception(f"El objeto con clave {llave} no existe en los datos")
        except IOError as e:
            raise Exception(f"Error al intentar leer o escribir el archivo: {self.__archivo}, error: {e}") 
        except Exception as e:
            raise Exception(f"Error Inesperado al eliminar dato en el archivo: {self.__archivo}, error: {e}")
        else:
            return {
                    "status": True,
                    "message": f"El objeto con clave {llave} ha sido eliminado exitosamente"
                }            
        
    def updateOne(self, key, value) -> str:
        try:
            data = self.getAll()
            if(key not in data):
                raise Exception(f"El objeto con clave {key} no existe en los datos")
            else:
                data[key]=value
                self.create(data)                
        except IOError as e:
            raise Exception(f"Error al intentar leer o escribir el archivo: {self.__archivo}, error: {e}") 
        except Exception as e:
            raise Exception(f"Error Inesperado al eliminar dato en el archivo: {self.__archivo}, error: {e}")
        else:
            return f"El objeto con clave {key} ha sido elminado con Exito!"
            
        
