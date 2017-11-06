from pymongo import MongoClient

## CONEXAO
client = MongoClient('localhost')
db = client['dexterops']

menu = """Escolha a opção desejada:
1) - INSERIR
2) - MOSTRAR
3) - SAIR
"""

while True:

    opcao = int(input(menu))

    if opcao == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")

        aluno = {"nome": nome, "email": email}
        if db.alunos.insert(aluno):
            print('Inserido com sucesso')
        else:
            print('Falha ao inserir')
    elif opcao == 2:
        email = input("Digite o email: ")
        aluno = db.alunos.find({"email": email})

        for a in aluno:
            print(a['nome'])
    elif  opcao == 3:
        pass

    elif opcao == 4:
        exit(0)