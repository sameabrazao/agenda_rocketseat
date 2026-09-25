# Agenda Rocketseat

Projeto desenvolvido como desafio prático do curso de Python da Rocketseat.

## 📋 Objetivo

Criar uma agenda de contatos em Python com persistência de dados utilizando arquivos JSON.

## 🚀 Funcionalidades

- Adicionar contatos
- Listar contatos
- Atualizar contatos
- Excluir contatos

## ⭐ Funcionalidades previstas

As seguintes funcionalidades fazem parte dos requisitos do desafio, mas ainda estão em desenvolvimento:

- Marcar contatos como favoritos
- Listar apenas os contatos favoritos

## 🛠️ Tecnologias utilizadas

- Python
- Biblioteca nativa `json`

## 💾 Armazenamento de dados

Os contatos são armazenados em um arquivo JSON, permitindo a persistência das informações mesmo após o encerramento da aplicação.

### Exemplo de estrutura dos dados

```json
[
    {
        "nome": "João Silva",
        "telefone": "99999-9999",
        "email": "joao@email.com"
    }
]
