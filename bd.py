import pymysql


def obtener_conexion():
    return pymysql.Connect(host='localhost',
                           user='root',
                           passwd='',
                           db='tienda')
