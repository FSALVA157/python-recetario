import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as messagebox
from recetario import *
from ventana_creareceta import *
from ventana_mostrar import *
from ventana_editar import *
from PIL import Image, ImageTk

"""
Importamos las librerias necesarias y las clases que utilizamos
"""

class VentanaPrincipal(ttk.Frame):

    """
    En esta clase creamos la ventana principal que permite mostar la lista de recetas y los botones necesarios para llamar a los diferentes metodos
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.master.title("Ventana Principal")
        self.master.geometry("1500x700")
        self.master.configure(bg="#F5F5F5") 

        """
        instanciamos la clase controlador de Receta
        """
        self.recetas_service = Recetario()

        self.create_menu_bar()
        self.create_menu_frame()
        self.create_main_frame()

    def abrir_alta_receta(self):
         """
        método que abre la ventana para crear una nueva receta
        """
         root = ThemedTk(theme="ubuntu")
         vent=VentanaCreareceta(master=root)
         vent.mainloop()
        
    def abrir_mostrar_receta(self, key):
        """
        método que abre la ventana para mostrar una receta
        """
        root = ThemedTk(theme="ubuntu")
        vent=VentanaMostrar(key,master=root)
        vent.mainloop()

    def abrir_editar_receta(self, key):
        """
        método que abre la ventana para editar una receta
        """
        root = ThemedTk(theme="ubuntu")
        vent=VentanaEditar(key,master=root)
        vent.mainloop()


    def del_receta(self, key):
        """
        método que elimina una receta
        """

        resultado = self.recetas_service.delOne(key)
        if resultado["status"] == True:
            messagebox.showinfo("Éxito", resultado["message"])
        else:
            messagebox.showerror("Error", resultado["message"])    


        """
        Creamos todos los menú y label necesarios
        """
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
        self.menu_frame.pack(side="left", fill="y") 
        self.menu_frame.configure(style="Menu.TFrame")

        self.button1 = ttk.Button(self.menu_frame, text="Crear Receta", command=self.abrir_alta_receta)
        self.button1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self.menu_frame, text="Listar Recetas")
        self.button2.pack(pady=10, padx=10)
        
    def create_main_frame(self):
     self.main_frame = ttk.Frame(self.master)
     self.main_frame.pack(side="right", fill="both", expand=True)
     self.main_frame.configure(style="Main.TFrame")

     """
     Solicitando al servicio la receta del dia
     """
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
 
     """
     Creamos el widget Panedwindow para dividir el frame principal en dos
     """
     self.panedwindow = ttk.Panedwindow(self.main_frame, orient="horizontal")
     self.panedwindow.pack(fill="both", expand=True)
 
     """
     Creampos el frame para la lista
     """
     self.lista_frame = ttk.Frame(self.panedwindow)
     self.lista_frame.configure(style="Lista.TFrame")
     self.panedwindow.add(self.lista_frame)
 
     """
     Agregar los widgets para mostrar la lista.
     Tambien creamos los botones con los estilos queremos y un frame para cada fila
     """
     
     
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
 
     
     estilo_botones = ttk.Style()
     estilo_botones.configure("Botones.TButton", font=("Arial", 12), borderwidth=3)
 
     for dato in datos:
         fila_frame = ttk.Frame(self.lista, borderwidth=2, relief="groove")
         fila_frame.pack(fill="x", padx=5, pady=5)
 
         fila_texto = ttk.Label(fila_frame, text=dato, font=("Arial", 14))
         fila_texto.pack(side="left", padx=10, pady=10)
 
         fila_boton_editar = ttk.Button(fila_frame, text="Editar", style="Botones.TButton",command=lambda valor = dato: self.abrir_editar_receta(valor))
         fila_boton_editar.pack(side="left", padx=10, pady=10)

         fila_boton_mostrar = ttk.Button(fila_frame, text="Mostrar", style="Botones.TButton",command=lambda valor = dato: self.abrir_mostrar_receta(valor))         
         fila_boton_mostrar.pack(side="left", padx=10, pady=10)
 
         fila_boton_eliminar = ttk.Button(fila_frame, text="Eliminar", style="Botones.TButton",command=lambda valor = dato: self.del_receta(valor))         
         fila_boton_eliminar.pack(side="left", padx=10, pady=10)
 
     """
     Creamos un frame para el objeto
     """
     self.objeto_frame = ttk.Frame(self.panedwindow)
     self.objeto_frame.configure(style="Objeto.TFrame")
     self.panedwindow.add(self.objeto_frame)

     """
     Antes de empezar tomo los datos de receta del dia para ver que imagen voy a mostrar
     """
     obj = r_deldia[n_deldia]

     img_name = obj["imagenes"][0]

     self.label_img = tk.Label(self.objeto_frame)
     self.label_img.pack(side='left', padx=10, pady=10)

     imagen = Image.open(f"img/{img_name}")      
     imagen = imagen.resize((400, 400), Image.ANTIALIAS)
     imagen_tk = ImageTk.PhotoImage(imagen)

     self.label_img.configure(image=imagen_tk)
     self.label_img.image = imagen_tk
 
     self.label_titulo = ttk.Label(self.objeto_frame, text=n_deldia)
     self.label_titulo.pack(pady=10)
 

    
     self.fields_frame = ttk.LabelFrame(self.objeto_frame, text="Receta del Dia", )
     self.fields_frame.pack(pady=10)     
    

     max_label_width = 0  
     field_font = ('TkDefaultFont', 14)
     row_count = 0  
     for key, value in obj.items():        
        field_label = ttk.Label(self.fields_frame, text=key+":", anchor="e", justify="right", font=field_font)
        field_label.grid(column=0, row=row_count, padx=(10, 5), pady=5, sticky='e')
        
        label_width = field_label.winfo_reqwidth()
        if label_width > max_label_width:
            max_label_width = label_width
        
        if isinstance(value, list):
            value_listbox = tk.Listbox(self.fields_frame, height=len(value))
            for item in value:
                value_listbox.insert(tk.END, item)
            value_listbox.grid(column=1, row=row_count, padx=(0, 10), pady=5, sticky='w')
        else:
            value_label = ttk.Label(self.fields_frame, text=value, anchor="w", justify="left", font=field_font)
            value_label.grid(column=1, row=row_count, padx=(0, 10), pady=5, sticky='w')
        
        row_count += 1
    
     self.fields_frame.configure(width=max_label_width+20)  
 
     s = ttk.Style()
     s.configure("Main.TFrame", background="#4189A1")
     s.configure("Lista.TFrame", background="#E6E6E6")


if __name__ == "__main__":
    root = ThemedTk(theme="ubuntu")
    app = VentanaPrincipal(master=root)
    app.mainloop()