from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('cuadrado'))
@app.route('/cuadrado', methods=['GET', 'POST'])
def cuadrado():
    area = None
    perimetro = None
    
    if request.method == 'POST':
        lado = float(request.form['lado'])
        
        # Fórmulas del cuadrado
        area = lado * lado
        perimetro = lado * 4
        
    return render_template('cuadrado.html', area=area, perimetro=perimetro)

if __name__ == '__main__':
    app.run(debug=True)