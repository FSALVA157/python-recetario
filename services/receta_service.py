import os
import json
import mysql.connector


class RecetaService:
    

    def __init__(self):
        current_dir = os.getcwd()
        config_path = os.path.join(current_dir, 'services/config_data.json')
        with open(config_path ,'r') as config_file:
            data = json.load(config_file)
            self.conn = mysql.connector.connect(**data)           
            self.cur = self.conn.cursor()

    def createOne(self, nombre, receta):
        try:
            new_receta = {**receta, "nombre": nombre}            
            query = """INSERT INTO receta (nombre_receta, preparacion, tiempo_preparacion, tiempo_coccion, imagen, etiquetas, es_favorita)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.cur.execute(query, (new_receta['nombre'],new_receta['preparacion'], new_receta['duracion'], new_receta['coccion'],
                                     new_receta['etiquetas'], new_receta['imagen'], new_receta['favorita']))            
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:            
            self.conn.commit()
        finally:
            self.conn.close()
        return {
                "status": True,
                "message": f"la receta {new_receta['nombre']} ha sido Creada"
            }
    
    def getAll(self):
        try:
            query = """SELECT * FROM receta"""
            self.cur.execute(query)            
            data = self.cur.fetchall()
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        # else:            
        #     self.conn.commit()
        finally:
            self.conn.close()
        return {
                "status": True,
                "recetas": data
            }
    
    def getOne(self, id):
        try:
            query = """SELECT * FROM receta WHERE id_receta = %s"""
            self.cur.execute(query, (id,))            
            data = self.cur.fetchall()
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        # else:            
        #     self.conn.commit()
        finally:
            self.conn.close()
        return {
                "status": True,
                "receta": data
            }
    
    def deleteOne(self, id):
        try:
            query = """DELETE FROM receta WHERE id_receta = %s"""
            self.cur.execute(query, (id,))                        
            num_rows_affected = self.cur.rowcount

            if num_rows_affected == 0:
                respuesta = {
                "status": False,
                "message": "No se encontró el registro con el ID proporcionado."
            }                
            else:                
                respuesta = {
                "status": True,
                "message": "El registro se eliminó exitosamente."
            }
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:            
            self.conn.commit()
        finally:
            self.conn.close()
        return respuesta
    
    def updateOne(self, id, data):
        try:
            query = """UPDATE receta SET nombre_receta=%s, preparacion=%s, tiempo_preparacion=%s, tiempo_coccion=%s, etiquetas=%s, imagen=%s, es_favorita=%s WHERE id_receta = %s"""
            new_data = (data['nombre_receta'], data['preparacion'], data['duracion'], data['coccion'], data['etiquetas'], data['imagen'],data['favorita'], id)
            self.cur.execute(query, new_data)                        
            num_rows_affected = self.cur.rowcount

            if num_rows_affected == 0:
                 respuesta = {
                     "status": False,
                     "message": "No se encontró el registro con el ID proporcionado."
                 }                
            else:
                 respuesta = {
                     "status": True,
                     "message": "El registro ha sido actualizado exitosamente."
                 }                        
            
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }
        else:            
            self.conn.commit()
        finally:
            self.conn.close()
        return respuesta
    


if __name__ == "__main__":
    receta_s =  RecetaService()            
    # res =  receta_s.createOne("guiso", {"preparacion": "{'agregar carne trozada', 'agregar papa trozada', 'hervir agua'}", "duracion": "1 hora", "coccion": "45 minutos", "etiquetas": "{'guiso', 'carne', 'caliente'}","imagen": "imagen-2", "favorita": 0})
    #res = receta_s.getAll()
    #res = receta_s.getOne(2)
    #res = receta_s.deleteOne(3)
    res = receta_s.updateOne(1,{"nombre_receta": "sopa crema","preparacion": "{'agregar medio choclo', 'carne trozada', 'hervir agua'}", "duracion": "40 minutos", "coccion": "30 minutos", "etiquetas": "{'sopa', 'carne', 'caliente'}", "imagen": "imagen-1","favorita": 1})
    print(res)

        