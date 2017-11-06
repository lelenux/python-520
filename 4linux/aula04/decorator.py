alunos = [

]

menu = """
[MENU]

1) Inserir
2) Mostrar
3) Sair
Insira uma opção: """

def is_logged(*args):
    def func():
        if logado:
            return args[0]()
        else:
            return print('Permissão negada!')
    return func


@is_logged # o @ significa que é um decorator
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

        if a['nome'] == aluno:
            return a['email']




dict = {'Usuario': ['Leandro', 'Luis', 'Angelo'], 'senha': ['123456', '123789']}
login = input('Login:')
senha = input('Digite sua senha')

if login == dict['Usuario'] and senha == dict['senha']:
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