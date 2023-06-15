import re


class Animal:
    def __init__(self, especie, tipo_do_animal, idade, porte, peculiaridade, encontrado_por, contato):
        self.especie = especie
        self.tipo_do_animal = tipo_do_animal
        self.idade = idade
        self.porte = porte
        self.peculiaridade = peculiaridade
        self.encontrado_por = encontrado_por
        self.contato = contato

    def __str__(self):
        return f'Espécie: {self.especie}\nTipo do animal: {self.tipo_do_animal}\n Idade: {self.idade}\n Porte: {self.porte}\n Peculiaridade: {self.peculiaridade}\n Encontrado por: {self.encontrado_por}\n Contato: {self.contato}'


animais = []


def valida_especie(especie):
    if len(especie) < 3:
        return False

    vogais = set('aeiou')
    if not any(char in vogais for char in especie):
        return False

    for char in especie:
        if especie.count(char) > 2:
            return False

    return True


def valida_idade(idade):
    if not idade.isdigit():
        return False

    if int(idade) > 100:
        return False

    return True


def valida_encontro(encontrado_por):
    if len(encontrado_por) < 3:
        return False

    vogais = set('aeiou')
    if not any(char in vogais for char in encontrado_por):
        return False

    for char in encontrado_por:
        if encontrado_por.count(char) > 2:
            return False

    return True


def valida_contato(contato):
    if not re.match(r'^\d{10,11}$', contato) and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', contato):
        return False

    return True


def cadastrar_animal():
    while True:
        especie = input("Espécie do animal: ")
        while not valida_especie(especie):
            print(
                "Por favor, insira uma espécie válida.")
            especie = input("Espécie do animal: ")

        tipo_do_animal = input("Escolha o tipo do animal: ").lower()

        idade = input("Idade do animal: ")
        while not valida_idade(idade):
            print("Por favor, insira uma idade válida.")
            idade = input("Idade do animal: ")

        porte = input("Porte do animal (p, m ou g): ")
        while porte.lower() not in ["p", "m", "g"]:
            print("Por favor, insira um porte válido.")
            porte = input("Porte do animal (p, m ou g): ")

        peculiaridade = input("Peculiaridade do animal: ")

        encontrado_por = input("Quem encontrou o animal: ")
        while not valida_encontro(encontrado_por):
            print("Por favor, digite o nome completo.")
            encontrado_por = input("Quem encontrou o animal: ")

        contato = input("Contato da pessoa que entregou o animal: ")
        while not valida_contato(contato):
            print("Por favor, insira telefone ou e-mail.")
            contato = input("Contato da pessoa que entregou o animal: ")

        animal = Animal(especie, tipo_do_animal, idade, porte, peculiaridade, encontrado_por, contato)
        animais.append(animal)

        continuar = input("Deseja adicionar outro animal? (s/n): ")
        while continuar.lower() not in ["s", "n"]:
            print("Por favor, insira 's' para adicionar outro animal ou 'n' para sair.")
            continuar = input("Deseja adicionar outro animal? (s/n): ")

        if continuar.lower() == "n":
            break


def listar_animais():
    for animal in animais:
        print(animal)
        print("-" * 50)


def pesquisar_animais_por_caracteristicas():
    animais.sort(key=lambda x: (x.especie, x.porte, x.peculiaridade))

    especie = input("Espécie do animal: ")
    while not valida_especie(especie):
        print(
            "Por favor, insira uma espécie válida.")
        especie = input("Espécie do animal: ")
    
    porte = input("Porte do animal (p, m ou g): ")
    while porte.lower() not in ["p", "m", "g"]:
        print("Por favor, insira um porte válido.")
        porte = input("Porte do animal (p, m ou g): ")

    peculiaridade = input("Peculiaridade do animal: ")

    left = 0
    right = len(animais) - 1
    encontrou_animal = False
    contador_animais = 0

    while left <= right:
        mid = (left + right) // 2
        animal = animais[mid]

        if (animal.especie == especie and
                animal.porte == porte and
                animal.peculiaridade == peculiaridade):
            encontrou_animal = True
            contador_animais += 1
            print(animal)
            print("-" * 50)

        if (animal.especie < especie or
                (animal.especie == especie and animal.porte < porte) or
                (animal.especie == especie and animal.porte == porte and animal.peculiaridade < peculiaridade)):

            left = mid + 1

        else:
            right = mid - 1

    if encontrou_animal:
        print(f"Total de animais encontrados: {contador_animais}")

    else:
        print("Nenhum animal encontrado.")