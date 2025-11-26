'''Exercício 2: Calculadora de Desconto
● Peça ao usuário para digitar o preço original de um produto (float).
● Se o preço for maior que R$ 100,00, aplique um desconto de 10% e imprima o novo
preço.
● Use o operador de multiplicação (*) e subtração (-).'''

preco_original = float(input("Digite o valor do produto: "))
if preco_original > 100.00:
    print(f"O valor do produto com desconto é R$ {preco_original * 0.9}.")