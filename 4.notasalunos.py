import math

notas = []
qtdNotas = somaNotas = acimaMedia = somatorioDasDiferenças = 0

while True:
    nota = float(input(f'Digite a nota final do aluno {qtdNotas+1} (-1 para parar) '))

    while nota > 10:
        print('O valor informado deve ser entre 0 e 10')
        nota = float(input(f'Digite a nota final do aluno {qtdNotas+1} (-1 para parar) '))

    if (nota < 0):
        break

    notas.append(nota)
    somaNotas += nota
    qtdNotas += 1

if(qtdNotas == 0):
    print('Nenhuma nota foi informada!')
    exit()

media = somaNotas / qtdNotas

for nota in notas:
    if (nota > media):
        acimaMedia += 1
        
for nota in notas:
    somatorioDasDiferenças += (nota - media)**2

desvioPadrao = math.sqrt(somatorioDasDiferenças / qtdNotas)

print(f'\nA quantidade de notas lidas foram: {qtdNotas}')

print(f'As notas lidas são: ')
for nota in notas:
    print(nota, end='; ')

print(f'\nA soma das notas é: {somaNotas}')
print(f'A média das notas é: {media:.2f}')
print(f'A quantidade de alunos que tiraram nota acima da média é: {acimaMedia}')
print(f'O desvio padrão das notas é: {desvioPadrao:.2f}')


# Autor: Vanessa da Silva Lima de Carvalho
# email: vslc@discente.ifpe.edu.br