from pymongo import MongoClient

nome = input("Digite o nome: ")
email = input("Insira o e-mail:  ")

## CONEXAO
client = MongoClient('localhost')
db = client['']

## INSERT
fila = {"servico": "Intranet", "status": 0}
id = db.fila.insert(fila)

def nome (nome):
    return nome

def email (email):
    return email

valor = int(input())
print("Escolha a opção desejada: \r\n"
      "1 - Cadastro nome"
      "2 - E-mail "
      "3 -  "
      "4 - subtração "
      )

if valor == 1:
    print(nome(nome))

elif valor == 2:
    print(email(email))
