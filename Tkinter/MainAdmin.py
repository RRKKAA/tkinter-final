import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from SQL import BD
from Clases import Trabajadores

ventana_admin = tk.Tk()
ventana_admin.title("El Correo de Yury")

tabla_trabajadores = ttk.Treeview(ventana_admin, columns=("ID","rut", "nombre", "apellido", "sexo", "direccion", "telefono", "cargo", "area", "departamento"))
tabla_trabajadores.heading("ID", text="ID")
tabla_trabajadores.heading("rut", text="RUT")
tabla_trabajadores.heading("nombre", text="Nombre")
tabla_trabajadores.heading("apellido", text="Apellido")
tabla_trabajadores.heading("sexo", text="Sexo")
tabla_trabajadores.heading("direccion", text="Direccion")
tabla_trabajadores.heading("telefono", text="Telefono")
tabla_trabajadores.heading("cargo", text="Cargo")
tabla_trabajadores.heading("area", text="Area")
tabla_trabajadores.heading("departamento", text="Departamento")
tabla_trabajadores.pack()

def crear_contactos(rut_1):
    ventana_contactocrear = tk.Toplevel()
    ventana_contactocrear.title("Crear Nuevo Contacto")

    opciones_relacion = ["Amigo", "Familiar", "Vecino", "Compañero", "Otro"]
    rut_1 = rut_1

    # Crear los campos del formulario
    label_nombre_contacto = ttk.Label(ventana_contactocrear, text="Nombre:")
    label_nombre_contacto.pack()
    entry_nombre_contacto = ttk.Entry(ventana_contactocrear)
    entry_nombre_contacto.pack()

    label_relacion = ttk.Label(ventana_contactocrear, text="Relacion:")
    label_relacion.pack()
    combobox_relacion = ttk.Combobox(ventana_contactocrear, values=opciones_relacion)
    combobox_relacion.pack()

    label_telefono_contacto = ttk.Label(ventana_contactocrear, text="Telefono:")
    label_telefono_contacto.pack()
    entry_telefono_contacto = ttk.Entry(ventana_contactocrear)
    entry_telefono_contacto.pack()

    boton_guardar_contacto = ttk.Button(ventana_contactocrear, text="Guardar", command=lambda: crear_contacto(rut_1))
    boton_guardar_contacto.pack()

    def crear_contacto(rut_1):
        nombre = entry_nombre_contacto.get()
        relacion = combobox_relacion.get()
        telefono = entry_telefono_contacto.get()
        rut_1 = rut_1
        
        # Insertar los datos en la base de datos
        BD.registrar_contacto(nombre, relacion, telefono, rut_1)  # Ajusta según tu función
        
        # Cerrar la ventana modal
        ventana_contactocrear.destroy()
        
        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Éxito", "Contacto registrado correctamente.")

def crear_familiares(rut_1):
    ventana_familiarcrear = tk.Toplevel()
    ventana_familiarcrear.title("Crear Nuevo Familiar")

    opciones_parentesco = ["Padre/Madre", "Abuelo/Abuela", "Hermano/Hermana", "Hijo/Hija", "Tio/Tia", "Suegro/Suegra", "Otro"]
    rut_1 = rut_1

    # Crear los campos del formulario
    label_nombre_familiar = ttk.Label(ventana_familiarcrear, text="Nombre:")
    label_nombre_familiar.pack()
    entry_nombre_contacto = ttk.Entry(ventana_familiarcrear)
    entry_nombre_contacto.pack()

    label_parentesco = ttk.Label(ventana_familiarcrear, text="Parentesco:")
    label_parentesco.pack()
    combobox_parentesco = ttk.Combobox(ventana_familiarcrear, values=opciones_parentesco)
    combobox_parentesco.pack()

    label_sexo_familiar = ttk.Label(ventana_familiarcrear, text="Sexo:")
    label_sexo_familiar.pack()
    combobox_sexo_familiar = ttk.Combobox(ventana_familiarcrear, values=opciones_parentesco)
    combobox_sexo_familiar.pack()

    label_rut_familiar = ttk.Label(ventana_familiarcrear, text="RUT:")
    label_rut_familiar.pack()
    entry_rut_familiar = ttk.Entry(ventana_familiarcrear)
    entry_rut_familiar.pack()

    boton_guardar_familiar = ttk.Button(ventana_familiarcrear, text="Guardar", command=lambda: crear_familiar(rut_1))
    boton_guardar_familiar.pack()

    def crear_familiar(rut_1):
        nombre = entry_nombre_contacto.get()
        parentesco = combobox_parentesco.get()
        sexo = combobox_sexo_familiar.get()
        rut = entry_rut_familiar.get()
        rut_2 = rut_1
        
        # Insertar los datos en la base de datos
        BD.registrar_familiar(nombre, parentesco, sexo, rut, rut_2)  # Ajusta según tu función
        
        # Cerrar la ventana modal
        ventana_familiarcrear.destroy()
        
        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Éxito", "Familiar registrado correctamente.")

