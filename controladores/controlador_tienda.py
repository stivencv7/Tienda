from bd import obtener_conexion


def listaUsuario():
    conecxion = obtener_conexion()
    usuarios = []
    with conecxion.cursor() as cursor:
        cursor.execute(
            'SELECT usuarios.Codigo ,usuarios.nombresCompletos,usuarios.numeroCelular,usuarios.cuenta FROM tienda.usuarios')
        usuarios = cursor.fetchall()
    conecxion.close()
    return usuarios


def Agregar_usario(nombresCompletos, numeroCelular, cuenta):
    conecxion = obtener_conexion()
    with conecxion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombresCompletos,numeroCelular,cuenta)VALUES(%s,%s,%s)",
                       (nombresCompletos, numeroCelular, cuenta))
    conecxion.commit()
    conecxion.close()


def buscar(numeroCelular):
    conecxion = obtener_conexion()
    usuarios = []
    with conecxion.cursor() as cursor:
        cursor.execute(
            'SELECT   u.Codigo,u.nombresCompletos,u.numeroCelular,u.cuenta FROM tienda.usuarios as u WHERE u.numeroCelular=%s', (numeroCelular,))
        usuarios = cursor.fetchall()
    conecxion.commit()
    conecxion.close()
    return usuarios


def edit(numeroCelular):
    conecxion = obtener_conexion()
    usuario = None
    with conecxion.cursor() as cursor:
        cursor.execute(
            'SELECT  usuarios.Codigo as Codigo, usuarios.nombresCompletos as nombresClompletos,usuarios.numeroCelular as numeroCelular,usuarios.cuenta as cuenta FROM tienda.usuarios  WHERE numeroCelular=%s', (numeroCelular))
        usuario = cursor.fetchone()
    conecxion.close()
    return usuario


def actualizar(nombresCompletos, numeroCelular, cuenta, Codigo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tienda.usuarios SET nombresCompletos=%s, numeroCelular=%s , cuenta=%s  WHERE Codigo=%s",
                       (nombresCompletos, numeroCelular, cuenta, Codigo))
    conexion.commit()
    conexion.close()


def edit_suma(numeroCelular):
    conecxion = obtener_conexion()
    usuarios = []
    with conecxion.cursor() as cursor:
        cursor.execute(
            'SELECT   u.Codigo,u.nombresCompletos,u.numeroCelular,u.cuenta FROM tienda.usuarios as u WHERE u.numeroCelular=%s', (numeroCelular,))
        usuarios = cursor.fetchone()
    conecxion.commit()
    conecxion.close()
    return usuarios


def guardarSuma(cuenta, numeroCelular):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'UPDATE  tienda.usuarios SET cuenta=%s WHERE numeroCelular=%s', (cuenta, numeroCelular))
    conexion.commit()
    conexion.close()


def eliminar(numeroCelular):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'DELETE from usuarios Where numeroCelular=%s', (numeroCelular))
    conexion.commit()
    conexion.close()
