from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = ''
    estado = ''

    if request.method == 'POST':
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = round((nota1 + nota2 + nota3) / 3, 1)

            if asistencia >= 75 and promedio >= 40:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        resultado = ''
        resultado2 = ''

        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        len_nombre1 = len(nombre1)
        len_nombre2 = len(nombre2)
        len_nombre3 = len(nombre3)

        if len_nombre1 >= len_nombre2 and len_nombre1 >= len_nombre3:
            resultado = f"El nombre más largo es : {nombre1}"
            resultado2 = f"El nombre tiene : {len_nombre1} caracteres"
        elif len_nombre2 >= len_nombre1 and len_nombre2 >= len_nombre3:
            resultado = f"El nombre más largo es : {nombre2}"
            resultado2 = f"El nombre tiene : {len_nombre2} caracteres"
        else:
            resultado = f"El nombre más largo es : {nombre3}"
            resultado2 = f"El nombre tiene : {len_nombre3} caracteres"
        return render_template('ejercicio2.html', resultado=resultado, resultado2=resultado2)
    return render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run(debug=True)
