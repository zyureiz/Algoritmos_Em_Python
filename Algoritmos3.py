#1. Algoritmo que imprime na tela lado a lado o texto "Hello World!" 10 vezes.
texto = "Hello World"

for _ in range(10):
    print(texto, end=' ')
    

    
#2. Algoritmo que imprime na tela o texto "Hello World!" 10 vezes, um por linha.
texto = "Hello World"

for _ in range(10):
    print(texto)
 
 
    
#3. Algoritmo que imprime todos os números inteiros de 1 até 100 inclusive.
for numero in range(1, 101):
    print(numero)  
    
 
    
#4. Algoritmo que imprime 100 vezes o texto "1- Hello World!" com o número.
for i in range (1, 100):
    print(f"{i}- Hello World!")
    
 
    
#5. Algoritmo que imprime todos os números decrescentes de 100 até 0 inclusive.
numero = 100

while numero >= 0:
    print(numero) 
    numero -= 1 
    
 
    
#6. Algoritmo que imprime todos os números pares inteiros de 1 até 1000.
for numero in range(2, 1001, 2):
    print(numero)
    


#7. Algoritmo que imprime todos os números ímpares de 1000 até 0.
numero = 1000

while numero >= 1:
    if numero % 2 != 0:
        print(numero)
    numero -= 1
    
 
    
#8. Algoritmo que imprime a soma dos 100 primeiros números inteiros positivos.
soma = 0

for numero in range(1, 101):
    soma += numero
    
print("A soma dos 100 primeiros numeros inteiros positivos é:", soma)



#9. Algoritmo que solicita ao usuário um número inteiro que indicará a quantidade de vezes que o texto "Hello World!" será impresso na tela, um em cada linha.
quantidade = int(input("Digite a quantidade de vezes que 'Hello World!' deve ser impresso: "))

for i in range(quantidade):
    print("Hello World!")
    


#10. Algoritmo que solicita ao usuário uma palavra e um número inteiro que 
# indicará a quantidade de vezes que a palavra digitada será impressa na tela, um em cada 
# linha.
palavra = input("Digite a palavra que voce deseja imprimir: ")
quantidade = int(input("Digite a quantidade de vezes que a palavra deve ser impressa: "))

for i in range(quantidade):
    print(palavra)
 
    
    
#11. Algoritmo que le um número de entrada que indicará a quantidade de números a serem lidos. Em seguida, leia n números (conforme o valor informado anteriormente) e imprime a soma e a média aritmética dos números informados.
quantidade = int(input("Digite a quantidade de números a serem lidos: "))

soma = 0

for i in range(quantidade):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero
    
media = soma / quantidade

print(f"A soma dos números é: {soma}")
print(f"A média aritmética dos números é: {media}")



#12. Algoritmo que le um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o nome e idade de N pessoas e ao final apresentar o nome da pessoa mais velha.
n = int(input("Digite a quantidade de registros a serem lidos: "))

nome_mais_velho = ""
idade_mais_velho = -1

for i in range (n):
    nome = input(f"Digite o nome da {i + 1}º pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    
    if idade > idade_mais_velho:
        nome_mais_velho = nome
        idade_mais_velho = idade
        
print(f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velho} anos.")



#13. Algoritmo que le um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N pessoas e ao final apresentar a média de idade de ambos os gêneros catalogados.
n = int (input("Digite a quantidade de registros a serem lidos: "))

soma_idade_homens = 0
soma_idade_mulheres = 0
total_homens = 0
total_mulheres = 0

for i in range(n):
    sexo = input(f"Digite o sexo {i + 1}ª pessoa (M/F): ")
    idade = int(input("Digite a idade: "))
    
    if sexo == "M":
        soma_idade_homens += idade
        total_homens += 1
    elif sexo == "F":
        soma_idade_mulheres += idade
        total_mulheres += 1
    else:
        print("Sexo inválido. Use M para Masculino e F para femnino.")
        
media_idade_homens = soma_idade_homens / total_homens if total_homens > 0 else 0
media_idade_homens = soma_idade_mulheres / total_mulheres if total_mulheres > 0 else 0

print(f"Media de idade para homens: {media_idade_homens:.2f} anos")



#14. Algoritmo que solicita ao usuário 10 números reais e ao final apresente o maior e o menor deles.
maior_numero = None
menor_numero = None

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º numero real:"))
    
    if i == 0:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
            
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")



#15. Algoritmo que solicita N números reais e quando o usuário informar o valor nulo 0 (zero) o programa ordene e mostre todos os números informados de forma crescente. 
numeros = []

while True:
    numero = float(input("Digite um número real (0 para ordenar e sair): "))
    
    if numero == 0:
        break
    else:
        numeros.append(numero)
        
numeros.sort()

if numeros:
    print("Números em ordem crescente:")
    for numero in numeros:
        print(numero)
else:
    print("Nenhum número informado. ")
    
  
    
#16. Programa que vai solicitando as idades dos alunos da sala até que todos 
# sejam informados (perguntar ao usuário se deseja informar a idade do próximo aluno). Ao 
# final apresentar a idade do mais novo, a idade do mais velho, Quantos alunos têm mais de 18 anos, quantos alunos têm até 18 anos, a média aritmética e a mediana. 
idades = []

while True:
    idade = int(input("Informe a idade do aluno: "))
    idades.append(idade)
    
    continuar = input("Deseja informar a idade do próximo aluno? (S/N): ")
    if continuar.lower() != 's':
        break

idade_mais_novo = min(idades)
idade_mais_velho = max(idades)

alunos_mais_dezoito = sum(1 for idade in idades if idade > 18)
alunos_ate_dezoito = sum(1 for idade in idades if idade <= 18)

media = sum(idades) / len(idades)

idades.sort()

n = len(idades)
if n % 2 == 0:
    mediana = (idades[n // 2 - 1] + idades[n // 2]) / 2
else:
    mediana = idades[n // 2]
    
print(f"Idade do mais novo: {idade_mais_novo} anos")
print(f"Idade do mais velho: {idade_mais_velho} anos")
print(f"Quantidade de alunos com mais de 18 anos: {alunos_mais_dezoito}")
print(f"Quantidade de alunos com até 18 anos: {alunos_ate_dezoito}")
print(f"Média das idades: {media:.2f} anos")
print(f"Mediana das idades: {mediana} anos")   