def listar_trabajadores_admin():
    datos_trabajadores = BD.obtener_trabajadores()

    print(datos_trabajadores)

    tabla_trabajadores.delete(*tabla_trabajadores.get_children())
    for trabajador in datos_trabajadores:
        tabla_trabajadores.insert('', 'end', values=(trabajador.id, trabajador.rut, trabajador.nombre, trabajador.apellido, trabajador.sexo, trabajador.direccion, trabajador.telefono, trabajador.cargo, trabajador.area, trabajador.departamento))

        def mostrar_menu_contexto(event):
            # Obtener el item seleccionado
            item = tabla_trabajadores.identify('item', event.x, event.y)
            if item:
                # Obtener el ID del contacto
                rut = tabla_trabajadores.item(item)['values'][1]

                # Crear el menú contextual
                menu_familiar = tk.Menu(tabla_trabajadores, tearoff=0)
                menu_familiar.add_command(label="Nuevo Contacto", command=lambda: crear_contactos(rut))
                menu_familiar.add_command(label="Nuevo Familiar", command=lambda: crear_familiares(rut))

                # Mostrar el menú en la posición del clic
                menu_familiar.post(event.x_root, event.y_root)

        tabla_trabajadores.bind("<Button-3>", mostrar_menu_contexto)


def registrar_nuevo_trabajador():
    ventana_registro1 = tk.Toplevel()
    ventana_registro1.title("Registrar Nuevo Trabajador")

    rut_disponibles = BD.obtener_ruts_disponibles()
    opciones_sexo = ["Hombre", "Mujer", "Otro"]
    opciones_cargos = ["Consultor", "Desarrollador", "Diseñador", "Gerente"]
    opciones_areas = ["Ventas", "Marketing", "Desarrollo", "Administración"]
    opciones_departamentos = ["Tecnología", "Comercial", "Recursos Humanos"]

    label_rut = ttk.Label(ventana_registro1, text="Rut:")
    label_rut.pack()
    combobox_rut = ttk.Combobox(ventana_registro1, values=rut_disponibles)
    combobox_rut.pack()

    label_nombre = ttk.Label(ventana_registro1, text="Nombre:")
    label_nombre.pack()
    entry_nombre = ttk.Entry(ventana_registro1)
    entry_nombre.pack()

    label_apellido = ttk.Label(ventana_registro1, text="Apellido:")
    label_apellido.pack()
    entry_apellido = ttk.Entry(ventana_registro1)
    entry_apellido.pack()

    label_sexo = ttk.Label(ventana_registro1, text="Sexo:")
    label_sexo.pack()
    combobox_sexo = ttk.Combobox(ventana_registro1, values=opciones_sexo)
    combobox_sexo.pack()

    label_direccion = ttk.Label(ventana_registro1, text="Direccion:")
    label_direccion.pack()
    entry_direccion = ttk.Entry(ventana_registro1)
    entry_direccion.pack()

    label_telefono = ttk.Label(ventana_registro1, text="Telefono:")
    label_telefono.pack()
    entry_telefono = ttk.Entry(ventana_registro1)
    entry_telefono.pack()

    label_cargo = ttk.Label(ventana_registro1, text="Cargo:")
    label_cargo.pack()
    combobox_cargo = ttk.Combobox(ventana_registro1, values=opciones_cargos)
    combobox_cargo.pack()

    label_area = ttk.Label(ventana_registro1, text="Area:")
    label_area.pack()
    combobox_area = ttk.Combobox(ventana_registro1, values=opciones_areas)
    combobox_area.pack()

    label_departamento = ttk.Label(ventana_registro1, text="Departamento:")
    label_departamento.pack()
    combobox_departamento = ttk.Combobox(ventana_registro1, values=opciones_departamentos)
    combobox_departamento.pack()
    
    def guardar_trabajador():
        rut = combobox_rut.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        sexo = combobox_sexo.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        cargo = combobox_cargo.get()
        area = combobox_area.get()
        departamento = combobox_departamento.get()
        
        BD.insertar_trabajador(rut, nombre, apellido, sexo, direccion, telefono, cargo, area, departamento)
        ventana_registro1.destroy()
        messagebox.showinfo("Éxito", "Trabajador registrado correctamente.")

    boton_guardar = ttk.Button(ventana_registro1, text="Guardar", command=guardar_trabajador)
    boton_guardar.pack()

