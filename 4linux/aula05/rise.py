'''
1 -Criar uma classe chamada Carro

2 -ela deve ter os atributos: velocidade máxima e velocidade atual(zero)

3 - Criar um método para acelerar, ele deve verificar a velocidade atual e se for menor que
a velocidade máxima,somar a velocidade. Caso contrario mostrar que atingiu o limite de velocidade.

4 Criar um método para frear, ele deve verificar a velocidade atual, se for maior do que zero, abaixar
a velocidade. Se for igual a zero, mostrar que o carro já esta parado.
'''

class Carro: # Uma classe
    vel_max = 200 #Atributo
    vel_atual = 0 #Atributo

    def acelerar(self,velocidade): #metodo ou sessão
        if (self.vel_atual + velocidade) <= self.vel_max:
            self.vel_atual += velocidade
            raise Exception("Velocidade aumentada. (%s) "% self.vel_atual)
        else:
            raise Exception("Velocidade maxima atingida")

    def freiar(self):
        if (self.vel_atual - velocidade) >= 0:
            self.vel_atual = velocidade
            raise Exception("Velocidade reduzida. (%s)" % self.vel_atual)
        else:
            raise Exception("Não foi possivel reduzir")

try:


    objeto = Carro()

    objeto.acelerar(210)

    objeto.freiar(50)

except Exception as e:
    print(e)
