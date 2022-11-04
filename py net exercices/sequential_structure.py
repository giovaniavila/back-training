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


quadrado = int(input('digite a área do quadrado: '))
print(f'o dobro da área é de {quadrado*2}')


hora = int(input('quanto você ganha por hora: '))
trabalhadas = int(input('número de horas trabalhadas: '))
print(f'seu salário é de R${hora*trabalhadas}')


temperatura = int(input('digite a temperatura em graus fahrenheint: '))
print(f'temperatura em graus celsius é de {(5*(temperatura-32))/9}')

n1 = int(input('digite um número inteiro: '))
n2 = float(input('digite um número real: '))
print(f'{(n1*2)*(n2/2)}')
print(f'{(n1*3)+(n1*3)}')
print(f'{n1**3}')


metro = float(input('tamanho da área a ser pintada:'))

litros = 6*metro

lata = litros/18
galao = litros/3.6

pl = lata*80
pg = galao*25

print(f'comprando latas: R${pl}')
print(f'comprando galao: R${pg}')




