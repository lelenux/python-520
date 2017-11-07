lista = [
    {
        "nome": "Gabriel",
        "notas": [
            1,4,5,6
        ]
    },
    {
        "nome":  "João",
        "notas": [
            3,5,10,10
        ]
    }

]

nome = input("Qual é o nome do aluno? ")

for l in lista:                  # Neste exemplo "l" é a variavel de lista
    if l["nome"] == nome:        # Se "l" (uma linha dalista) for igual a entrada
        soma = 0                 # Variavel para criar a soma
        for n in l["notas"]:     # Neste exemplo "n" é a variavel de notas
            soma += n            # Soma para pegar as notas
        if soma / len(l["notas"]):        # média das Notas Obs: "len" conta quantas posições existem na lista
            print("Aprovado") #
        else:
            print("Aluno reprovado")