class Adotante:
    def __init__(self, nome, cpf, telefone, especie_interessada, preferencia_animal):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.especie_interessada = especie_interessada
        self.preferencia_animal = preferencia_animal

    def __str__(self): # __str__ retorna uma representação em forma de string do objeto Adotante.
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nEspécie de animal interessada: {self.especie_interessada}\nPreferência de animal: {self.preferencia_animal}"


adotantes = []

while True:
    nome = input("Nome completo: ")

    cpf = input("CPF (Somente números): ")
    if not cpf.isdigit() or len(cpf) != 11: # isdigit() verifica se a entrada contém somente dígitos.
        print("O CPF deve conter somente 11 dígitos numéricos.")
        continue

    telefone = input("Telefone (Somente números com DDD): ")
    if not telefone.isdigit() or len(telefone) not in [10, 11]: # isdigit() verifica se a entrada contém somente dígitos.
        print("O telefone deve conter 10 dígitos numéricos se fixo ou 11 dígitos numéricos se celular.")
        continue

    especie_interessada = input("Espécie de animal interessada: ")

    preferencia_animal = input("Preferência: ")

    adotante = Adotante(nome, cpf, telefone, especie_interessada, preferencia_animal)
    adotantes.append(adotante)

    continuar = input("Deseja adicionar outro adotante? (s/n): ")
    if continuar.lower() != "s":
        break

# Teste para verificar funcionalidade da classe:
#for adotante in adotantes:
#    print(adotante)
