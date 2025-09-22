'''1/2/3 - Crie uma classe chamada Pessoa. No "registro de nascimento" (__init__), toda pessoa deve
ter um nome e uma idade. Usando a classe Pessoa que você criou, crie dois objetos:
-Uma pessoa chamada "João", com 25 anos.
-Uma pessoa chamada "Maria", com 30 anos.
Depois de criá-los, imprima o nome e a idade de cada um para confirmar que deu certo.
Adicione um método (uma "ação") à sua classe Pessoa chamado apresentar. Esse método
deve imprimir uma frase como: "Olá, meu nome é [nome] e eu tenho [idade] anos." Chame
esse método para os objetos "João" e "Maria".
'''

class Pessoa:
    def __init__(self, nome:str , idade:int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e eu tenho {self.idade} anos.")

pessoa_1 = Pessoa("João", 25)
print("Pessoa 01")
print("Nome:", pessoa_1.nome)
print("Idade:", pessoa_1.idade)

pessoa_1.apresentar()

pessoa_2 = Pessoa("Maria", 30)
print("\nPessoa 02")
print("Nome:", pessoa_2.nome)
print("Idade:", pessoa_2.idade)

pessoa_2.apresentar()

'''4- Crie uma nova classe chamada Produto. Todo produto deve ter nome e preço. Depois, crie
duas instâncias:
1. Um "Caderno" que custa 15.50.
2. Uma "Caneta" que custa 3.00.
Imprima o nome e o preço de cada produto'''

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

produto_01 = Produto("Caderno", 15.00)
print("\nProduto 01:", produto_01.nome)
print("Preço: R$", produto_01.preco)

produto_02 = Produto("Caneta", 03.00)
print("\nProduto 02:", produto_02.nome)
print("Preço: R$", produto_02.preco)

'''5/6 - Crie uma classe ContaBancaria. Toda conta deve começar com um titular e um saldo inicial.
Crie um método depositar(valor) que some um valor ao saldo da conta. Crie um objeto,
deposite um valor e imprima o novo saldo.
Na mesma classe ContaBancaria, adicione um método para sacar(valor). Este método deve
verificar se há saldo suficiente na conta.
● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado com sucesso.".
● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o saldo.
Teste os dois cenários: um saque bem-sucedido e uma tentativa de sacar mais do que
tem.
'''

class ContaBancaria:
    def __init__(self, titular: str, saldo: float =0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor precisa ser positivo.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente!")


conta = ContaBancaria("Ana", 150.00)
print(f"\nTitular:", conta.titular)
print(f"Saldo Inicial: R$", conta.saldo)

conta.depositar(100.00)
print(f"\nTitular:", conta.titular)
print(f"Saldo Atual: R$", conta.saldo)

conta.sacar(50.00)
print(f"\nTitular:", conta.titular)
print(f"Saldo Atual: R$", conta.saldo)

'''7- Crie uma classe Retangulo que é inicializada com base e altura. Crie dois métodos:
1. calcular_area(): deve retornar o cálculo base * altura.
2. calcular_perimetro(): deve retornar o cálculo 2 * (base + altura).
Crie um retângulo, chame os dois métodos e imprima os resultados que eles retornam.
'''

class Retangulo:
    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
retangulo = Retangulo(4, 8)
print("\nBase:", retangulo.base)
print("Altura:", retangulo.altura)


print("Área:", retangulo.calcular_area())

print("Perímetro: ", retangulo.calcular_perimetro())

'''8- Crie uma classe Carro com os atributos modelo e nivel_combustivel (começando com 0).
1. Crie um método para abastecer(litros) que aumenta o nível de combustível.
2. Crie um método dirigir(distância) que consome combustível (ex: 1 litro a cada 10 km). O
método deve verificar se há combustível suficiente para a viagem. Se houver, diminua o
combustível e avise que o carro andou. Se não, avise que não há combustível.
'''

class Carro:
    def __init__(self, modelo: str, nivel_combustivel:int = 0):
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel

    def abastecer(self, litros: int):
        if litros > 0:
            self.nivel_combustivel += litros
            print(f"\nSeu carro foi abastecido com {litros} litros. E o nível atual de combustível é: {self.nivel_combustivel} litros.")
        else:
            print("Digite um valor positivo.")
    
    def dirigindo(self, distancia:int):
        if distancia <= 0:
            print("Digite um número positivo para a distância.")
            return

            # 1 litro a cada 10 km
        consumo_por_km = 1 / 10  
        combustivel_necessario = distancia * consumo_por_km

        if self.nivel_combustivel >= combustivel_necessario:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro andou {distancia} km. Combustível restante: {self.nivel_combustivel:.2f}L")
        else:
            print("Não há combustível suficiente para a viagem.")

carro = Carro("Virtus")

carro.abastecer(10)
carro.dirigindo(30)

'''9- Crie uma classe Funcionario. Cada funcionário terá nome e salário (atributos de instância).
Agora, crie um atributo de classe chamado percentual_bonus, com o valor 1.10
(representando 10% de bônus).
Crie um método aplicar_bonus que multiplica o salário do funcionário pelo percentual_bonus
da classe. Crie dois funcionários com salários diferentes, aplique o bônus e veja o resultado.
● Dica: Um atributo de classe é definido diretamente dentro da classe, fora de qualquer
método.'''

class Funcionario:
    percentual_bonus = 1.10

    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        return self.salario
    
funcionario_01 = Funcionario("Joaquim", 2500)
print("\nFuncionário: ", funcionario_01.nome)
print("Sálario: ", funcionario_01.salario)
print("Salário + Bônus: ", funcionario_01.aplicar_bonus())

funcionario_02 = Funcionario("Josefina", 5000)
print("\nFuncionário: ", funcionario_02.nome)
print("Sálario: ", funcionario_02.salario)
print("Salário + Bônus: ", funcionario_02.aplicar_bonus())

'''10- Crie duas classes: Motor e Carro.
1. A classe Motor terá um atributo potencial.
2. A classe Carro terá modelo. Ao criar um Carro, ele deve também criar um objeto Motor e
guardá-lo como um de seus atributos (ex: self.motor = Motor(100)).
Crie um método no Carro chamado exibir_potencia que imprime a potência do seu motor.'''

class Motor:
    def __init__(self, potencia:int):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo: str, motor_potencia):
        self.modelo = modelo
        self.motor = Motor(motor_potencia)

    def exibir_potencia(self):
        print(f"\nO carro {self.modelo} tem {self.motor.potencia} de potência")

carro1 = Carro("Virtus", 500)
carro1.exibir_potencia()

'''11-Crie duas classes: Livro e Biblioteca.
1. A classe Livro terá atributos título e autor.
2. A classe Biblioteca terá um atributo acervo, que começa como uma lista vazia [].
3. A Biblioteca deve ter dois métodos:
○ adicionar_livro(livro): recebe um objeto Livro e o adiciona à lista acervo.
○ listar_livros(): percorre a lista acervo e imprime o título e o autor de cada livro.
Crie uma biblioteca, crie alguns objetos Livro e adicione-os à biblioteca. Depois, liste os livros.
'''

class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, novo_livro: Livro):
        self.acervo.append(novo_livro)
        print("Adicionado a bibliotica!")

    def listar_livros(self):
        if not self.acervo:
            print("Não há livro na bibilioteca.")
        else:
            print(f"\nLista de Livros")
            for livro in self.acervo:
                print(f"{livro.titulo}, de {livro.autor}")
        

biblioteca = Biblioteca()

livro1= Livro("Cinquenta tons de cinza", "E.L.James")
livro2= Livro("Feliz Natal, Alex Cross", "James Patterson")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

'''12- Crie uma classe Filme com título, diretor e ano. Se você tentar dar print() em um objeto Filme,
o resultado não será muito útil. Para resolver isso, implemente o método especial __str__(self).
Este método deve retornar uma string formatada, como por exemplo: "Filme: 'De Volta para o
Futuro' (1985) - Diretor: Robert Zemeckis".
Depois de implementar, crie um objeto Filme e simplesmente use print(meu_filme).
● Dica: O que o método __str__ retorna (return) é o que será exibido quando o objeto for
impresso.'''

class Filme:
    def __init__(self, titulo: str, diretor: str, ano:int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"\nFilme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"
    
meu_filme = Filme("Jogos Mortais", "James Wan", 2005)
print(meu_filme)