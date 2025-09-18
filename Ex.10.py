# 10. Calculadora simples
# Receba dois números inteiros e uma operação (+, -, *, /) 
# digitada pelo usuário. Use if-else para calcular e mostrar o resultado.

numero_1 = int(input("digite aqui o primeiro numero: "))
numero_2 = int(input("digite aqui o segundo numero: "))
operacao = input("digite aqui a operacao que voce deseja fazer (+, - , * , / ): ")

if operacao == "+":
    resultado_soma = numero_1 + numero_2
    print(f"o resultado da soma é {resultado_soma}")
elif operacao == "-":
    resultado_sub = numero_1 - numero_2
    print(f"o resultado da subtracao é {resultado_sub}")
elif operacao == "*":
    resultado_multi = numero_1 * numero_2
    print(f"o resultado da multiplicacao é {resultado_multi}")
elif operacao == "/":
    resultado_div = numero_1 / numero_2
    print(f"o resultado da divisao é {resultado_div}")