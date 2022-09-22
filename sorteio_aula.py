from random import randrange
from time import sleep
nomes = ('Jonathan', 'Bruna')
sorteado = nomes[randrange(len(nomes))]
print('\033[36m*=' * 15)
print('  SORTEIO AULA DE DOMINGO')
print('  O nome sorteado foi: ', end='')
sleep(2)
print(sorteado)
if sorteado == 'Bruna':
    print('\033[32m+' * 30)
    aulasb = ('Funções Python', 'Lista Python',  'Python if, else, elif', 'Tuplas python', 'Dicionario Python',
              'sortudo pode escolher o que ensinar', 'For python', 'While Python', 'django basico', 'flask basico',
              'PDF python', 'biblioteca py')
    print('O tema da aula será:  ', end='')
    sleep(2)
    aula = aulasb[randrange(len(aulasb))]
    print(aula)
    print('\033[32m+' * 30)
else:
    print('\033[31m¨' * 30)
    aulasj = ('Funções Javascript', 'Funções Python', 'Lista Python', 'Array Javascript', 'Python if, else, elif',
              'Javascript if, if else','Javascript switch,', ' case', 'Css grid', 'Css flex box', 'HTML buttões',
              'Css manipulações básicas','Tuplas python', 'Dicionario Python', 'Dicionaria javascript', 'While Python',
              'sortudo pode escolher o que ensinar', 'For python', 'For javascript',  'While Javascript')
    print('O tema da aula será:  ', end='')
    sleep(2)
    aula = aulasj[randrange(len(aulasj))]
    print(aula)
    print('\033[31m¨' * 30)
print('\033[36m*=' * 15)
print('Estaremos aguardando ansiosos!')
print('     ==> BOA SORTE! <==   ')
