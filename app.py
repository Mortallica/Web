from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder='templates')


actividades_list = ['Agricultura', 'Comercio','Investigación','Insumos','Transporte']

@app.route('/')
def formulario():
    return render_template('formulario.html',actividades=actividades_list)

@app.route('/lista')
def lista():
    participantes_list = requests.get('http://localhost:5000/participantes').json()
    return render_template('lista.html',participantes=participantes_list)

@app.route('/guardarparticipantes',methods=['POST'])
def guardarparticipantes():
    participantes = dict(request.values)
    participantes['estrato'] = int(participantes['estrato'])
    requests.post('http://localhost:5000/participantes',json=participantes)
    return(lista())
   # return render_template('lista.html',participantes=participantes_list)

app.run(debug = true , port =)  
