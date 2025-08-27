'''Peça um número ao usuário.
● Use um while para imprimir a tabuada desse número, de 1 a 10.
○ Exemplo: 5 x 1 = 5, 5 x 2 = 10, etc.'''
numero = int(input("Digite um número: "))
i = 1
print(f"*** TABUADA DO {numero} ***")
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1