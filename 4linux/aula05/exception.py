#Tratar erros no python
def checar(x):
    try:
        if x == 3:
            raise Exception('Numero invalido')
    except Exception as e:
        raise Exception(e)


try:
    x = int(input('Digite o primeiro numero: '))
    y = int(input('Digite o segundo numero: '))

    checar(x)

    print(x+y)
except Exception as e:
    print('Digite apaenas numeros')
    print(e)
finally:
    print("Sempre executa")