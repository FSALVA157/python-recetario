import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from recetario import *
""" 
Importamos tkinter para poder crear la ventana
Tambien importamos todos los metodos y clases de recetario que nos permite utlizarlas en lo que necesitemos
"""

class VentanaMostrar(ttk.Frame):
    """
    En esta clase creamos la ventana que permite mostar una receta elegida
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Mostrar Receta")
        self.master.configure(bg="#73C0C8") # Configura el color de fondo en celeste

        #instanciamos la clase controlador de Receta
        self.recetas_service = Recetario()

    def mostrar(self):
        
        clave = self.buscador
        res= self.recetas_service.getOne(key)