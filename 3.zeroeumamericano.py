qtdParticipantes = int(input('Quantos participantes? '))

while qtdParticipantes < 2:
    print('Quantidade inválida de participantes. Escolha um valor maior que 1')
    qtdParticipantes = int(input('Quantos participantes? '))

participantes = []
somaDedos = 0

cont = 1
while (cont <= qtdParticipantes):
    dedo = int(input(f'Participante {cont} : '))

    while dedo < 0 or dedo > 10:
        print('O valor informado deve ser entre 0 e 10')
        dedo = int(input(f'Participante {cont} : '))


    participantes.append(dedo)
    
    somaDedos += dedo
    cont += 1

resto = somaDedos
while resto > qtdParticipantes:
    resto -= qtdParticipantes

print(f'Total: {somaDedos}')
print(f'O vencedor é o participante {resto}')


# Autor: Vanessa da Silva Lima de Carvalho
# email: vslc@discente.ifpe.edu.br