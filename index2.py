# Define as variaveis
n = int(input("Digite o número de termos que deseja: "))
a = 0
b = 1
n2 = False #Variavel que mostra se o valor faz ou não parte da sequencia

# Cria a sequência de Fibonacci e analisa se algum numero faz parte
for i in range(n):
        if a == n:
            n2 = True

        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Mostra se o valor pertence a sequencia
if n2 == True:
    print("O numero que você digitou pertence a sequencia de Fibonacci")
elif n2 == False:
    print("O numero que você digitou não pertence a sequencia de Fibonacci")

