from agenda import *

def menu():
    while True:
        print("AGENDA - Escolha a ação desejada:")
        print("1- Exibir contatos.\n"
              "2- Adicionar contato\n"
              "3- Atualizar contato\n"
              "4- Excluir contato\n"
              "5- Favoritar contato\n"
              "6- Ver favoritos\n"
              "0- Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except (ValueError, TypeError):
            print("\nDigite uma opção válida!\n")
            continue

        if opcao == 1:
            listar(1)
        elif opcao == 2:
            adicionar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 5:
            favoritar()
        elif opcao == 6:
            ver_favoritos()
        elif opcao == 0:
            print("Saindo...")
            break

if __name__ == "__main__":
    menu()
