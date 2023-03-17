import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as messagebox
from recetario import *

class VentanaPrincipal(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.master.title("Ventana Principal")
        self.master.geometry("1500x700")
        self.master.configure(bg="#73C0C8") # Configura el color de fondo en celeste

        #instanciamos la clase controlador de Receta
        self.recetas_service = Recetario()

        self.create_menu_bar()
        self.create_menu_frame()
        self.create_main_frame()

        
    def del_receta(self, key):
        # método que elimina una receta
        resultado = self.recetas_service.delOne(key)
        if resultado["status"] == True:
            messagebox.showinfo("Éxito", resultado["message"])
        else:
            messagebox.showerror("Error", resultado["message"])    

    def create_menu_bar(self):
        self.menu_bar = tk.Menu(self.master, bg="#73C0C8")
        self.master.config(menu=self.menu_bar)

        self.archivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Abrir")
        self.archivo_menu.add_command(label="Guardar")
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.master.quit)

        self.editar_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.editar_menu)
        self.editar_menu.add_command(label="Cortar")
        self.editar_menu.add_command(label="Copiar")
        self.editar_menu.add_command(label="Pegar")

    def create_menu_frame(self):
        self.menu_frame = ttk.Frame(self.master)
        self.menu_frame.pack(side="left", fill="y") # Cambia la orientación del menú y lo coloca a la izquierda
        self.menu_frame.configure(style="Menu.TFrame")

        self.button1 = ttk.Button(self.menu_frame, text="Crear Receta")
        self.button1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self.menu_frame, text="Listar Recetas")
        self.button2.pack(pady=10, padx=10)

    def create_main_frame(self):
     self.main_frame = ttk.Frame(self.master)
     self.main_frame.pack(side="right", fill="both", expand=True)
     self.main_frame.configure(style="Main.TFrame")

     #solicitando al servicio la receta del dia
     res = self.recetas_service.recetaDelDia()
     if(res['status']==True):
         n_deldia = res['r_del_dia']
         peticion = self.recetas_service.getOne(n_deldia)         
         if(peticion['status']==True):
            r_deldia = peticion['receta']
         else:
            r_deldia = {}
     else:
         n_deldia = ""
 
     # Crear el widget Panedwindow para dividir el frame principal en dos
     self.panedwindow = ttk.Panedwindow(self.main_frame, orient="horizontal")
     self.panedwindow.pack(fill="both", expand=True)
 
     # Crear el frame para la lista
     self.lista_frame = ttk.Frame(self.panedwindow)
     self.lista_frame.configure(style="Lista.TFrame")
     self.panedwindow.add(self.lista_frame)
 
     # Agregar los widgets para mostrar la lista
     
     
     datos_r = self.recetas_service.getAll()
     
     if(datos_r['status'] == True):
        datos = datos_r['recetas'].keys()
        datos = list(datos)
        datos.sort()
     else:
        datos = []
     
     self.lista_label = ttk.Label(self.lista_frame, text="Lista de objetos")
     self.lista_label.pack(pady=10, padx=10)
 
     self.lista = tk.Listbox(self.lista_frame, height=30)
     self.lista.pack(fill="both", expand=True)
 
     # Crear el estilo para los botones
     estilo_botones = ttk.Style()
     estilo_botones.configure("Botones.TButton", font=("Arial", 12), borderwidth=3)
 
     for dato in datos:
         # Crear un frame para cada fila de la lista
         fila_frame = ttk.Frame(self.lista, borderwidth=2, relief="groove")
         fila_frame.pack(fill="x", padx=5, pady=5)
 
         # Agregar el texto de cada elemento
         fila_texto = ttk.Label(fila_frame, text=dato, font=("Arial", 14))
         fila_texto.pack(side="left", padx=10, pady=10)
 
         # Agregar el botón de editar
        #  fila_boton_editar = ttk.Button(fila_frame, text="Editar", style="Botones.TButton",command=lambda: self.recetas_service.delOne(dato))
         fila_boton_editar = ttk.Button(fila_frame, text="Editar", style="Botones.TButton")
         fila_boton_editar.pack(side="left", padx=10, pady=10)
 
         # Agregar el botón de eliminar
         fila_boton_eliminar = ttk.Button(fila_frame, text="Eliminar", style="Botones.TButton",command=lambda valor = dato: self.del_receta(valor))         
         fila_boton_eliminar.pack(side="left", padx=10, pady=10)
 
     # Crear el frame para el objeto
     self.objeto_frame = ttk.Frame(self.panedwindow)
     self.objeto_frame.configure(style="Objeto.TFrame")
     self.panedwindow.add(self.objeto_frame)
 
     # Agregar los widgets para mostrar el objeto
     self.label_titulo = ttk.Label(self.objeto_frame, text=n_deldia)
     self.label_titulo.pack(pady=10)
 
    #  self.label_descripcion = ttk.Label(self.objeto_frame, text="Descripción del objeto")
    #  self.label_descripcion.pack(pady=10)
     self.fields_frame = ttk.LabelFrame(self.objeto_frame, text="Contenido", )
     self.fields_frame.pack(pady=10)     
     obj = r_deldia[n_deldia]
    #  for key, value in obj.items():
    #         print(key)
    #         print(value)

     max_label_width = 0  # variable para almacenar el ancho del label más ancho

     for key, value in obj.items():
          # crear y empaquetar label de clave
          field_label = ttk.Label(self.fields_frame, text=key+":", anchor="e", justify="right")
          field_label.pack(side="top", padx=10, pady=5)
          
          # obtener el ancho requerido del label de clave
          label_width = field_label.winfo_reqwidth()
          if label_width > max_label_width:
              max_label_width = label_width
          
          # crear y empaquetar label de valor
          value_label = ttk.Label(self.fields_frame, text=value, anchor="w", justify="left")
          value_label.pack(side="top", padx=10, pady=5)

     # establecer el ancho del LabelFrame de acuerdo con el ancho requerido del label más ancho
     self.fields_frame.configure(width=max_label_width+20)  # sumar un padding de 20 para dar espacio adicional
 
     # Establecer el estilo de los frames
     s = ttk.Style()
     s.configure("Main.TFrame", background="#4189A1")
     s.configure("Lista.TFrame", background="#E6E6E6")
     s.configure("Objeto.TFrame", background="#D2D9E8")
     #s.configure("Objeto.frame_obj", background="#D2D9E8")


if __name__ == "__main__":
    #root = tk.Tk()
    root = ThemedTk(theme="ubuntu")
    app = VentanaPrincipal(master=root)
    app.mainloop()
