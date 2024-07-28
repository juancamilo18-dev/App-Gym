import flet as ft
from assets.form.form_desing.desing import DiseñoApp
from assets.bd.comandos import BaseDatos
import datetime, sqlite3

class LogicaDesing(DiseñoApp):
    def estructura(self, rutina, con_ejercicios, con_datos_ejercicios, tabla_inser):
        now_date = datetime.datetime.now()
        now = now_date.strftime("%d-%m-%Y")

        def ingresar(e):
            for i in con_ejercicios:
                if i[1] == ejercicios.value:
                    b = BaseDatos()
                    b.insertarTablaDiaEjercicioDatos(i[0], tabla_inser, series.value, self.peso.value, self.repeticiones.value, now)
                    x = series.options[0]
                    series.options.remove(x)
                    self.pagina.update()

            for i in con_ejercicios:
                if ejercicios.value == i[1]:
                    id = i[0]
                    for a in con_datos_ejercicios:
                        if id == a[0] and int(series.value) == a[1]:
                            texto = ft.Text()
                            texto.value = f"Serie {a[1]}\nPeso: {int(self.peso.value )- a[2]}\nRepeticiones: {int(self.repeticiones.value) - a[3]}"
                            self.contenido.controls.append(texto)

            if series.options == []:
                self.seleccion.disabled = False
                self.ingresar_datos.disabled = True

            self.pagina.update()


        def seleccionar(e):
            self.ingresar_datos.disabled = False
            series.options = []
            vaciarInforme()
            
            try:
                for i in con_ejercicios:
                    if ejercicios.value == i[1]:
                        id = i[0]
                        for a in con_datos_ejercicios:
                            if id == a[0]:
                                series.options.append(ft.dropdown.Option(a[1]))
                        seleccionTabla(id)
                        seleccionUltimosDatos(id)
                self.seleccion.disabled = True
            except sqlite3.DatabaseError:
                self.pagina.snack_bar = ft.SnackBar(ft.Text("Error: Tabla no encontrada"), bgcolor="red", duration=600)
                self.pagina.snack_bar.open = True
                self.pagina.update()
                    
            self.pagina.update()
        
                    
        self.pagina.clean()
        self.pagina.vertical_alignment = ft.MainAxisAlignment.START
        self.texto = ft.Text(rutina, weight="bold", size=25)
        self.regresar = ft.TextButton("Regresar")
        self.seleccion = ft.TextButton("Seleccionar", on_click=seleccionar)
        self.ingresar_datos = ft.TextButton("Ingresar", on_click=ingresar, disabled=True)

        series, ejercicios = self.entradasSeries(con_ejercicios)

        self.peso = ft.TextField(label="Peso", hint_text="Peso", width=90)

        self.fecha = ft.TextField(label="Fecha", hint_text="Fecha", expand=True, value=now)

        # SECCIÓN DE ENTRADA DE REPETICIONES Y BOTONES (+) Y (-)

        self.repeticiones = ft.TextField(value="0", label="Reps", width=70)

        def mas(e):
            self.repeticiones.value = int(self.repeticiones.value) + 1
            self.pagina.update()

        def menos(e):
            if int(self.repeticiones.value) > 0:
                self.repeticiones.value = int(self.repeticiones.value) - 1
                self.pagina.update()

        self.disminuir = ft.IconButton(ft.icons.REMOVE, on_click=menos)
        self.aumentar = ft.IconButton(ft.icons.ADD, on_click=mas)

        # SECCIÓN DE TABLAS

        self.tabla = ft.DataTable(
            expand=True,
            columns=[
                ft.DataColumn(ft.Text("Serie", weight="bold")),
                ft.DataColumn(ft.Text("Peso", weight="bold")),
                ft.DataColumn(ft.Text("Repeteciones", weight="bold")) 
            ]
        )

        def seleccionTabla(id):
            self.tabla.rows = []
            for i in con_datos_ejercicios:
                if i[0] == id:
                    self.tabla.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(f"{i[1]}")),
                                ft.DataCell(ft.Text(f"{i[2]}")),
                                ft.DataCell(ft.Text(f"{i[3]}"))
                                
                            ]
                        )
                    )
            self.pagina.update()

        self.tabla_datos = ft.DataTable(
            expand=True,
            columns=[
                ft.DataColumn(ft.Text("Serie")),
                ft.DataColumn(ft.Text("Peso")),
                ft.DataColumn(ft.Text("Repeticiones"))
            ]
        )

        def seleccionUltimosDatos(id):
            self.tabla_datos.rows = []
            b = BaseDatos()
            contenido = b.mostrarDatosTablaDia(tabla_inser)
            contenido.reverse()
            n_series = 0

            for i in con_datos_ejercicios:
                if id == i[0]:
                    n_series = n_series + 1

            for i in contenido:
                if i[0] == id and n_series > 0:
                    self.tabla_datos.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(f"{i[1]}")),
                                ft.DataCell(ft.Text(f"{i[2]}")),
                                ft.DataCell(ft.Text(f"{i[3]}"))
                            ]
                        )
                    )
                    n_series = n_series - 1
            self.tabla_datos.rows.reverse()
            self.pagina.update()

        # SECCIÓN DE INFORME    

        self.informe = ft.Text("Informe", weight="bold", size=20)

        self.contenedor_tabla = ft.Container(
            col=7,
            content=ft.Column(
                scroll="auto",
                controls=[ft.ResponsiveRow(controls=[self.tabla_datos])]
            )
        )

        texto = ft.Text("Hola")

        self.contenido = ft.Column(
                                    scroll="auto",
                                    controls=[self.informe, texto]
                                               )
        
        def vaciarInforme():
            self.contenido.controls = []
            self.contenido.controls.append(self.informe)

        self.contenedor_informe = ft.Container(
                                                col=5,
                                               content=self.contenido)
        
        self.contenedor = ft.ResponsiveRow(controls=[self.contenedor_informe, self.contenedor_tabla], expand=True)

        # AÑADIR ELEMENTOS  

        self.pagina.add(ft.Row(controls=[self.texto], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ejercicios, series, self.peso, self.disminuir, self.repeticiones, self.aumentar, self.fecha]),
                        ft.Row(controls=[self.ingresar_datos, self.seleccion, self.regresar]),
                        ft.Row(controls=[self.tabla]),
                        self.contenedor)
        
    def lunesRutina(self):
        tabla = "lunes"
        try:
            b = BaseDatos()
            contendio = b.mostrarDatosTablaDia(tabla)
            b = BaseDatos()
            contenido_datos = b.mostrarDatosTablaDia("datos"+tabla)
            self.estructura("Rutina Lunes", contendio, contenido_datos, "datosejerciciolunes")
        except:
            self.pagina.snack_bar = ft.SnackBar(ft.Text("No hay registros"), bgcolor="red", duration=800)
            self.pagina.snack_bar.open = True
            self.pagina.update()

    def martesRutina(self):
        tabla = "martes"
        try:
            b = BaseDatos()
            contendio = b.mostrarDatosTablaDia(tabla)
            b = BaseDatos()
            contenido_datos = b.mostrarDatosTablaDia("datos"+tabla)
            self.estructura("Rutina Martes", contendio, contenido_datos, "datosejerciciomartes")
        except:
            self.pagina.snack_bar = ft.SnackBar(ft.Text("No hay registros"), bgcolor="red", duration=800)
            self.pagina.snack_bar.open = True
            self.pagina.update()
        
    def miercolesRutina(self):
        tabla = "miercoles"
        try:
            b = BaseDatos()
            contendio = b.mostrarDatosTablaDia(tabla)
            b = BaseDatos()
            contenido_datos = b.mostrarDatosTablaDia("datos"+tabla)
            self.estructura("Rutina Miercoles", contendio, contenido_datos, "datosejerciciomiercoles")
        except:
            self.pagina.snack_bar = ft.SnackBar(ft.Text("No hay registros"), bgcolor="red", duration=800)
            self.pagina.snack_bar.open = True
            self.pagina.update()
    
    def juevesRutina(self):
        tabla = "jueves"
        try:
            b = BaseDatos()
            contendio = b.mostrarDatosTablaDia(tabla)
            b = BaseDatos()
            contenido_datos = b.mostrarDatosTablaDia("datos"+tabla)
            self.estructura("Rutina Jueves", contendio, contenido_datos, "datosejerciciojueves")
        except:
            self.pagina.snack_bar = ft.SnackBar(ft.Text("No hay registros"), bgcolor="red", duration=800)
            self.pagina.snack_bar.open = True
            self.pagina.update()

    def viernesRutina(self):
        tabla = "viernes"
        try:
            b = BaseDatos()
            contendio = b.mostrarDatosTablaDia(tabla)
            b = BaseDatos()
            contenido_datos = b.mostrarDatosTablaDia("datos"+tabla)
            self.estructura("Rutina Viernes", contendio, contenido_datos, "datosejercicioviernes")
        except:
            self.pagina.snack_bar = ft.SnackBar(ft.Text("No hay registros"), bgcolor="red", duration=800)
            self.pagina.snack_bar.open = True
            self.pagina.update()            

    def sabadoRutina(self):
        tabla = "sabado"
        try:
            b = BaseDatos()
            contendio = b.mostrarDatosTablaDia(tabla)
            b = BaseDatos()
            contenido_datos = b.mostrarDatosTablaDia("datos"+tabla)
            self.estructura("Rutina Sabado", contendio, contenido_datos, "datosejerciciosabado")
        except:
            self.pagina.snack_bar = ft.SnackBar(ft.Text("No hay registros"), bgcolor="red", duration=800)
            self.pagina.snack_bar.open = True
            self.pagina.update()
    def __init__(self, pagina):
        super().__init__(pagina)