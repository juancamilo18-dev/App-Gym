from assets.bd.comandos import BaseDatos
from assets.form.form_desing.desing_new_rutina import CrearRutina
import flet as ft

class LogicaCrearRutina(CrearRutina):

    def actualizar(self, e):
        self.auxiliar = int(self.n_series.value)
        self.serie.options = []

        for i in range(int(self.n_series.value)):
            self.serie.options.append(ft.dropdown.Option(i+1))
        
        self.pagina.update()

    
    def ingresar(self, e):
        dia = self.day_weeks.value
        ejercicio = self.ejercicio.value
        serie = self.serie.value
        repeticiones = self.repeteciones.value
        peso = self.peso.value
        
        if self.auxiliar == int(self.n_series.value):
            b = BaseDatos()
            b.crearTablaDia(dia)
            b = BaseDatos()
            b.crearTablaDiaEjercicio(dia)
            b = BaseDatos()
            b.crearTablaDiaEjercicioDatos(dia)    
            b = BaseDatos()
            b.insertarTablaDia(dia, ejercicio)

        if self.auxiliar >= 0:
            b = BaseDatos()
            b.insertarTablaDiaEjercicio(dia, serie, peso, repeticiones)
            x = self.serie.options[0]
            self.serie.options.remove(x)
            self.pagina.update()
            self.auxiliar = self.auxiliar - 1

        if self.auxiliar == 0:
            self.ejercicio.value = ""
            self.pagina.update()
        

    def __init__(self, pagina):
        super().__init__(pagina)
        self.auxiliar = 0