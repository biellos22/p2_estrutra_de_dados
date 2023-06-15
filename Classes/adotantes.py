import re

class Adotante:
    def __init__(self, nome, cpf, telefone, especie_interessada, tipo_animal, porte, preferencia_animal):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.especie_interessada = especie_interessada
        self.tipo_animal = tipo_animal
        self.porte = porte
        self.preferencia_animal = preferencia_animal

    def __str__(self): # __str__ retorna uma representação em forma de string do objeto Adotante.
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nEspécie de animal interessada: {self.especie_interessada}\nTipo do animal: {self.tipo_animal}\nPorte: {self.porte}\nPreferência de animal: {self.preferencia_animal}'

# Teste para verificar funcionalidade da classe:
adotantes = []

ibama_permitido = {
    'peixe': ['guppy', 'betta', 'molly', 'espada', 'acara disco', 'tetra neon', 'corydoras', 'peixe arco iris', 'peixe gato de vidro', 'peixe anjo'],
    'anfibio': ['ra', 'sapo', 'perereca'],
    'repteis': ['jabuti', 'iguana verde', 'teiu', 'calango', 'tartaruga', 'lagartixa', 'cobra do milho'],
    'ave': ['peru', 'galinha', 'calopsita', 'periquito', 'canario', 'caturrita', 'diamante', 'mandarim', 'avestruz'],
    'mamifero': ['cachorro', 'gato', 'rato', 'porco', 'ovelha', 'jumento', 'lhama', 'hamster', 'vaca', 'coelho']
}

def cadastrar_adotante():
    while True:
        nome = input('Nome completo: ')

        while True:
            cpf = input('CPF (Somente números): ')
            cpf = re.sub(r'[^0-9]', '', cpf)
            if not cpf.isdigit() or len(cpf) != 11: # isdigit() verifica se a entrada contém somente dígitos.
                print('O CPF deve conter somente 11 dígitos numéricos.')
                continue
            else:   
                nove_digitos = cpf[:9]
                contador_regressivo = 10

                resultado1 = 0
                for numero1 in nove_digitos:  
                    resultado1 += int(numero1) * contador_regressivo
                    contador_regressivo -= 1
                numero1 = (resultado1 * 10)%11

                dez_digitos = nove_digitos + str(numero1)
                contador_regressivo2 = 11
                resultado2 = 0
                for numero2 in dez_digitos:  
                    resultado2 += int(numero2) * contador_regressivo2
                    contador_regressivo2 -= 1
                numero2 = (resultado2 * 10)%11

                novo_cpf = f'{nove_digitos}{numero1}{numero2}'

                if cpf == novo_cpf:
                    break
                else:
                    print('CPF inválido')
                    continue

        while True:
            telefone = input('Telefone (Somente números com DDD): ')
            if not telefone.isdigit() or len(telefone) not in [10, 11]: # isdigit() verifica se a entrada contém somente dígitos.
                print('O telefone deve conter 10 dígitos numéricos se fixo ou 11 dígitos numéricos se celular.')
                continue
            break

        while True:
            especie_interessada= input('Escolha a espécie (peixe, anfibio, reptil, ave ou mamifero): ').lower()
            tipo_animal = input('Escolha o tipo do animal: ').lower()

            if especie_interessada in ibama_permitido:
                especie_interessada = especie_interessada
                if tipo_animal in ibama_permitido[especie_interessada]:
                    print('Aprovado! O animal pode ser adotado.')
                    break
                else:
                    print('O tipo de animal escolhido não é válido para a espécie selecionada.')
            else:
                print('A espécie selecionada não é válida.')

        while True:
            porte = input('Porte do animal (p, m ou g): ')
            if porte.lower() not in ['p', 'm', 'g']:
                print('Por favor, insira um porte válido (p, m ou g).')
                continue
            break 

        preferencia_animal = input('Preferência: ')

        adotante = Adotante(nome, cpf, telefone, especie_interessada, tipo_animal, porte, preferencia_animal)
        adotantes.append(adotante)

        continuar = input('Deseja adicionar outro adotante? (s/n): ')
        if continuar.lower() != 's':
            break

def listar_adotantes():
    for adotante in adotantes:
        print(adotante)
        print('-' * 50)