def filtrar_trabajadores():
    ventana_filtros = tk.Toplevel()
    ventana_filtros.title("Filtros de Búsqueda")

    opciones_sexo = ["Hombre", "Mujer", "Otro"]
    opciones_cargos = ["Consultor", "Desarrollador", "Diseñador", "Gerente"]
    opciones_departamentos = ["Tecnología", "Comercial", "Recursos Humanos"]

    label_sexo = ttk.Label(ventana_filtros, text="Sexo:")
    label_sexo.pack()
    combobox_sexo = ttk.Combobox(ventana_filtros, values=opciones_sexo)
    combobox_sexo.pack()

    label_cargo = ttk.Label(ventana_filtros, text="Cargo:")
    label_cargo.pack()
    combobox_cargo = ttk.Combobox(ventana_filtros, values=opciones_cargos)
    combobox_cargo.pack()

    label_departamento = ttk.Label(ventana_filtros, text="Departamento:")
    label_departamento.pack()
    combobox_departamento = ttk.Combobox(ventana_filtros, values=opciones_departamentos)
    combobox_departamento.pack()

    def aplicar_filtros():
        sexo_seleccionado = combobox_sexo.get()
        cargo_seleccionado = combobox_cargo.get()
        departamento_seleccionado = combobox_departamento.get()

        consulta = "SELECT * FROM trabajadores WHERE "
        condiciones = []
        parametros = []

        if sexo_seleccionado:
            condiciones.append("sexo = %s")
            parametros.append(sexo_seleccionado)

        if cargo_seleccionado:
            condiciones.append("cargo = %s")
            parametros.append(cargo_seleccionado)

        if departamento_seleccionado:
            condiciones.append("departamento = %s")
            parametros.append(cargo_seleccionado)

        if condiciones:
            consulta += " AND ".join(condiciones)
            resultados = BD.ejecutar_consulta(consulta, parametros)
        else:
            resultados = BD.obtener_trabajadores()

        print(consulta)
        tabla_trabajadores.delete(*tabla_trabajadores.get_children())
        for trabajador in resultados:
            tabla_trabajadores.insert('', 'end', values=(trabajador.id, trabajador.rut, trabajador.nombre, trabajador.sexo, trabajador.cargo))
        ventana_filtros.destroy()

    boton_aplicar = ttk.Button(ventana_filtros, text="Aplicar", command=aplicar_filtros)
    boton_aplicar.pack()

menubar = tk.Menu(ventana_admin)

menu_trabajadores = tk.Menu(menubar, tearoff=0)
menu_trabajadores.add_command(label="Listar trabajadores", command=listar_trabajadores_admin)
menubar.add_cascade(label="Trabajadores", menu=menu_trabajadores)


