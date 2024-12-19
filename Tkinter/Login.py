import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Clases.Usuarios as Usuarios
import SQL.BD as BD
from Clases.Trabajadores import Trabajador

def ventana_registro(): #crea la ventana del usuario

    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrarse")
    ventana_registro.geometry("480x360")

    label_usuario = ttk.Label(ventana_registro, text="Usuario:")
    label_usuario.pack()
    entry_usuario = ttk.Entry(ventana_registro)
    entry_usuario.pack()

    label_contrasena = ttk.Label(ventana_registro, text="Contraseña:")
    label_contrasena.pack()
    entry_contrasena = ttk.Entry(ventana_registro, show="*")
    entry_contrasena.pack()

    roles = ["Administrador", "RR.HH.", "Trabajador"]
    variable = tk.StringVar()
    variable.set(roles[0])

    label_rol = ttk.Label(ventana_registro, text="Rol:")
    label_rol.pack()
    combobox_rol = ttk.Combobox(ventana_registro, textvariable=variable, values=roles)
    combobox_rol.pack()

    label_rut = ttk.Label(ventana_registro, text="Rut:")
    label_rut.pack()
    entry_rut = ttk.Entry(ventana_registro)
    entry_rut.pack()

    def registrar():
        nombre_usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()
        rol = variable.get()
        rut_usuario = entry_rut.get()

        if not nombre_usuario or not contrasena or not rol or not rut_usuario:
            messagebox.showerror("Error", "Por favor, complete sus datos.")
            return

        hashed_password = Usuarios.Usuario.hash_password(contrasena)

        if BD.registrar_usuario(nombre_usuario, hashed_password, rol, rut_usuario):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            entry_usuario.delete(0, tk.END)
            entry_contrasena.delete(0, tk.END)
            variable.set("")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "Error al registrar al usuario. Por favor, intenta nuevamente.")

    boton_registrar = ttk.Button(ventana_registro, text="Registrar", command=registrar)
    boton_registrar.pack()

def login():
    nombre_usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not nombre_usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return

    usuario_db = BD.verificar_usuario(nombre_usuario, contrasena)

    if usuario_db:
        usuario_app = Usuarios.Usuario(usuario_db.id, usuario_db.nombre_usuario, usuario_db.contrasena, usuario_db.rol, usuario_db.rut_usuario)
        if usuario_app.rol == 'Administrador':
            messagebox.showinfo("Éxito", "Bienvenido, administrador")
            ventana_login.destroy()
            import MainAdmin

        elif usuario_app.rol == 'RR.HH.':
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario_app.nombre_usuario}")
            ventana_login.destroy()
            import MainAdmin


        elif usuario_app.rol == 'Trabajador':
            rut_trabajador = usuario_db.rut_usuario
            trabajador = BD.obtener_trabajador_por_rut(rut_trabajador)
            if trabajador:
                messagebox.showinfo("Éxito", f"Bienvenido, {usuario_app.nombre_usuario}")
                ventana_login.destroy()
                import MainTrabajador
                MainTrabajador.ventana_registro_trabajador(rut_trabajador)
            else: 
                messagebox.showinfo("Acceso negado", "Todavia no estas asignado, contacta con RR.HH e intente mas tarde")
        else:
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario_app.nombre_usuario}")
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

ventana_login = tk.Tk()
ventana_login.title("Iniciar Sesión")
ventana_login.geometry("300x200")

label_usuario = ttk.Label(ventana_login, text="Usuario:")
label_usuario.pack()
entry_usuario = ttk.Entry(ventana_login)
entry_usuario.pack()

label_contrasena = ttk.Label(ventana_login, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = ttk.Entry(ventana_login, show="*")
entry_contrasena.pack()


boton_login = ttk.Button(ventana_login, text="Iniciar Sesión", command=login)
boton_login.pack()

boton_registro = ttk.Button(ventana_login, text="¿No tienes una cuenta? Registrarte", command=ventana_registro)
boton_registro.pack()

ventana_login.mainloop()

