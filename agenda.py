
import  json

def salvar(contatos):
    try:
        with open('contatos.json', 'w', encoding='utf8') as file:
            json.dump(contatos, file, indent=4, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError):
        return

def listar():
    try:
        with open('contatos.json', 'r', encoding='utf8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if len(data) == 0:
        print('\nNenhum contato foi encontrado.\n')
        return
    else:
        print('\n------Contatos encontrado:-----')
        indice = 0
        for item in data:
            indice += 1
            print(f'Contato: {indice}')
            print(item.get('nome'))
            print(item.get('telefone'))
            print(item.get('email'))
            print("\n")
        print('------------------------------')
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

def atualizar():
    contatos = listar()
    contato = int(input('Digite o indice do contato desejado: '))
    c = contato-1

    if (c<0 or c>len(contatos)-1):
        print('\nNenhum contato foi encontrado.\n')
        return
    else:
        contatos[c]["nome"] = input('Digite o nome do contato: ')
        contatos[c]["telefone"] = input('Digite o telefone do contato: ')
        contatos[c]["email"] = input('Digite o email do contato: ')
    try:
        with open('contatos.json', 'w', encoding='utf8') as file:
            json.dump(contatos, file, indent=4, ensure_ascii=False)
            print(f'Contato: {contato} atualizado com sucesso.')
    except (FileNotFoundError, json.JSONDecodeError):
        return

def excluir():
    contatos = listar()
    contato = int(input("Selecione o contato que deseja excluir: "))
    if(contato<0 or contato>len(contatos)-1):
        print('\nNenhum contato foi encontrado.\n')
    else:
        indice = contato-1
        contatos.pop(indice)
        salvar(contatos)
        print(f'\nContato {contato} excluido com sucesso.')
