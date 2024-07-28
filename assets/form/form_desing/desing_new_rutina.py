import flet as ft

class CrearRutina:
    def __init__(self, pagina):
        self.pagina = pagina

        self.contenedor_lateral = ft.Container(
            padding=10,
            col=4
        )

        self.contendor_derecho = ft.Container(
            col=8
        )

    def diseño(self):
        self.regresar = ft.TextButton("Salir")
        # LISTADO DÍA DE LAS SEMANAS
        self.day_weeks = ft.Dropdown(
            label="Día de la semana",
            options=[
                ft.dropdown.Option("Lunes"),
                ft.dropdown.Option("Martes"),
                ft.dropdown.Option("Miercoles"),
                ft.dropdown.Option("Jueves"),
                ft.dropdown.Option("Viernes"),
                ft.dropdown.Option("Sabado")
            ]
        )

        self.ejercicio = ft.TextField(label="Ejercicio", hint_text="Ejercicio")
        self.n_series = ft.TextField(label="Número de series", hint_text="Número de series")
        self.btn_update = ft.TextButton("Actualizar", on_click=self.actualizar)

        # LISTADO DE SERIES
        self.serie = ft.Dropdown(label="Serie", width=140)
        self.peso = ft.TextField(label="Peso", hint_text="Peso", width=140)
        self.repeteciones = ft.TextField(label="Repeticiones", hint_text="Repeticiones", width=140)
        self.agregar = ft.TextButton("Agregar", on_click=self.ingresar)

        self.pagina.add(ft.Row(controls=[self.day_weeks]),
                   ft.Column(controls=[self.ejercicio,
                                       ft.Row(controls=[self.n_series, self.btn_update]),
                                       ft.Row(controls=[self.serie, self.repeteciones, self.peso, self.agregar]),
                                       self.regresar]))
        
    
    # MÉTODOS DE LOS BOTONES
    def actualizar(self):
        pass
    
    def ingresar(self):
        pass