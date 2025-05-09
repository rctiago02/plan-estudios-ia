

from flask import Flask, render_template, request, redirect, url_for
from dicc_converter import lista_a_dicc
from config import PREGUNTAS_AISLADAS , RESPUESTAS_DIC
from Deepseek import Open_IA
import re
dic = {}
plan_estudio = ""
def funcion_ruta2(dic):  
    
    
    if request.method == "POST":
      for i in range(len(PREGUNTAS_AISLADAS)):
          respuesta = request.form.get(f"respuesta{i}")
          dic[PREGUNTAS_AISLADAS[i]] = respuesta
    return dic



    

promp_default = "generas 5 preguntas simple sobre python(solo preguntas) para evaluar el nivel"
preguntas_ia = Open_IA(promp_default)
PREGUNTAS_AISLADAS = re.findall(r"\d+[.] (.+)",preguntas_ia)


app= Flask(__name__)  


@app.route("/") 
def index():

    return render_template("parte1.html")


@app.route("/parte2",methods = ["GET","POST"])
def contacto():
    global plan_estudio
    if request.method == "POST":
        funcion_ruta2(dic)
        print("Diccionario final:", dic)
        prompt_estudios = f"lee {dic}, analiza y formula un plan de estudios para mejorar en el area. Solamente escribeme el plan de estudio"
        plan_estudio = Open_IA(prompt_estudios)
        return redirect(url_for('part3'))


    return render_template("parte2.html",PREGUNTAS_AISLADAS=PREGUNTAS_AISLADAS)


@app.route("/parte3")
def part3():
    print(plan_estudio)
    return render_template("parte3.html", respuestas=dic, plan=plan_estudio)













if __name__ == "__main__":
    app.run(debug=True)
