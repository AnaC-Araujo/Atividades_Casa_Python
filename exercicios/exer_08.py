'''Peça a nota de um aluno (float).
● Use if-elif-else para atribuir um conceito:
○ = 9.0: Conceito A
○ = 7.0: Conceito B
○ = 5.0: Conceito C
○ < 5.0: Conceito D'''
nota = float(input("Digite sua nota: "))
if nota >= 9.0:
    print("Conceito A")
elif nota >= 7.0:
    print("Conceito B")
elif nota >= 5.0:
    print("Conceito C")
else:
    print("Conceito D")