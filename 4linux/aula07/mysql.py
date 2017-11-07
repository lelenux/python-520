import MySQLdb

try:

    con = MySQLdb.connect(
        host="localhost",
        user="admin",
        passwd="4linux",
        db="projetos"
    )

    cur = con.cursor()

    #INSERT
    cur.execute("INSERT INTO clientes(nome,endereco) VALUES('lelenux', 'lelenu@gmail.com')")

    #UPDATE
    cur.execute("UPDATE clientes SET endereco='gabriel@gariel' WHERE nome='gabriel'")

    ##DELETE
    # cur.execute("DELETE FROM clientes WHERE endereco='mariana'")

    con.commit()

except Exception as e:
    print(e)
    cur.rollback()
    con.close()
    ##SELECT



