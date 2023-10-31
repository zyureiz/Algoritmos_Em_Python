#1. Programa que solicita ao usuário um número real e ao final imprima na tela se o 
# número informado é maior que 10 (dez)
numero = float(input("Digite um número real: "))

if numero > 10:
    print("O número informado é maior que 10.")
else:
    print("O número informado não é maior que 10.")
    


#2. Programa que solicita ao usuário um número real e ao final imprima na tela se 
# o número informado é maior ou igual a dez ou menor que 10 (dez)
numero = float(input("Digite um número real: "))

if numero >= 10:
    print("O número informado é maior ou igual a dez.")
else: 
    print("O número informado não é maior ou igual a dez.")
    


#3. Algoritmo que solicita ao usuário um número real e ao final imprima na tela se o 
# número informado é maior que dez, se é menor que dez, ou se é igual a dez    
numero = float(input("Digite um número real: "))

if numero > 10:
    print("O número informado é maior que 10.")
elif numero < 10:
    print("O número informado é menor que 10.")
else:
    print("O número informado é igual a 10.")
    


#4. Algoritmo que solicita ao usuário um número real e ao final imprima na tela se o 
# número informado é positivo, negativo ou nulo (zero)
numero = float(input("Digite um número real: "))

if numero > 0:
    print("O número informado é positivo.")
elif numero < 0:
    print("O número informado é negativo.")
else:
    print("O número informado é nulo (zero).")
    
  
    
#.5 Algoritmo que le um número inteiro e imprima uma das mensagens: é múltiplo 
# de 3, ou, não é múltiplo de 3
numero = int(input("Digite um número inteiro: "))

if numero % 3 == 0:
    print("O número informado é múltiplo de 3.")
else:
    print("O número informado não é múltiplo de 3.")



#6. Refazer o algoritmo anterior, solicitando antes o múltiplo a ser testado    
multiplo = int(input("Digite um múltiplo para teste: "))

numero = int(input("Digite um número inteiro: "))

if numero % multiplo == 0:
    print(f"O número informado é múltiplo de {multiplo}.")
else:
    print(f"O número informado não é múltiplo de {multiplo}.")



#7. Algoritmo que classifica um número inteiro fornecido pelo usuário como 
# par ou ímpar
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número informado é par.")
else:
    print("O número informado é ímpar.")



#8. Algoritmo que le um número, e se ele for maior do que 20, imprimir a metade 
# desse número, caso contrário, imprimir o dobro do número
numero = float(input("Digite um número: "))

if numero > 20:
    metade = numero / 2
    print(f"A metade do número é: {metade}")
else:
    dobro = numero * 2
    print(f"O dobro do número é: {dobro}")
    


#9. Algoritmo que le dois números inteiros e realize a adição; caso o resultado 
# seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele
numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))

resultado =  numero1 + numero2

if resultado > 10:
    resultado_quadrado = resultado ** 2
    print(f"O quadrado do resultado é: {resultado_quadrado}")
    
else: 
    resultado_metade = resultado / 2
    print(f"O resultado é: {resultado_metade}.")
    


#10. O sistema de avaliação de determinada disciplina é composto por três provas. A primeira 
# prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Considerando que a 
# média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno 
# desta disciplina e dizer se o aluno foi aprovado ou não 
peso_prova1 = 2
peso_prova2 = 3
peso_prova3 = 5

nota_prova1 = float(input("Digite a primeira nota: "))
nota_prova2 = float(input("Digite a segunda nota: "))
nota_prova3 = float(input("Digite a terceira nota: "))

media_final = (nota_prova1 * peso_prova1 + nota_prova2 * peso_prova2 + nota_prova3 * peso_prova3) \
    / (peso_prova1 + peso_prova2 + peso_prova3)
    
if media_final >=6.0:
    print(f"A média final do aluno é {media_final:.2f}. O aluno está aprovado.")  
    
else: 
    print(f"A média final do aluno é {media_final:.2f}. O aluno está reprovado.")
    


#11. Algoritmo que le o nome e o peso de duas pessoas e imprima o nome da 
# pessoa mais pesada 
n1 = input("Digite o nome da primeira pessoa: ")
p1 = float(input("Digite o peso da primeira pessoa: "))

n2 = input("Digite o nome da segunda pessoa: ")
p2 = float(input("Digite o peso da segunda pessoa: "))

if p1 > p2:
    print(n1, "é a pessoa mais pesada.")
elif p2 > p1:
    print(n2, "é a pessoa mais pesada.")    
else:
    print("Ambas as pessoas têm o mesmo peso.")
    
 
    
#12. Algoritmo que indica se um número digitado está compreendido entre 20 e 90, ou não.
numero = int(input("Digite um número: "))

if numero >= 20 and numero <= 90:
    print("O número está compreendido entre 20 e 90.")
else:
    print("O número não está compreendido entre 20 e 90.") 
    


#13. Algoritmo que le dois números e imprima qual é maior, qual é menor, ou se são iguais.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior.")
elif numero1 < numero2:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")   
    
 
    
#14. Programa em python que solicita ao usuário a média para aprovação
# em um curso e em seguida solicita ao usuário o nome, sexo e as 03 notas do aluno e ao
# final imprima a frase: "O aluno XXXXX foi aprovado com media YY" considerando o gênero
# do(a) aluno(a) e se foi aprovado(a) ou reprovado(a) 
media_aprovacao = float(input("Digite a média para aprovação no curso: "))

nome = input("Digite o nome do aluno: ")
genero = input("Digite o sexo do aluno (masculino ou feminino): ")

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media_aluno = (nota1 + nota2 + nota3) / 3

if media_aluno >= media_aprovacao:
    status = "aprovado"
else:
    status = "reprovado"

if genero == "masculino":
    print(f"O aluno {nome} foi {status} com média {media_aluno:.2f}")
elif genero == "feminino":
    print(f"A aluna {nome} foi {status} com média {media_aluno:.2f}")
else:
    print(f"O aluno/aluna {nome} foi {status} com média {media_aluno:.2f}")