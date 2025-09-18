# 8. Par ou múltiplo de 5
# Solicite um número inteiro e verifique:
# Se ele é par, escreva “Par”.
# Senão, se for múltiplo de 5, escreva “Múltiplo de 5”.
# Caso contrário, escreva “Outro número”.

numero = int(input("digite aqui um numero inteiro: "))
print(f"voce digitou o numero: {numero}")

if numero %2 ==0:
    print("o número é par")
elif numero  %5 ==0:
    print("multiplo de 5 ")
else:
    print("outro numero")