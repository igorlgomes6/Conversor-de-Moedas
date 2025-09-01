def mostrar(resultado, nome, moeda):
    if resultado == int(resultado):
        print(f"{nome}: {int(resultado)} {moeda}")
    else:
        print(f"{nome}: {resultado} {moeda}")


valor = float(input("Valor em BRL: "))
cot_USD = float(input("Cotação do Dólar: "))
cot_EUR = float(input("Cotação do Euro: "))

resultadoUSD = valor * cot_USD
resultadoEUR = valor * cot_EUR

# Solicita o valor em reais ao usuário
valor = float(input("Valor em BRL: "))
# Solicita a cotação do dólar
cot_USD = float(input("Cotação do Dólar: "))
# Solicita a cotação do euro
cot_EUR = float(input("Cotação do Euro: "))

# Calcula o valor convertido para dólar e euro
resultadoUSD = valor * cot_USD
resultadoEUR = valor * cot_EUR

# Exibe o valor em dólar, sem casas decimais se for inteiro
mostrar(resultadoUSD, "Valor em Dólares", "USD")

# Exibe o valor em euro, sem casas decimais se for inteiro
mostrar(resultadoEUR, "Valor em Euros", "EUR")