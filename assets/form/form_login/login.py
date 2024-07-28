import flet as ft
from assets.form.form_desing.desing_logica import LogicaDesing
from assets.form.form_desing.logia_desing_new_rutina import LogicaCrearRutina 
import os, sys

class DiseñoLogin:
    def __init__(self):
        ft.app(target=self.construir)

    def construir(self, page = ft.Page):
        page.clean()
        page.title = "GYM"
        page.window_width = 500
        page.window_min_width = 500
        page.window_height = 400
        page.window_min_height = 380

        self.d = LogicaDesing(page)

        def inicio(e = None):
            self.d.diseño()
            self.d.salir.on_click = salir
            self.d.nueva_rutina.on_click = makeRutina
            self.d.lunes.on_click = regresarLunes
            self.d.martes.on_click = regresarMartes
            self.d.miercoles.on_click = regresarMiercoles
            self.d.jueves.on_click = regresarJueves
            self.d.viernes.on_click = regresarViernes
            self.d.sabado.on_click = regresarSabado

            
        def ingresar(e):
            if self.usuario.value == "cbum" and self.contraseña.value == "cbum":
                inicio()

        def makeRutina(self):
            c = LogicaCrearRutina(page)
            page.clean()
            c.diseño()
            page.update()
            c.regresar.on_click = inicio

        def salir(e):
            self.construir(page)
            page.update()

        def regresarLunes(e):
            self.d.lunesRutina()
            try:
                self.d.regresar.on_click = inicio
            except:
                pass
        def regresarMartes(e):
            self.d.martesRutina()
            try:
                self.d.regresar.on_click = inicio
            except:
                pass

        def regresarMiercoles(e):
            self.d.miercolesRutina()
            try:
                self.d.regresar.on_click = inicio
            except:
                pass

        def regresarJueves(e):
            self.d.juevesRutina()
            try:
                self.d.regresar.on_click = inicio
            except:
                pass
        
        def regresarViernes(e):
            self.d.viernesRutina()
            try:
                self.d.regresar.on_click = inicio
            except:
                pass
        
        def regresarSabado(e):
            self.d.sabadoRutina()
            try:
                self.d.regresar.on_click = inicio
            except:
                pass

        def resolver_ruta(ruta_relativa):
            ruta_base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath('assets')))
            return os.path.join(ruta_base, ruta_relativa)
        
        ruta = resolver_ruta("assets")
        nruta = os.path.join(ruta, "casco.png")


        login = ft.Text("Inicio de sesión", size=30, weight="bold")

        imagen_login = ft.Image(src=nruta, width=100, height=90)

        self.usuario = ft.TextField(label="Usuario", hint_text="Usuario", value="cbum", text_size=17)
        self.contraseña = ft.TextField(label="Contraseña", hint_text="Contraseña", value="cbum", password=True, text_size=17, max_length=8)

        boton_ingresar = ft.TextButton(text="Ingresar", on_click=ingresar)

        page.add(ft.Row(controls=[imagen_login], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[login], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(controls=[self.usuario, self.contraseña]),
                    ft.Row(controls=[boton_ingresar], alignment=ft.MainAxisAlignment.CENTER))