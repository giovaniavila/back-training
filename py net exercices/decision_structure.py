#Faça um Programa que peça dois números e imprima o maior deles
n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))

if n1 > n2:
    print(n1)
else:
    print(n2)

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('número: '))
 
if valor >= 0:
    print('valor positivo')
else:
    print('valor negativo')

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = str(input('letra: '))

if letra == 'F' or letra == 'M':
    print(letra)
    
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('digite uma letra: '))
vogal = ['a','e','i','o','u']

if letra in vogal:
    print('vogal')
else:
    print('consoante')

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = int(input('primeira nota: '))
nota2 = int(input('segunda nota: '))
medida = (nota1 + nota2)/2

if 7 <= media < 10:
    print('aprovado')
if media < 7:
    print('reprovado')
if media == 10:
    print('Aprovado com Distinção')

