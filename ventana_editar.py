import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from recetario import *
from tkinter import font

""" 
Importamos tkinter para poder crear la ventana
Tambien importamos todos los metodos y clases de recetario que nos permite utlizarlas en lo que necesitemos
"""

class VentanaEditar(ttk.Frame):
    """
    En esta clase manejamos el frontend de una ventana de edicion
    """

    def __init__(self, nombre_receta = "guiso", master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Editar Receta")
        self.master.configure(bg="#F5F5F5") # Configura el color de fondo en celeste
        

        """instanciamos la clase controlador de Receta"""
        self.recetas_service = Recetario()

        self.nombre_receta = nombre_receta

        """tomamos la data utilizando el metodo correspondiente"""
        res = self.recetas_service.getOne(nombre_receta)
        if(res['status']== True):
            self.receta = res['receta'][nombre_receta]          
            self.createView()
        else:
            self.receta = {}
            
        
        print(self.receta)

    def actualizar_diccionario(self, *args):
        self.receta["duracion"] = self.duracion.get()
        self.receta["coccion"] = self.coccion.get()
        self.receta["fecha"] = self.fecha.get()

        """Actualizar la lista de ingredientes en el diccionario"""
        nuevos_ingredientes = []
        for i in range(self.ingredientes_listbox.size()):
            item = self.ingredientes_listbox.get(i)
            ingrediente = {
                'nombre': self.nombre_ingredientes_vars[i].get(),
                'cantidad': item['cantidad'],
                'unidad_de_medida': item['unidad_de_medida']
            }
            nuevos_ingredientes.append(ingrediente)
        self.receta['ingredientes'] = nuevos_ingredientes

    def actualizar_ingredientes(self, *args):
        ingredientes = self.ingredientes_listbox.get(0, tk.END) # Obtenemos la lista de ingredientes
        self.receta["ingredientes"] = list(ingredientes)

    def guardar_receta(self):
        self.receta["duracion"] = self.duracion.get()    
        self.receta["coccion"] = self.coccion.get()
        self.receta["fecha"] = self.fecha.get()
        self.receta["ingredientes"] = self.ingredientes.get()
        print(self.receta)
    
    def createView(self):
        fuente_mediana = font.Font(family="Arial", size=20, weight="bold")

        """voy a enlazar todos los campos del dictionary self.receta a variables de control tkinter"""
        duracion_var = tk.StringVar()
        duracion_var.set(self.receta["duracion"])
        duracion_var.trace("w", self.actualizar_diccionario)

        coccion_var = tk.StringVar()
        coccion_var.set(self.receta["coccion"])
        coccion_var.trace("w", self.actualizar_diccionario)

        fecha_var = tk.StringVar()
        fecha_var.set(self.receta["fecha"])
        fecha_var.trace("w", self.actualizar_diccionario)

        ingredientes_var = tk.StringVar()
        ingredientes_var.set(self.receta["ingredientes"])
        ingredientes_var.trace("w", self.actualizar_diccionario)

        """Creacion de los widgets con los entry correspondientes"""
        valor_name = tk.StringVar(value=self.nombre_receta)
        tk.Label(self, text=f"Nombre de Receta: ").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_receta = tk.Entry(self, textvariable=valor_name, font=fuente_mediana)
        self.nombre_receta.configure(state='disabled')
        self.nombre_receta.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Duración de preparación: ").grid(row=1, column=0,padx=10, pady=10)
        self.duracion = tk.Entry(self, textvariable=duracion_var)
        self.duracion.grid(row=1, column=1)

        tk.Label(self, text="Tiempo de cocción: ").grid(row=2, column=0, padx=10, pady=10)
        self.coccion = tk.Entry(self, textvariable=coccion_var)
        self.coccion.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Fecha: ").grid(row=3, column=0, padx=10, pady=10)
        self.fecha = tk.Entry(self, textvariable=fecha_var)
        self.fecha.grid(row=3, column=1, padx=10, pady=10)

        self.nombre_ingredientes_vars = []
        self.ingredientes_listbox = tk.Listbox(self, height=10, width=50)
        self.ingredientes_listbox.grid(row=4, column=1)
        for ingrediente in self.receta['ingredientes']:
            nombre_var = tk.StringVar()
            nombre_var.set(ingrediente['nombre'])
            self.nombre_ingredientes_vars.append(nombre_var)
            self.ingredientes_listbox.insert(tk.END, ingrediente)

        ttk.Button(self, text="Guardar", command=self.guardar_receta).grid(row=10, column=1)

        self.grid()  
    

 
    
    
if __name__ == "__main__":
    #root = tk.Tk()
    root = ThemedTk(theme="ubuntu")
    window = VentanaEditar(master=root)    
    window.mainloop()
    
    
