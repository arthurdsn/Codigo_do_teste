#Define Variaveis
indice = int(13) 
soma = int(0) 
k = int(0) 

#Escreve o valor das variavies
print("O valor do indice é: ",indice) 
print("O valor da soma é: ",soma) 
print("O valor de K é: ",k) 

while k < indice: #Execulta um looping enquanto o valor de K for menor que o indice
    k = k + 1
    soma = soma + k 
    print("K vale: ",k) #Escreve o valor de K
    print("O valor da soma é:",soma) #Escreve o valor da SOMA
if k == indice: #Condição se K for igual a indice
    print("Agora o valor de K possui o mesmo valor do indice")
elif k > indice: #Condição se K for maior que indice
    print("Agora o valor de K é maior do indice")

print("O valor final da Soma será: ",soma)

