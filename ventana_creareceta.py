import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from recetario import *
""" 
Importamos tkinter para poder crear la ventana
Tambien importamos todos los metodos y clases de recetario que nos permite utlizarlas en lo que necesitemos
"""

class VentanaCreareceta(ttk.Frame):
    """
    En esta clase creamos la ventana que permite crear una nueva receta
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Crear Receta")
        self.master.configure(bg="#73C0C8") # Configura el color de fondo en celeste
        self.ingredientes= []

        #instanciamos la clase controlador de Receta
        self.recetas_service = Recetario()

        # Creacion de los widgets con los entry correspondientes
        tk.Label(self, text="Nombre de la nueva receta: ").grid(row=0, column=0)
        self.nombre_receta = tk.Entry(self)
        self.nombre_receta.grid(row=0, column=1)

        tk.Label(self, text="Ingredientes").grid(row=1, column=0)
        

        tk.Label(self, text="Nombre ingr:").grid(row=1, column=1)
        self.nomb_ingr = tk.Entry(self)
        self.nomb_ingr.grid(row=1, column=2)

        tk.Label(self, text="Cantidad:").grid(row=2, column=1)
        self.cantidad = tk.Entry(self)
        self.cantidad.grid(row=2, column=2)

        tk.Label(self, text="Unidad de medida:").grid(row=3, column=1)
        self.un_medida = tk.Entry(self)
        self.un_medida.grid(row=3, column=2)

        tk.Label(self, text="Preparación: ").grid(row=4, column=0)
        self.preparacion = tk.Entry(self)
        self.preparacion.grid(row=4, column=1)

        tk.Label(self, text="Imagenes: ").grid(row=5, column=0)
        self.imagenes = tk.Entry(self)
        self.imagenes.grid(row=5, column=1)

        tk.Label(self, text="Duración de preparación: ").grid(row=6, column=0)
        self.duracion = tk.Entry(self)
        self.duracion.grid(row=6, column=1)

        tk.Label(self, text="Tiempo de cocción: ").grid(row=7, column=0)
        self.coccion = tk.Entry(self)
        self.coccion.grid(row=7, column=1)

        tk.Label(self, text="Fecha: ").grid(row=8, column=0)
        self.fecha = tk.Entry(self)
        self.fecha.grid(row=8, column=1)

        tk.Label(self, text="Etiquetas: ").grid(row=9, column=0)
        self.etiqueta = tk.Entry(self)
        self.etiqueta.grid(row=9, column=1)

        # Creamos un Checkbox para indicar si la receta es favorita
        self.es_favorita = tk.IntVar() # Variable de control para el Checkbox
        tk.Checkbutton(self, text="Si", variable=self.es_favorita).grid(row=10, column=1)
        tk.Label(self, text="Favorita (tildar si es favorita)").grid(row=10, column=0)

        #Creamos los dos botones necesarios para poder invocar a las funciones necesarias
        tk.Button(self, text="Agregar receta", command=self.agregar_receta).grid(row=11, column=2)

        tk.Button(self, text="Agregar ingrediente", command=self.agregar_ingrediente).grid(row=1, column=3)

        self.grid()

    def agregar_receta(self):
        """
          Funcion que permite consumir los datos de todos los campos entrados en los widgets de la ventana
        """
        nombre=self.nombre_receta.get()
        preparacion= self.preparacion.get()
        imagenes= [self.imagenes.get()]
        duracion= self.duracion.get()
        coccion= self.coccion.get()
        fecha= self.fecha.get()
        etiquetas= [self.etiqueta.get()]
        es_favorita= self.es_favorita.get() == 1

        receta= {"ingredietes": self.ingredientes, "preparacion": preparacion, "imagenes": imagenes, "duracion": duracion,
                 "coccion": coccion, "fecha": fecha, "etiquetas": etiquetas, "es_favorita": es_favorita}

        res= self.recetas_service.addOne(nombre,receta) # LLamamos al metodo addone del recetario

        self.nombre_receta.delete(0, tk.END)
        self.preparacion.delete(0, tk.END)
        self.imagenes.delete(0, tk.END)
        self.duracion.delete(0, tk.END)
        self.coccion.delete(0, tk.END)
        self.fecha.delete(0, tk.END)
        self.etiqueta.delete(0, tk.END)
        self.es_favorita.set(0)

        self.nombre_receta.focus() # pone el cursor en el primer widget de la ventana

    def agregar_ingrediente(self):
        """ 
        Funcion que permite agregar más de un ingrediente en la receta, guardando los datos de los campos 
        """
        nombre = self.nomb_ingr.get()
        cantidad = self.cantidad.get()
        unidad = self.un_medida.get()

        self.ingredientes.append({"nombre": nombre, "cantidad": cantidad, "unidad de medida": unidad})
        # Se agrega un diccionario nuevo con la data del ingrediente

        #Para limpiar los Entry correspondientes
        self.nomb_ingr.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.un_medida.delete(0, tk.END)

        self.nomb_ingr.focus() # pone el cursor en el primer widget de la sub ventana ingredientes


    
if __name__ == "__main__":
    #root = tk.Tk()
    root = ThemedTk(theme="ubuntu")
    vent=VentanaCreareceta(master=root)
    vent.mainloop()
    
# tengo los siguientes problemas:
# falta que al terminar de un cartel de cargado exitosamente o de error