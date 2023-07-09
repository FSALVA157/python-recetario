import os
import json
import mysql.connector


class IngredienteService:
    

    def __init__(self):
        current_dir = os.getcwd()
        config_path = os.path.join(current_dir, 'services/config_data.json')
        with open(config_path ,'r') as config_file:
            data = json.load(config_file)
            self.conn = mysql.connector.connect(**data)           
            self.cur = self.conn.cursor()

    def createOne(self, ingrediente):
        try:
            
            query = """INSERT INTO ingrediente (nombre_ingrediente, unidad_medida)
                        VALUES (%s, %s)"""
            self.cur.execute(query, (ingrediente['nombre_ingrediente'],ingrediente['unidad_medida']))            
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
                "message": f"El ingrediente {ingrediente['nombre_ingrediente']} ha sido Creado Exitosamente"
            }
    
    def getAll(self):
        try:
            query = """SELECT * FROM ingrediente"""
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
                "ingredientes": data
            }
    
    def getOne(self, id):
        try:
            query = """SELECT * FROM ingrediente WHERE id_ingrediente = %s"""
            self.cur.execute(query, (id,))            
            data = self.cur.fetchall()
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }        
        finally:
            self.conn.close()
        return {
                "status": True,
                "ingrediente": data
            }
    
    def deleteOne(self, id):
        try:
            query = """DELETE FROM ingrediente WHERE id_ingrediente = %s"""
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
            query = """UPDATE ingrediente SET nombre_ingrediente=%s, unidad_medida=%s WHERE id_ingrediente = %s"""
            new_data = (data['nombre_ingrediente'], data['unidad_medida'], id)
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
    ingrediente_s =  IngredienteService()            
    res =  ingrediente_s.createOne({"nombre_ingrediente": "cebolla", "unidad_medida": "gramos"})
    #res = ingrediente_s.getAll()
    #res = ingrediente_s.getOne(2)
    #res = ingrediente_s.deleteOne(3)
    #res = ingrediente_s.updateOne(16,{"nombre_ingrediente": "caldo de verduras", "unidad_medida": "cubito"})
    print(res)

        