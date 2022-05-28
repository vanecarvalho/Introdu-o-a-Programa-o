#banco de dados tirado de: 
# https://buzzfeed.com.br/quiz/estas-perguntas-foram-feitas-no-show-do-milhao-quantas-voce-consegue-acertar

import random

perguntas = {
    1 : 'Qual bicho transmite Doença de Chagas?',
    2 : 'Qual fruto é conhecido no Norte e Nordeste como "jerimum"?',
    3 : 'Qual é o coletivo de cães?',
    4 : 'Qual é o triângulo que tem todos os lados diferentes?',
    5 : 'Quem compôs o Hino da Independência?',
    6 : 'Qual é o antônimo de "malograr"?',
    7 : 'Em que país nasceu Carmem Miranda?',
    8 : 'Qual foi o último Presidente do período da ditadura militar no Brasil?',
    9 : 'Seguindo a sequência do baralho, qual carta vem depois do dez?',
    10: 'O adjetivo "venoso" está relacionado a:'
}

alternativas = {
    1 : [
            'A) Abelha',
            'B) Barata',
            'C) Pulga',
            'D) Barbeiro'
        ],
    2 : [
            'A) Caju',
            'B) Abóbora', 
            'C) Chuchu', 
            'D) Coco'
         ],
    3 : [
            'A) Matilha', 
            'B) Rebanho', 
            'C) Alcateia', 
            'D) Manada'
        ],
    4 : [
            'A) Equilátero', 
            'B) Isóceles', 
            'C) Escaleno', 
            'D) Trapézio'
        ],
    5 : [
            'A) Dom Pedro I', 
            'B) Manuel Bandeira', 
            'C) Castro Alves', 
            'D) Carlos Gomes'
        ],
    6 : [
            'A) Perder', 
            'B) Fracassar', 
            'C) Conseguir', 
            'D) Desprezar'
        ],
    7 : [
            'A) Brasil', 
            'B) Espanha', 
            'C) Portugal', 
            'D) Argentina'
        ],
    8 : [
            'A) Costa e Silva', 
            'B) João Figueiredo', 
            'C) Ernesto Geisel', 
            'D) Emílio Médici'
        ],
    9 : [
            'A) Rei', 
            'B) Valete', 
            'C) Nove', 
            'D) Ás'
        ],
    10 : [
            'A) Vela', 
            'B) Vento', 
            'C) Vênia', 
            'D) Veia'
        ],
}

gabarito = {
    1 : 'D',
    2 : 'B',
    3 : 'A',
    4 : 'C',
    5 : 'A',
    6 : 'C',
    7 : 'C',
    8 : 'B',
    9 : 'B',
    10 : 'D',
}

qtdRodadas = 5
pontos = 0

for i in range(qtdRodadas):
    chaveSorteada = random.randint(1, len(perguntas))

    print(perguntas[chaveSorteada])

    for alternativa in alternativas[chaveSorteada]:
        print(alternativa)
        
    respostaUsuario = input('Escolha uma alternativa: ')

    if (respostaUsuario.upper() != gabarito[chaveSorteada]):
        print('GAME OVER!')
        break

    pontos += 100
    del perguntas[chaveSorteada]
    del alternativas[chaveSorteada]
    del gabarito[chaveSorteada]

print(f'Sua pontuação foi: {pontos} pontos')
