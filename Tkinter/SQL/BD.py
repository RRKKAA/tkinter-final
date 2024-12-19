import mysql.connector
import bcrypt
from Clases.Usuarios import Usuario
from Clases.Trabajadores import Trabajador
from Clases.Contactos import Contacto
from Clases.Familiares import Familiar

def conectar_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Jujuy"
        )
        mycursor = mydb.cursor()
        return mydb, mycursor
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")

        #Usuarios

def registrar_usuario(nombre_usuario, contrasena_hasheada, rol, rut_usuario):
    try:
        mydb, mycursor = conectar_db()
        sql = "INSERT INTO usuarios (nombre_usuario, contrasena, rol, rut_usuario) VALUES (%s, %s, %s, %s)"
        val = (nombre_usuario, contrasena_hasheada, rol, rut_usuario)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Usuario registrado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()

def verificar_usuario(nombre_usuario, contrasena):
    try:
        mydb, mycursor = conectar_db()
        sql = "SELECT * FROM Usuarios WHERE nombre_usuario = %s"
        val = (nombre_usuario,)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()

        if resultado:
            if bcrypt.checkpw(contrasena.encode('utf-8'), resultado[2].encode('utf-8')):
                return Usuario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            else:
                return None
        else:
            return None
    except mysql.connector.Error as error:
        print(f"Error al verificar usuario: {error}")
        return None
    finally:
        if mydb:
            mydb.close()


        #Trabajadores

def insertar_trabajador(rut, nombre, apellido, sex, direccion, telefono, cargo, area, departamento):
    try:
        mydb, mycursor = conectar_db()
        sql = "INSERT INTO trabajadores (rut, nombre, apellido, sexo, direccion, telefono, cargo, area, departamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (rut, nombre, apellido, sex, direccion, telefono, cargo, area, departamento)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Usuario registrado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()



def obtener_trabajadores():
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM trabajadores")
        resultados = mycursor.fetchall()
        trabajadores = []
        for row in resultados:
            trabajador = Trabajador(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            trabajadores.append(trabajador)

        return trabajadores
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()
    
def obtener_trabajador_por_rut(rut):
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM trabajadores WHERE rut = %s"
        val = (rut,)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()
        if resultado:
            trabajador = Trabajador(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9])

            return trabajador
        else:
            return None
        
    except mysql.connector.Error as error:
        print(f"Error al obtener los trabajadores: {error}")
        return []
    finally:
        if mydb:
            mydb.close()

