
import psycopg2
menu = """
[MENU]

1) Inserir
2) Alterar
3) Atualizar
4) Deletar

Insira uma opção: """

con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
cur = con.cursor()

while True:

    opcao = int(input(menu))

    if opcao == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")

        try:
            cur.execute("INSERT INTO alunos(nome,email) VALUES('%s', '%s')" )
            print('Registro inserido com  sucesso')
        except Exception as e:
            print('Falha ao inserir')
            print(e)
    elif opcao == 2:

        quem = input('Qual aluno deseja alterar?: ')
        nome = input('Insira o nome: ')
        email = input('Insira o e-mail: ')

        try:
            cur.execute("UPDATE alunos SET nome='%s, email='%s WHERE aluno='%s" % (nome, email, aluno))
            print('Registro alterado com sucesso')
        except Exception as e:
            print('Falha ao alterar')


    elif opcao == 3:
        # UPDATE
        quem = input('Qual aluno deseja atualizar')
        nome = input('Atualize o nome: ')
        email = input('Atualize o email: ')

        try:
            cur.execute("UPDATE alunos SET email='gabriel@gariel' WHERE nome='gabriel'")
            print('Registros atualizados com sucesso!')
        except Exception as e:
            print('Falha ao atualizar.')

    elif opcao == 4:
        break