menu_acciones = tk.Menu(menu_trabajadores, tearoff=0)
menu_acciones.add_command(label="Registrar nuevo", command=registrar_nuevo_trabajador)
menu_trabajadores.add_cascade(label="Acciones", menu=menu_acciones)
menu_trabajadores.add_command(label="Listar por filtro", command=filtrar_trabajadores)

ventana_admin.config(menu=menubar)

ventana_admin.mainloop()

def crear_contactos(rut_1):
    ventana_contactocrear = tk.Toplevel()
    ventana_contactocrear.title("Crear Nuevo Contacto")

    opciones_relacion = ["Amigo", "Familiar", "Vecino", "Compañero", "Otro"]
    rut_1 = rut_1

    label_nombre_contacto = ttk.Label(ventana_contactocrear, text="Nombre:")
    label_nombre_contacto.pack()
    entry_nombre_contacto = ttk.Entry(ventana_contactocrear)
    entry_nombre_contacto.pack()

    label_relacion = ttk.Label(ventana_contactocrear, text="Relacion:")
    label_relacion.pack()
    combobox_relacion = ttk.Combobox(ventana_contactocrear, values=opciones_relacion)
    combobox_relacion.pack()

    label_telefono_contacto = ttk.Label(ventana_contactocrear, text="Telefono:")
    label_telefono_contacto.pack()
    entry_telefono_contacto = ttk.Entry(ventana_contactocrear)
    entry_telefono_contacto.pack()

    boton_guardar_contacto = ttk.Button(ventana_contactocrear, text="Guardar", command=lambda: crear_contacto(rut_1))
    boton_guardar_contacto.pack()

    def crear_contacto(rut_1):
        nombre = entry_nombre_contacto.get()
        relacion = combobox_relacion.get()
        telefono = entry_telefono_contacto.get()
        rut_1 = rut_1
        
        BD.registrar_contacto(nombre, relacion, telefono, rut_1)
        
        ventana_contactocrear.destroy()
        
        messagebox.showinfo("Éxito", "Contacto registrado correctamente.")

def crear_familiares(rut_1):
    ventana_familiarcrear = tk.Toplevel()
    ventana_familiarcrear.title("Crear Nuevo Familiar")

    opciones_parentesco = ["Padre/Madre", "Abuelo/Abuela", "Hermano/Hermana", "Hijo/Hija", "Tio/Tia", "Suegro/Suegra", "Otro"]
    rut_1 = rut_1

    label_nombre_familiar = ttk.Label(ventana_familiarcrear, text="Nombre:")
    label_nombre_familiar.pack()
    entry_nombre_contacto = ttk.Entry(ventana_familiarcrear)
    entry_nombre_contacto.pack()

    label_parentesco = ttk.Label(ventana_familiarcrear, text="Parentesco:")
    label_parentesco.pack()
    combobox_parentesco = ttk.Combobox(ventana_familiarcrear, values=opciones_parentesco)
    combobox_parentesco.pack()

    label_sexo_familiar = ttk.Label(ventana_familiarcrear, text="Sexo:")
    label_sexo_familiar.pack()
    combobox_sexo_familiar = ttk.Combobox(ventana_familiarcrear, values=opciones_parentesco)
    combobox_sexo_familiar.pack()

    label_rut_familiar = ttk.Label(ventana_familiarcrear, text="RUT:")
    label_rut_familiar.pack()
    entry_rut_familiar = ttk.Entry(ventana_familiarcrear)
    entry_rut_familiar.pack()

    boton_guardar_familiar = ttk.Button(ventana_familiarcrear, text="Guardar", command=lambda: crear_familiar(rut_1))
    boton_guardar_familiar.pack()

    def crear_familiar(rut_1):
        nombre = entry_nombre_contacto.get()
        parentesco = combobox_parentesco.get()
        sexo = combobox_sexo_familiar.get()
        rut = entry_rut_familiar.get()
        rut_2 = rut_1
        
        BD.registrar_familiar(nombre, parentesco, sexo, rut, rut_2)
        
        ventana_familiarcrear.destroy()
        
        messagebox.showinfo("Éxito", "Familiar registrado correctamente.")