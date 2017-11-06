alunos = [
    {
        "Nome": "Mariana",
        "curso": ["Python"]
    },
    {
        "Nome": "João",
        "curso": ["Python", "Infra Agil"]
    }
]

curso = (input("Escolha um curso: "))

for a in alunos:
    for c in a ["curso"]:
        if c == curso:
            print(a["Nome"])




