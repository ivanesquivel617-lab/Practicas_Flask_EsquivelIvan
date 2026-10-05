from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# 6. Cambiar el nombre del proyecto y el encabezado principal (Ruta raíz)
@app.route('/')
def inicio():
    return redirect(url_for('suma'))

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        # 4. Mostrar el resultado con dos decimales
        resultado = round(numero1 + numero2, 2)

    return render_template('suma.html', resultado=resultado)

@app.route('/resta', methods=['GET', 'POST'])
def resta():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        # 4. Mostrar el resultado con dos decimales
        resultado = round(numero1 - numero2, 2)

    return render_template('resta.html', resultado=resultado)

@app.route('/multiplicacion', methods=['GET', 'POST'])
def multiplicacion():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        # 4. Mostrar el resultado con dos decimales
        resultado = round(numero1 * numero2, 2)
        
    return render_template('multiplicacion.html', resultado=resultado)

@app.route('/division', methods=['GET', 'POST'])
def division():
    resultado = None
    error = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        
        if numero2 == 0:
            error = 'No es posible dividir entre cero.'
        else:
            # 4. Mostrar el resultado con dos decimales
            resultado = round(numero1 / numero2, 2)
        
    return render_template('division.html', resultado=resultado, error=error)

# 5. Agregar una quinta ruta opcional que calcule el residuo de una división (%)
@app.route('/residuo', methods=['GET', 'POST'])
def residuo():
    resultado = None
    error = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        
        if numero2 == 0:
            error = 'No es posible calcular el residuo si el divisor es cero.'
        else:
            # 4. Mostrar el resultado con dos decimales
            resultado = round(numero1 % numero2, 2)
        
    return render_template('residuo.html', resultado=resultado, error=error)
                
if __name__ == '__main__':
    app.run(debug=True)
