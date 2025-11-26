'''Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.'''

numeros = []
i = 0
while i < 3:
    numero_fornecido = input(f"Digite o {i+1}º número: ")
    if numero_fornecido.isdigit() and int(numero_fornecido) > 0:
        numero = int(numero_fornecido)
        numeros.append(numero)
        i += 1
    else:
        print("Digite um número inteiro positivo!")

lado_a = numeros[0]
lado_b = numeros[1]
lado_c = numeros[2]

soma = (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b)
diferenca = (lado_a > abs(lado_b - lado_c)) and (lado_b > abs(lado_a - lado_c)) and (lado_c > abs(lado_a - lado_b))

if soma and diferenca:
    print("Os números fornecidos podem formar um triângulo.")
else:
    print("Os números fornecidos não podem formar um triângulo.")