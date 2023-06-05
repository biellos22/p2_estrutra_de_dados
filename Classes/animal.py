class Animal:
    def __init__(self, especie, idade, porte, peculiaridade, encontrado_por, contato):
        self.especie = especie
        self.idade = idade
        self.porte = porte
        self.peculiaridade = peculiaridade
        self.encontrado_por = encontrado_por
        self.contato = contato

    def __str__(self): # A função __str__ retorna uma representação em forma de string do objeto Animal.
        return f"Espécie: {self.especie}\nIdade: {self.idade}\nPorte: {self.porte}\nPeculiaridade: {self.peculiaridade}\nEncontrado por: {self.encontrado_por}\nContato: {self.contato}"


animais = []

while True:
    especie = input("Espécie do animal: ")
    if not especie.isalpha(): # isalpha() verifica-se se a entrada contém somente letras
        print("Por favor, insira somente letras para a espécie.")
        continue

    idade = input("Idade do animal: ")
    if not idade.isdigit() or len(idade) > 3: # isdigit() verifica se a entrada contém somente dígitos.
        print("Por favor, insira somente números até 3 dígitos para a idade.")
        continue

    porte = input("Porte do animal (pequeno, médio ou grande): ")
    if porte.lower() not in ["pequeno", "médio", "grande"]:
        print("Por favor, insira um porte válido (pequeno, médio ou grande).")
        continue

    peculiaridade = input("Peculiaridade do animal (raça ou traços físicos): ")

    encontrado_por = input("Quem encontrou o animal: ")

    contato = input("Contato da pessoa que entregou o animal: ")

    animal = Animal(especie, idade, porte, peculiaridade, encontrado_por, contato)
    animais.append(animal)

    continuar = input("Deseja adicionar outro animal? (s/n): ")
    if continuar.lower() != "s":
        break

# Teste para verificar funcionalidade da classe:
#for animal in animais:
#    print(animal)
