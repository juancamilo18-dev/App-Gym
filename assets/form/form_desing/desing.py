import flet as ft
from assets.bd.comandos import BaseDatos
import sqlite3
from assets.form.form_desing.logia_desing_new_rutina import LogicaCrearRutina
# from base_datos.comandos import BaseDatos

class DiseñoApp:
    def __init__(self, pagina = None):
        self.pagina = pagina

    def diseño(self):
        self.pagina.clean()

        # Contendor 
        c = LogicaCrearRutina(self.pagina)
        
        # Tamaño
        self.pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.pagina.window_width = 800
        self.pagina.window_height = 600 

        # Botones
        self.lunes = ft.ElevatedButton("Lunes", width=120)
        self.martes = ft.ElevatedButton("Martes", width=120)
        self.miercoles = ft.ElevatedButton("Miercoles", width=120)
        self.jueves = ft.ElevatedButton("Jueves", width=120)
        self.viernes = ft.ElevatedButton("Viernes", width=120)
        self.sabado = ft.ElevatedButton("Sabado", width=120)
        self.salir = ft.ElevatedButton("Salir", width=150)
        self.nueva_rutina = ft.ElevatedButton("Nueva Rutina", width=150)

        c.contenedor_lateral.content = ft.Column(controls=[ft.Row(controls=[self.nueva_rutina], alignment=ft.MainAxisAlignment.CENTER),
                                                           ft.Row(controls=[self.salir], alignment=ft.MainAxisAlignment.CENTER)])

        c.contendor_derecho.content = ft.Column(controls=[ft.Row(controls=[self.lunes, self.martes, self.miercoles], alignment=ft.MainAxisAlignment.CENTER),
                                        ft.Row(controls=[self.jueves, self.viernes, self.sabado], alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER)

        contenedor = ft.ResponsiveRow(controls=[c.contenedor_lateral, c.contendor_derecho], expand=True)

        self.pagina.add(contenedor)
                        

        
    def entradasSeries(self, con_ejercicios):
        series = ft.Dropdown(label="Series",
                             width=90)               
        
        ejercicios = ft.Dropdown(label="Ejercicios",
                                 width=220)
        
        ejercicios.options = []

        
        for i in con_ejercicios:
            ejercicios.options.append(ft.dropdown.Option(i[1]))

        return series, ejercicios
    
    def estructura(self):
        pass
        
    def lunesRutina(self):
        pass
        
    def martesRutina(self):
        pass