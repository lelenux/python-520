n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

def soma (n1, n2):
    return n1 + n1

def divisao (n1, n2):
    return n1 / n2

def multi (n1, n2):
    return n1 * n2

def subtracao (n1, n2):
    return n1 - n2


print("Escolha a opção desejada: \r\n"
      "1 - Soma "
      "2 - divisao "
      "3 - multiplição "
      "4 - subtração "
      )

valor = int(input())

if valor == 1:
    print(soma(n1,n2))

elif valor == 2:
    print(divisao(n1,n2))

elif valor == 3:
    print(multi(n1,n2))

elif valor == 4:
    print(subtracao(n1,n2))

else:
    print("Você não digitou nenhuma das opção corretas! ")