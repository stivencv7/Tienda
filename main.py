
from flask import Flask, render_template, url_for, flash, get_flashed_messages, redirect, request
from flask.templating import render_template_string


from controladores.controlador_tienda import eliminar, listaUsuario, Agregar_usario, buscar, actualizar, edit, edit_suma, guardarSuma


app = Flask(__name__)

app.secret_key = "flash message"


@app.route("/")
def inicio():

    usuarios = listaUsuario()
    return render_template("index.html", usuarios=usuarios)


@app.route("/agregar_usuario")
def agregar_usuario():
    return render_template("agregarUsuario.html")


@app.route("/guardar_usuario", methods=['POST'])
def guardar_usuario():

    nombresCompletos = request.form['nombre']
    numeroCelular = request.form['numeroCelular']
    cuenta = request.form['cuenta']
    usuarios = listaUsuario()
    usua = []
    if len(nombresCompletos) == 0 or len(numeroCelular) == 0 or len(cuenta) == 0:
        flash('Favor llene los espacios.....', 'info')
        return redirect("/agregar_usuario")
    try:
        for u in usuarios:
            print(u[2])
            usua.append(u[2])
        if numeroCelular in usua:

            flash('numero de celular ya existente.....', 'info')
            print("este numero ya existe")
            return redirect("/agregar_usuario")

        else:
            Agregar_usario(nombresCompletos, numeroCelular, cuenta)
            return redirect("/")

    except Exception as x:

        print("numero existente", x)
        return redirect("/agregar_usuario")


@app.route("/encontre")
def encontre():
    numeroCelular = request.form['numeroCelular']
    usuario = buscar(numeroCelular)
    render_template("encontrar.html", usuario=usuario)


@app.route("/busqueda ", methods=['POST'])
def busqueda():

    numeroCelular = request.form['numeroCelular']
    usuario = buscar(numeroCelular)

    if(len(usuario) == 0):

        flash('usuario no existe.....', 'info')
        return redirect("/")

    elif(usuario == usuario):
        print(".|.")
        return render_template("encontrar.html", usuario=usuario)


@app.route("/edictar/<int:numeroCelular>")
def edictar(numeroCelular):
    atender = edit(numeroCelular)
    print("usuarios para actualizar=", atender)

    return render_template("formulario_editar.html", atender=atender)


@app.route("/actualizarUsuario", methods=['POST'])
def actualizarUsuario():
    Codigo = request.form["Codigo"]
    nombresCompletos = request.form["nombresCompletos"]
    numeroCelular = request.form["numeroCelular"]
    cuenta = request.form["cuenta"]

    u = actualizar(nombresCompletos, numeroCelular, cuenta, Codigo)

    print("usuario actualizado", u)
    return redirect("/")


@app.route("/sumar/<int:numeroCelular>")
def sumar(numeroCelular):
    suma = edit_suma(numeroCelular)
    return render_template("Suma.html", suma=suma)


@app.route("/sumatoria", methods=["POST"])
def sumatoria():
    numeroCelular = request.form["numeroCelular"]
    cuenta = int(request.form["cuenta"])

    lista = edit_suma(numeroCelular)
    for list in lista:

        cuenta = lista[3]+cuenta

        break
    guardarSuma(cuenta, numeroCelular)
    print(cuenta)
    return redirect("/")


@app.route("/Eliminar", methods=["POST"])
def Eliminar():
    numeroCelular = request.form["numeroCelular"]
    eliminar(numeroCelular)
    return redirect("/")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
