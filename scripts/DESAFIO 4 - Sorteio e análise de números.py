from random import sample
numeros_sorteado = tuple(sample(range(1, 50), 6))
numeros_sorteado_sorted = tuple(sorted(numeros_sorteado))
palpite = 0
#Loop de validação palpite
while True:
    try:
        palpite = int(input('Palpite de numero inteiro na tupla aleatória (1 a 50): '))
        if 1 <= palpite <= 50:
            break
    except ValueError:
        print('ERRO. Digite um numero inteiro entre 1 e 50')
        continue
#Número palpitado esta na tupla? Em qual posição?
if palpite in numeros_sorteado_sorted:
    print(f'O numero {palpite} esta na posição humana {numeros_sorteado_sorted.index(palpite) + 1} na tupla ordenada em ordem crescente.')
else:
    print(f'O numero {palpite} não esta em nenhuma das tuplas.')
#Exibição em loop dos números radomizados na tupla
print('Os números sorteados foram: ', end='')
for numeros in numeros_sorteado:
    print(f'{numeros}', end=' ')
#Primeiro e ultimo da tupla ordenada ou maior e menor da tupla random
print(f'\nPrimeiro numero em ordem crescente: {numeros_sorteado_sorted[0]} | Ultimo numero em ordem crescente: {numeros_sorteado_sorted[-1]}')
#Exibição em loop da tupla ordenada
print('Números sorteados em ordem crescente: ', end='')
for numeros in numeros_sorteado_sorted:
    print(f'{numeros}', end=' ')


