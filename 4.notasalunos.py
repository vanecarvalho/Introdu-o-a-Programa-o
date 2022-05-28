import math

qtdNotas = 1
notas = []
somaNotas = acimaMedia = somatorioDasDiferenças = 0

while True:
    nota = float(input('Digite a nota final do aluno {qtdNotas} (-1 para parar) '))

    if (nota < 0):
        break

    notas.append(nota)
    somaNotas += nota
    qtdNotas += 1

print(f'A quantidade de notas lidas foram: {qtdNotas}')
print(f'As notas lidas foram: {notas}')
print(f'A soma das notas é: {somaNotas}')

media = somaNotas / qtdNotas
print(f'A média das notas é: {media:.2f}')

for nota in notas:
    if (nota > media):
        acimaMedia += 1
        
print(f'A quantidade de alunos que tiraram nota acima da média foram: {acimaMedia}')

for nota in notas:
    somatorioDasDiferenças += (nota - media)**2

desvioPadrao = math.sqrt(somatorioDasDiferenças / qtdNotas)

print(f'O desvio padrão das notas é: {desvioPadrao:.2f}')