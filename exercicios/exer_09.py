'''Peça a idade e se o usuário tem CNH (True ou False).
● Use if-elif-else com operadores lógicos (and e or) para:
○ Se for maior de 18 e tiver CNH: "Pode dirigir."
○ Se for maior de 18 e não tiver CNH: "Precisa tirar a CNH."
○ Se for menor de 18: "Não pode dirigir."'''
idade = int(input("Qual é sua idade? "))
cnh = input("Você possui CNH? (sim ou nao): ").lower()
if cnh == "sim":
    cnh = True
else:
    cnh = False

if idade > 18 and cnh == True:
    print("Você pode dirigir!")
elif idade > 18 and cnh == False:
    print("Você precisa tirar CNH!")
else:
    print("Não pode dirigir!")