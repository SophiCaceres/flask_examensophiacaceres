from flask import Flask, render_template, request

app = Flask(__name__)

# -----------------------------
# RUTA PRINCIPAL (MENÚ)
# -----------------------------
@app.route('/')
def index():
    return render_template("index.html")


# -----------------------------
# EJERCICIO 1 (COMPRA DE TARROS)
# -----------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        tarros = request.form.get('tarros')

        # Validación de campos vacíos
        if not nombre or not edad or not tarros:
            error = "Por favor, complete todos los campos."
        else:
            try:
                edad = int(edad)
                tarros = int(tarros)

                precio_sin_descuento = tarros * 9000
                descuento = 0
                texto_descuento = "0% (sin descuento)"

                # Reglas de descuento
                if 18 <= edad <= 30:
                    descuento = 0.15
                    texto_descuento = "15%"
                elif edad > 30:
                    descuento = 0.25
                    texto_descuento = "25%"

                monto_descuento = precio_sin_descuento * descuento
                total_final = precio_sin_descuento - monto_descuento

                resultado = {
                    "nombre": nombre,
                    "precio": precio_sin_descuento,
                    "texto_descuento": texto_descuento,
                    "total_final": total_final
                }

            except ValueError:
                error = "Los datos ingresados no son válidos."

    return render_template("ejercicio1.html", resultado=resultado, error=error)


# -----------------------------
# EJERCICIO 2 (LOGIN)
# -----------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')

        if usuario == "juan" and contraseña == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and contraseña == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


# -----------------------------
# EJECUCIÓN
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
