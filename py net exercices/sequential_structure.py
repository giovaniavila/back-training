#Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('alô mundo')

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = int(input('número: '))
print(f'número informado é {num}')

#Faça um Programa que peça dois números e imprima a soma
n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
print(n1+n2)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
b1 = int(input('bimestre 1: '))
b2 = int(input('bimestre 2: '))
b3 = int(input('bimestre 3: '))
b4 = int(input('bimestre 4: '))
print(f'a média é {(b1+b2+b3+b4)/4}')

#Faça um Programa que converta metros para centímetros.
metro = int(input('digite em metros: '))
print(f'em centímetros é:{metro*100}cm')

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input('raio do círculo: '))
print(f'a área do círculo é aproximadamente de:{(raio**2)*3,14}')

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
quadrado = int(input('digite a área do quadrado: '))
print(f'o dobro da área é de {quadrado*2}')

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
hora = int(input('quanto você ganha por hora: '))
trabalhadas = int(input('número de horas trabalhadas: '))
print(f'seu salário é de R${hora*trabalhadas}')

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
temperatura = int(input('digite a temperatura em graus fahrenheint: '))
print(f'temperatura em graus celsius é de {(5*(temperatura-32))/9}')

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo
n1 = int(input('digite um número inteiro: '))
n2 = float(input('digite um número real: '))
print(f'{(n1*2)*(n2/2)}')
print(f'{(n1*3)+(n1*3)}')
print(f'{n1**3}')


#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metro = float(input('tamanho da área a ser pintada:'))

litros = 6*metro

lata = litros/18
galao = litros/3.6

pl = lata*80
pg = galao*25

print(f'comprando latas:R${pl}')
print(f'comprando galao:R${pg}')




