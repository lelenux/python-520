alunos = [

]

banco = [
    {
        'login': 'Leandro',
        'senha': '123789'

    }
]

logado = False
menu = """
[MENU]

1) Inserir
2) Mostrar
3) Sair
Insira uma opção: """

def inserir_aluno():
    global alunos
    nome = input("Inserir o nome: ")
    email = input("Inserir o email: ")

    alunos.append(
        {
            "nome": nome,
            "email": email
        }
    )


def mostrar_aluno():
    global alunos
    aluno = input("Informe o nome do aluno: ")
    for a in alunos:

        if a ['nome'] == aluno:
            return a ['email']

def login():
    global logado, banco

    login = input('Login')
    senha = input('Digite sua senha:')



#dict = {'Usuario': ['Leandro', 'Luis', 'Angelo'], 'senha': ['123456', '123789']}
#login = input('Login:')
#senha = input('Digite sua senha')

#if login == dict['Usuario'] and senha == dict['senha']:
    print('Bem vindo ao sistema!')


    while True:
        opcao = int(input(menu))

        if opcao == 1:
            inserir_aluno()
        elif opcao == 2:
              aluno = input("Informe o nome do aluno: ")
              for a in alunos:
                if a['nome'] == aluno:
                    print(a['email'])
        elif opcao == 3:
            break
        else:
            print("Nenhuma opção válida")

else:
    print('Se fudeu!')