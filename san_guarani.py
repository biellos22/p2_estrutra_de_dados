from Classes.adotantes import *
from Classes.animal import *

def gerar_relatorio():
    if not adotantes:
        print("Nenhum adotante cadastrado.")
        return

    if not animais:
        print("Nenhum animal cadastrado.")
        return

    encontrou_adotante = False
    for adotante in adotantes:
        encontrou_animal = False
        for animal in animais:
            if (animal.especie == adotante.especie_interessada
                and animal.porte == adotante.porte
                and animal.peculiaridade == adotante.preferencia_animal):
                encontrou_adotante = True
                encontrou_animal = True
                print(f"Adotante: {adotante.nome}")
                print(f'Espécie interessada: {adotante.especie_interessada}')
                print(f'Porte: {adotante.porte}')
                print(f'Preferencia do animal: {adotante.preferencia_animal}')
                print(' ')
                print("Animais disponíveis:")
                print("Espécie:", animal.especie)
                print("Idade:", animal.idade)
                print("Porte:", animal.porte)
                print("Peculiaridade:", animal.peculiaridade)
                print("Encontrado por:", animal.encontrado_por)
                print("Contato:", animal.contato)
                print("-" * 50)
                break  

        if not encontrou_animal:
            print(f"Nenhum animal disponível para o adotante {adotante.nome}.")
            print("-" * 50)

    if not encontrou_adotante:
        print("Nenhum adotante encontrado para os animais cadastrados.")


def menu():
    print("\n~ Seja bem-vindo ao Santuário Guarani ~")
    print("      ===== MENU =====")
    print("      1. Cadastrar animal")
    print("      2. Cadastrar adotante")
    print("      3. Listar adotantes")
    print("      4. Listar animais")
    print("      5. Gerar relatório de cruzamento")
    print("      6. Pesquisar animais por características")
    print("      7. Sair")
    print("-" * 50)

    opcao = input("Escolha uma opção: ")
    print("-" * 50)

    if opcao == "1":
        cadastrar_animal()
    elif opcao == "2":
        cadastrar_adotante()
    elif opcao == "3":
        listar_adotantes()
    elif opcao == "4":
        listar_animais()
    elif opcao == "5":
        gerar_relatorio()
    elif opcao == "6":
        pesquisar_animais_por_caracteristicas()
    elif opcao == "7":
        return
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    menu()
menu()