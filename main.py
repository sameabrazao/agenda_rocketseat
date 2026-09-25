from agenda import *

def menu():
    while True:
        print("AGENDA - Escolha a ação desejada:")
        print("1- Exibir contatos.\n"
              "2- Adicionar contato\n"
              "3- Atualizar contato\n"
              "4- Excluir contato\n"
              "0- Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            listar()
        elif opcao == 2:
            adicionar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 0:
            print("Saindo...")
            break

if __name__ == "__main__":
    menu()
