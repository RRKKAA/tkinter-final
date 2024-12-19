import bcrypt

class Usuario:
    def __init__(self, id:int, nombre_usuario:str, contrasena:str, rol:str, rut_usuario:str):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol
        self.rut_usuario = rut_usuario

    def set_contrasena(self, nueva_contrasena):
        # Aplicar algoritmo de hash para encriptar la contraseña
        salt = bcrypt.gensalt()
        self.contrasena = bcrypt.hashpw(nueva_contrasena.encode('utf-8'), salt)

    def verificar_contrasena(self, contrasena_ingresada):
        return bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), self.contrasena.encode('utf-8'))
    
    @staticmethod
    def hash_password(password):
        """Hashea una contraseña utilizando bcrypt."""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def __str__(self):
        return f"Usuario(id={self.id_usuario}, nombre={self.nombre_usuario}, rol={self.rol})"