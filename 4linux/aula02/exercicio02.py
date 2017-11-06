maior = 0
#############
num = int(input("Digite o primeiro numero: "))

if num > maior:
    maior = num

###############
num2 = int(input("Digite outro numero: "))

if num2 > maior:
    maior = num2

################

num3 = int(input("Digite o terceiro numero: "))

if num3 > maior:
    maior = num3

#######
print("o maior numero é: %s " % maior)
