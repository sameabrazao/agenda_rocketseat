
import  json

def salvar(contatos):
    try:
        with open('contatos.json', 'w', encoding='utf8') as file:
            json.dump(contatos, file, indent=4, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return

def listar(tipo):
    try:
        with open('contatos.json', 'r', encoding='utf8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if len(data) == 0:
        print('\nNenhum contato foi encontrado.\n')
        return
    else:
        if tipo == 1:
            print('\n------Contatos encontrados:-----')
            indice = 0
            for item in data:
                indice += 1
                print(f'Contato: {indice}')
                print(item.get('nome'))
                print(item.get('telefone'))
                print(item.get('email'))
                fav = item.get('favorito')
                if fav == '*':
                    print(f'Favorito: {fav}')
                print("\n")
            print('------------------------------')
        else:
            nfav = 0
            print('\n--------Contatos favoritos:--------')
            indice = 0
            for item in data:
                indice += 1
                fav = item.get('favorito')
                if fav == '*':
                    print(f'Contato: {indice}')
                    print(item.get('nome'))
                    print(item.get('telefone'))
                    print(item.get('email'))
                    print(f'Favorito: {fav}')
                    nfav += 1
                    print("\n")
            if nfav == 0:
                print(f'Nenhum contato favorito encontrado.\n')
            print('-----------------------------------\n')

    return data

def adicionar():
    nome = input('\nDigite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')

    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }

    try:
        with open('contatos.json', 'r', encoding='utf8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(novo_contato)
    salvar(data)
    print('\nContato adicionado com sucesso!\n')
    return novo_contato

def atualizar():
    contatos = listar(1)
    if not contatos:
        return
    try:
        contato = int(input('Digite o indice do contato desejado: '))
    except (ValueError, TypeError):
        print("Valor inválido. Retornando ao menu principal.\n")
        return
    c = contato-1

    if c<0 or c>=len(contatos):
        print('\nNenhum contato foi encontrado.\n')
        return
    else:
        contatos[c]["nome"] = input('Digite o nome do contato: ')
        contatos[c]["telefone"] = input('Digite o telefone do contato: ')
        contatos[c]["email"] = input('Digite o email do contato: ')

    salvar(contatos)
    print(f'Contato: {contato} atualizado com sucesso.')
    return contatos


def excluir():
    contatos = listar(1)
    if not contatos:
        return
    try:
        contato = int(input("Selecione o contato que deseja excluir: "))
    except (ValueError, TypeError):
        print("Valor inválido. Retornando ao menu principal.\n")
        return
    c = contato - 1
    if c<0 or c>=len(contatos):
        print('\nValor inválido. Retornando ao menu principal.\n')
    else:
        indice = contato-1
        contatos.pop(indice)
        salvar(contatos)
        print(f'\nContato {contato} excluido com sucesso.\n')


def favoritar():
    contatos = listar(1)
    if not contatos:
        return
    try:
        contato = int(input('Digite o indice do contato que deseja favoritar: '))
    except (ValueError, TypeError):
        print("Valor inválido. Retornando ao menu principal.\n")
        return

    c = contato-1

    if c<0 or c>=len(contatos):
        print("Valor inválido. Retornando ao menu principal.\n")
        return
    else:
        contatos[c]["favorito"] = '*'

    salvar(contatos)
    print(f'Contato: {contato} favoritado com sucesso.')

def ver_favoritos():
    listar(0)

