from Deepseek import Open_IA
contador = 3
while contador > 0 :
 prompt = input("")
 response,tokens,historial= Open_IA(prompt)
 contador-= 1

print(tokens)
print(response)
print(historial)