n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

def nota (n1,n2):
    nota = n1 + n2
    if nota >= 7:
        print("Você passou de ano!")
    else:
        print("Sua nota foi %s, então você foi reprovado!" % (nota))

print(nota(n1,n2))

