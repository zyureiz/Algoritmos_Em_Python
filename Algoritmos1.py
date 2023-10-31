#1. Programa que apresenta n tela a frase: "Meu primeiro programa"
print(" \n meu primeiro programa em python")
print("\n")



#2. Programa que solicita um numero inteiro e o final apresente na tela o numero informado
num = int(input("insira um numero inteiro "))
print("o numero inteiro é", num)



#3. Programa que solicita ao usuário um número inteiro e ao final 
# apresente na tela o número informado da seguinte forma: "Foi informado o valor: X"
num = int(input("insira um numero inteiro "))
print("o numero inteiro é", num)



#4. Programa que solicita ao usuário dois números inteiros e ao final apresente na 
# tela os dois números informados da seguinte forma: "Voce informou os numeros X e Y"
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print(f"Você informou os números {num1} e {num2}")



#5. Programa que solicita ao usuário um número real e ao final apresente na tela o
# número informado formatado com duas casas decimais da seguinte forma: "Voce informou o numero X.YY"
numero_real = float(input("Digite um número real: "))
numero_formatado = "{:.2f}".format(numero_real)
print(f"Você informou o número {numero_formatado}")



#6. Programa que solicita ao usuário a temperatura em graus Celsius e ao final
# apresente a temperatura correspondente em graus Farenheit. F = Celsius * 1.8 + 32
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius * 1.8 + 32    
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f} °F")



#7. Programa que solicita ao usuário um número inteiro e um número real e ao final 
# apresente na tela os dois números informados formatando com duas casas decimais 
# somente o número real da seguinte forma: "Voce informou os numeros N e X.YY"
numero_inteiro = int(input("Digite um número inteiro: "))
numero_real = float(input("Digite um número real: "))
numero_real_formatado = "{:.2f}".format(numero_real)
print(f"Você informou os números {numero_inteiro} e {numero_real_formatado}")



#8. Programa que solicita ao usuário a primeira letra de seu nome e ao final
# apresente na tela a letra informada pelo usuário da seguinte forma: "Voce digitou w"
primeira_letra = input("Digite a primeira letra do seu nome: ")
print(f"Você digitou {primeira_letra}")



#9. Programa que solicita ao usuário o nome de sua cor preferida e ao final
# apresente na tela a cor informada pelo usuário da seguinte forma: "Voce gosta da cor AAA"
cor_preferida = input("Digite o nome de sua cor preferida: ")
print(f"Você gosta da cor {cor_preferida.upper()}")



#10. Programa que solicita ao usuário o nome de uma verdura e uma fruta de sua  
# preferencia e ao final apresente na tela as informações digitadas pelo usuário da seguinte 
# forma: "Voce gosta de AAAAAAA e BBBBBBB"
verdura = input("Digite o nome de uma verdura de sua preferência: ")
fruta = input("Digite o nome de uma fruta de sua preferência: ")

print(f"Você gosta de {verdura.upper()} e {fruta.upper()}.")



#11. Algoritmo que solicita ao usuário um número real e ao final imprima na tela o 
# numero informado e na linha de baixo o dobro deste número da seguinte forma:  
# Numero -> X  
# Dobro deste numero -> Y
numero = float(input("Digite um número real: "))
dobro = 2 * numero

print(f'Número -> {numero}')
print(f'Dobro deste número -> {dobro}')



#12. Programa anterior anterior reescrito apresentando o quadrado e o cubo do número informado
numero = float(input("Digite um número real: "))

quadrado = numero ** 2
cubo = numero ** 3

print(f'Número -> {numero}')
print(f'Quadrado deste número -> {quadrado}')
print(f'Cubo deste número -> {cubo}')



#13. Programa que solicita ao usuário dois números inteiros e ao final apresente 
# na tela a soma dos dois números informados da seguinte forma: "O numeros N e X 
# somados correspondem a Y"
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

soma = numero1 + numero2

print(f'O números {numero1} e {numero2} somados correspondem a {soma}')



#14. Programa que solicita ao usuário dois números reais e ao final apresente na 
# tela o produto dos dois números informados da seguinte forma: "O produto dos numeros N 
# e X corresponde a Y"
numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))

produto = numero1 * numero2

print(f'O produto dos números {numero1} e {numero2} corresponde a {produto}')



#15. Programa anterior refeito realizando as quatro operações aritméticas básicas
numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Não é possível dividir por zero."

print(f'A soma dos números {numero1} e {numero2} é {soma}')
print(f'A subtração dos números {numero1} e {numero2} é {subtracao}')
print(f'A multiplicação dos números {numero1} e {numero2} é {multiplicacao}')
print(f'A divisão dos números {numero1} e {numero2} é {divisao}')