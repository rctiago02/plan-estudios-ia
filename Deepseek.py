from openai import OpenAI
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key,base_url="https://api.deepseek.com")
historial = [{"role":"system","content":""}]
def Open_IA(user_promt):
  historial.append({"role":"user","content":user_promt}) #Agregamos el formato del mensaje con el prompt del user al historial 
  chat= client.chat.completions.create(
      model= "deepseek-chat",
      messages=historial,
      stream= False,
      temperature= 0.7
  )   
  ia_response = chat.choices[0].message.content #guardamos la respuesta 
  # historial.append({"role":"assistant","content": ia_response}) #agregamos la respuesta al historial para que la IA recuerde la conversacion
  return ia_response

