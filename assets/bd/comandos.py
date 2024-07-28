import mysql
import mysql.connector


class BaseDatos:
    def __init__(self):
        self.base_datos = mysql.connector.connect(user="tu_usuario", password="tu_contraseña", host="tu_local_host", port="tu_puerto", db="tu_base_de _datos")
        self.cursor = self.base_datos.cursor()

    def cerrarConexion(self):
        self.base_datos.commit()
        self.base_datos.close()

    # Creación tabla
    def crearTablaDia(self, tabla):
        sql = f"""CREATE TABLE IF NOT EXISTS {tabla}(
        id_ejercicio INT NOT NULL AUTO_INCREMENT,
        ejercicio VARCHAR(50),
        PRIMARY KEY(id_ejercicio)
        )"""
        self.cursor.execute(sql)
        self.cerrarConexion()

    def crearTablaDiaEjercicio(self, tabla):
        tabla_datos = "datos"+tabla
        sql = f"""CREATE TABLE IF NOT EXISTS {tabla_datos}(
        id INT NOT NULL,
        serie INT,
        peso INT,
        repeticiones INT,
        FOREIGN KEY(id) REFERENCES {tabla}(id_ejercicio)
        )"""
        self.cursor.execute(sql)
        self.cerrarConexion()

    def crearTablaDiaEjercicioDatos(self, tabla):
        tabla_datos = "datosejercicio"+tabla
        sql = f"""CREATE TABLE IF NOT EXISTS {tabla_datos}(
        id_ejer INT NOT NULL,
        serie INT,
        peso INT,
        repeticiones INT,
        fecha VARCHAR(50),
        FOREIGN KEY(id_ejer) REFERENCES {tabla}(id_ejercicio)
        )"""
        self.cursor.execute(sql)
        self.cerrarConexion()

    def insertarTablaDiaEjercicioDatos(self, item,tabla, serie, peso, repeticiones, fecha):
        sql = f"""INSERT INTO {tabla}(id_ejer, serie, peso, repeticiones, fecha) VALUES({item}, {serie}, {peso}, {repeticiones}, '{fecha}')"""
        self.cursor.execute(sql)
        self.cerrarConexion()

    def insertarTablaDia(self, tabla, ejercicio):
        sql = f"""INSERT INTO {tabla}(ejercicio) VALUES('{ejercicio}')"""
        self.cursor.execute(sql)
        self.cerrarConexion()

    def mostrarDatosTablaDia(self, tabla):
        sql = f"""SELECT * FROM {tabla}"""
        self.cursor.execute(sql)
        contenido = self.cursor.fetchall()

        return contenido

    def insertarTablaDiaEjercicio(self, tabla, serie, peso, repeticiones):
        contenido = self.mostrarDatosTablaDia(tabla)
        contenido.reverse()
        item = contenido[0]

        BaseDatos()
        tabla_datos = "datos"+tabla
        sql = f"""INSERT INTO {tabla_datos}(id, serie, peso, repeticiones) VALUES({item[0]}, {serie}, {peso}, {repeticiones})"""
        self.cursor.execute(sql)
        self.cerrarConexion()