def ejecutar_consulta(consulta, parametros):
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        #sql = consulta
        val = [*parametros,]
        mycursor.execute(consulta,val)
        resultados = mycursor.fetchall()
        trabajadores = []
        for row in resultados:
            trabajador = Trabajador(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            trabajadores.append(trabajador)

        return trabajadores
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()

def obtener_ruts_disponibles():
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT rut_usuario FROM usuarios WHERE rol = 'trabajador' AND rut_usuario NOT IN (SELECT rut FROM trabajadores)")
        resultados = [row[0] for row in mycursor.fetchall()]
        return resultados
    except mysql.connector.Error as error:
        print(f"Error al obtener los trabajadores: {error}")
        return []
    finally:
        if mydb:
            mydb.close()

def actualizar_trabajador(rut, nuevo_nombre, nuevo_apellido, nuevo_sexo, nueva_direccion, nuevo_telefono, nuevo_cargo, nueva_area, nuevo_departamento):
    try:
        mydb, mycursor = conectar_db()
        sql = "UPDATE trabajadores SET nombre = %s, apellido = %s, sexo = %s, direccion = %s, telefono = %s, cargo = %s, area = %s, departamento = %s WHERE rut = %s"
        val = (nuevo_nombre, nuevo_apellido, nuevo_sexo, nueva_direccion, nuevo_telefono, nuevo_cargo, nueva_area, nuevo_departamento, rut)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Trabajador actualizado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al actualizar trabajador: {error}")
    finally:
        if mydb:
            mydb.close()

def eliminar_trabajador(rut):
    try:
        mydb, mycursor = conectar_db()
        sql = "DELETE FROM trabajadores WHERE rut = %s"
        val = (rut,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Trabajador eliminado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al eliminar trabajador: {error}")
    finally:
        if mydb:
            mydb.close()


        #Contactos

def registrar_contacto(nombre_contacto, relacion, telefono_contacto, rut_1):
    try:
        mydb, mycursor = conectar_db()
        sql = "INSERT INTO contactos (nombre_contacto, relacion, telefono_contacto, rut_1) VALUES (%s, %s, %s, %s)"
        val = (nombre_contacto, relacion, telefono_contacto, rut_1)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Contacto registrado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al registrar contacto: {error}")
    finally:
        if mydb:
            mydb.close()

def obtener_contactos_por_rut(rut_1):
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM contactos WHERE rut_1 = %s"
        val = (rut_1,)
        mycursor.execute(sql, val)
        resultados = mycursor.fetchall()
        contactos = []
        for row in resultados:
            contacto = Contacto(row[0], row[1], row[2], row[3], row[4])
            contactos.append(contacto)

        return contactos
    except mysql.connector.Error as error:
        print(f"Error al obtener los contactos: {error}")
        return []
    finally:
        if mydb:
            mydb.close()

def obtener_contacto_por_id(id_contacto):
    try:
        mydb, mycursor = conectar_db()
        sql = "SELECT * FROM contactos WHERE id_contacto = %s"
        val = (id_contacto,)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()
        if resultado:
            contacto = Contacto(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            return contacto
        else:
            return None
    except mysql.connector.Error as error:
        print(f"Error al obtener el contacto: {error}")
        return None
    finally:
        if mydb:
            mydb.close()

def actualizar_contacto(id_contacto, nombre_contacto, relacion, telefono_contacto):
    try:
        mydb, mycursor = conectar_db()
        sql = "UPDATE contactos SET nombre_contacto=%s, relacion=%s, telefono_contacto=%s WHERE id=%s"
        val = (nombre_contacto, relacion, telefono_contacto, id_contacto)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Contacto actualizado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al actualizar contacto: {error}")
    finally:
        if mydb:
            mydb.close()

def eliminar_contacto(id_contacto):
    try:
        mydb, mycursor = conectar_db()
        sql = "DELETE FROM contactos WHERE id_contacto=%s"
        val = (id_contacto,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Contacto eliminado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al eliminar contacto: {error}")
    finally:
        if mydb:
            mydb.close()

        #Familiares

def registrar_familiar(nombre_familiar, parentesco, sexo_familiar, rut_familiar, rut_2):
    try:
        mydb, mycursor = conectar_db()
        sql = "INSERT INTO familiares (nombre_familiar, parentesco, sexo_familiar, rut_familiar, rut_2) VALUES (%s, %s, %s, %s, %s)"
        val = (nombre_familiar, parentesco, sexo_familiar, rut_familiar, rut_2)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Contacto registrado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al registrar contacto: {error}")
    finally:
        if mydb:
            mydb.close()

def obtener_familiares_por_rut(rut_1):
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM familiares WHERE rut_2 = %s"
        val = (rut_1,)
        mycursor.execute(sql, val)
        resultados = mycursor.fetchall()
        familiares = []
        for row in resultados:
            familiar = Familiar(row[0], row[1], row[2], row[3], row[4], row[5])
            familiares.append(familiar)

        return familiares
    except mysql.connector.Error as error:
        print(f"Error al obtener los contactos: {error}")
        return []
    finally:
        if mydb:
            mydb.close()

def obtener_familiar_por_id(id_carga):
    try:
        mydb, mycursor = conectar_db()
        sql = "SELECT * FROM familiares WHERE id_carga = %s"
        val = (id_carga,)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()
        if resultado:
            familiar = Familiar(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            return familiar
        else:
            return None
    except mysql.connector.Error as error:
        print(f"Error al obtener el familiar: {error}")
        return None
    finally:
        if mydb:
            mydb.close()

def actualizar_familiar(id_carga, nombre_familiar, parentesco, sexo_familiar, rut_familiar):
    try:
        mydb, mycursor = conectar_db()
        sql = "UPDATE familiares SET nombre_familiar=%s, parentesco=%s, sexo_familiar=%s, rut_familiar=%s WHERE id_carga=%s"
        val = (nombre_familiar, parentesco, sexo_familiar, rut_familiar, id_carga)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Carga familiar actualizado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al actualizar familiar: {error}")
    finally:
        if mydb:
            mydb.close()

def eliminar_familiar(id_carga):
    try:
        mydb, mycursor = conectar_db()
        sql = "DELETE FROM familiares WHERE id_carga=%s"
        val = (id_carga,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Carga familiar eliminado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al eliminar familiar: {error}")
    finally:
        if mydb:
            mydb.close()