from random import shuffle

a1 = str(input('Insira o primeiro aluno: '))
a2 = str(input('Insira o segundo aluno: '))
a3 = str(input('Insira o terceiro aluno: '))
a4 = str(input('Insira o quarto aluno: '))
lista = [a1, a2, a3, a4]

shuffle(lista)

print('A sequencia de alunos será: {}'.format(lista))