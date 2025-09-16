'''Crie um programa que recebe uma frase do usuário e faz uma análise completa sobre ela,
mostrando:
● A quantidade de palavras na frase.
● A quantidade de vogais (a, e, i, o, u).
● A quantidade de consoantes.
● Se a frase é um palíndromo (ou seja, se ela pode ser lida da mesma forma de trás para
frente, ignorando espaços e letras maiúsculas).
'''

frase = input("Digite sua frase: ").strip().lower()

def contador_de_palavras(frase: str) -> int:
    '''Contar a quantidade de palavras na frase'''
    return len(frase.split())

def contador_de_vogais(frase: str) -> int:
    '''Contar quantas vogais há na frase'''
    vogais = "aeiou"
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

def contador_de_consoantes(frase: str) -> int:
    '''Contar quantas consoantes há na frase'''
    vogais = "aeiou"
    contador = 0
    for letra in frase:
        if letra.isalpha() and letra not in vogais:
            contador += 1
    return contador

def verificacao_palindromo (frase: str) -> bool:
    '''Verificar se a frase é um palíndromo'''
    retirando_espaco = ""
    for letra in frase:
        if letra != " ":
            retirando_espaco += letra
    return retirando_espaco == retirando_espaco[::-1]

print("--- Resumo da Análise ---")
print(f"Sua frase é: '{frase}'")
print(f"Há {contador_de_palavras(frase)} palavras na frase.")
print(f"Há {contador_de_vogais(frase)} vogais na frase.")
print(f"Há {contador_de_consoantes(frase)} consoantes na frase.")
if verificacao_palindromo(frase):
    print("Sua frase é um palíndromo.")
else:
    print("Sua frase não é um palíndromo.")