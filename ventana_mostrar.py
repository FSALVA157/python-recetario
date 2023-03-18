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
        self.master.geometry("800x500")
        self.master.configure(bg="#73C0C8") # Configura el color de fondo en celeste

        #instanciamos la clase controlador de Receta
        self.recetas_service = Recetario()

        tk.Label(self, text="Nombre de la receta a mostrar: ").grid(row=0, column=0)
        self.nombre_receta = tk.Entry(self)
        self.nombre_receta.grid(row=0, column=1)

        tk.Button(self, text="Buscar", command=self.mostrar).grid(row=2, column=2)



        self.grid()

    def mostrar(self):
        
        nombre = self.buscador
        res= self.recetas_service.getOne(nombre)
        


if __name__ == "__main__":
    #root = tk.Tk()
    root = ThemedTk(theme="ubuntu")
    vent=VentanaMostrar(master=root)
    vent.mainloop()
    