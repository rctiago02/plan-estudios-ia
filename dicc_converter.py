
from config import PREGUNTAS_AISLADAS


def lista_a_dicc(respuestas_usuario):

  dic={} 
  

  print("HOLA MUNDO")
  for pregunta in range(5):
      print(dic)
      print(respuestas_usuario)
      dic[PREGUNTAS_AISLADAS[pregunta]] = respuestas_usuario[pregunta]
      
  return dic




