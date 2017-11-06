import psycopg2

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")

    cur = con.cursor()

    #INSERT
    cur.execute("INSERT INTO alunos(nome,email) VALUES('lelenux', 'lelenu@gmail.com')")

    #UPDATE
    cur.execute("UPDATE alunos SET email='gabriel@gariel' WHERE nome='gabriel'")

    ##DELETE
   # cur.execute("DELETE FROM alunos WHERE nome='mariana'")

    con.commit()
except Exception as e:
    con.rollback()
    cur.close()
    con.close()

##SELECT

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
    cur = con.cursor()

    ###SELECIONA MAIS DE UM
    cur.execute("SELECT * FROM alunos")
    registros = cur.fetchall()

    print(registros)

    ###SELECIONA APENAS UM
    cur.execute("SELECT * FROM alunos WHERE nome='gabriel'")
    registro = cur.fetchone()

    print(registro)

except Exception as e:
    con.rollback()
    cur.close()
    con.close()

#### MOSTRAR TODOS ENCONTRADOS

for r in registros:
    print('id', r[0])
    print('nome', r[1])
    print('Email: ', r[2])

#### MOSTRAR APENAS O PRIMEIRO

    print('id', registro[0])
    print('nome', registro[1])
    print('Email: ', registro[2])

