'''Peça ao usuário um número inteiro.
● Verifique se o número é divisível por 5 (use o operador %).
● Se for, imprima "O número é divisível por 5".'''

numero = int(input("Digite um número inteiro: "))
if numero % 5 == 0:
    print(f"O número '{numero}' é divisível por 5.")
else:
    print(f"O número '{numero}' não é divisível por 5.")