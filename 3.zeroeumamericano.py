qtdParticipantes = int(input('Quantos participantes? '))

while qtdParticipantes < 2:
    print('Quantidade inválida de participantes. Escolha um valor maior que 1')
    qtdParticipantes = int(input('Quantos participantes? '))

participantes = []
somaDedos = 0

cont = 1
while (cont <= qtdParticipantes):
    dedo = int(input(f'Participante {cont} : '))

    participantes.append(dedo)
    
    somaDedos += dedo
    cont += 1

resto = somaDedos
while resto > qtdParticipantes:
    resto -= qtdParticipantes

print(participantes)
print(f'Total: {somaDedos}')
print(f'O vencedor é: {resto}')