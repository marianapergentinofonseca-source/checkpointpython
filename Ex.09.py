# 9. Conversão de temperatura
# Peça ao usuário uma temperatura em graus Celsius e mostre se está:
# Abaixo de 0 → “Congelante”
# Entre 0 e 30 → “Agradável”
# Acima de 30 → “Quente”

temperatura = float(input("digite aqui uma temperatudora em graus celcius: "))
if temperatura<0:
    print("congelante")
elif temperatura>=0 and temperatura<30:
    print("agradável")
else:
    print("quente")