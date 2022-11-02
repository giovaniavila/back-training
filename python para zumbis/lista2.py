
a = int(input('informe um lado:'))
b = int(input('informe outro lado:'))
c = int(input('informe outro lado: '))
if a > b + c or b > a + c or c > a + b:
    print('não pode ser um triângulo')
    print('um dos lados é maior que a soma dos outros dois lados')
elif a == b == c:
    print('equilátero')
elif a == b or b == c or a == c:
    print('isósceles')
else:
    print('escaleno')

from calendar import isleap
ano = int(input('digite o ano:'))
if isleap(ano):
    print('ano bissexto')
else:
    print('não é ano bissexto')

peixe = int(input('digite o peso em kg:'))
if peixe > 50:
    print(f'multa será de R${(peixe-50)*4}')
else:
    print('sem multa')

n1 = int(input('digite um número:'))
n2 = int(input('digite outro número: '))
n3 = int(input('digite outro número: '))
if n1 > n2 and n1 > n3:
    print(n1)
if n2 > n1 and n2 > n3:
    print(n2)
if n3 > n1 and n3 > n2:
    print(n3)

n1 = int(input('digite um número:'))
n2 = int(input('digite outro número: '))
n3 = int(input('digite outro número: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número')
if n3 > n1 and n3 > n2:
    print(f' {n3} é o maior número')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número')
if n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número')
if n3 < n1 and n3 < n2:
    print(f'{n3} é o menor número')

