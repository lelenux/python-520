nome = 2
idade = 151
ecivil = "t"
salario = -1
sexo =True

while nome <3:
    nome = len(input("Digite o nome: "))

while idade < 0 or idade >150:
    idade = int(input("Digite sua idade novamente: "))

while salario < 0:
    salario = int(input("Qual salario? "))

#while ecivil != "c" or ecivil != "s" and ecivil != "d" or ecivil != "v":
 #   ecivil = input("Estado civil? ")

while sexo:
    sexo = input("Qual seu sexo: ")
    if sexo == 'm':
        sexo = False
    elif sexo == 'f':
        sexo = False



print(nome, idade, ecivil, sexo)