notas = {
    200 : 0,
    100 : 0,
    50 : 0,
    20 : 0,
    5 : 0,
    2 : 0,
    1: 0
}

saque = int (input('Valor a ser sacado: '))
resto = saque

while True :
    nota = int (input('Informe qual valor da nota você quer (0 para parar): '))

    if (nota == 0):
        break

    while resto >= nota :
        notas[nota] += 1
        resto -= nota

notas[1] =  resto

print('A quantidade de notas é:') 
for key in notas:
    value = notas[key]
    
    if(value != 0):
        print(f'R$ {key} : {value}')
        
