from openai import OpenAI
client = OpenAI(api_key="sk-9568b9d96bcd4c9a8818a7752038f8b8",base_url="https://api.deepseek.com")
historial = [{"role":"system","content":"eres un experto el python y me generas 5 preguntas que permitan determinar el nivel ya sea principiante,intermedio o avanzado de una persona"}]
def Open_IA():
  #historial.append({"role":"user","content":user_promt}) #Agregamos el formato del mensaje con el prompt del user al historial 

  chat= client.chat.completions.create(
      model= "deepseek-chat",
      messages=historial,
      stream= False
  )   
  ia_response = chat.choices[0].message.content #guardamos la respuesta 
  historial.append({"role":"assistant","content": ia_response}) #agregamos la respuesta al historial para que la IA recuerde la conversacion
  return ia_response,chat.usage.total_tokens