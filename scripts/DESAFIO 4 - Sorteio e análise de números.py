from random import sample
numeros_sorteado = tuple(sample(range(1, 51), 6))
numeros_sorteado_sorted = tuple(sorted(numeros_sorteado))
palpite = 0
#Loop de validação palpite
while True:
    try:
        palpite = int(input('Palpite de numero inteiro na tupla aleatória (1 a 50): '))
        if 1 <= palpite <= 50:
            break
        else:
            print('ERRO. Digite um numero inteiro entre 1 e 50')
    except ValueError:
        print('ERRO. Digite um numero inteiro entre 1 e 50')
        continue
#Número palpitado esta na tupla? Em qual posição?
if palpite in numeros_sorteado_sorted:
    print(f'O numero {palpite} esta na posição humana {numeros_sorteado_sorted.index(palpite) + 1}'
          f' na tupla ordenada em ordem crescente.')
else:
    print(f'O numero {palpite} não esta em nenhuma das tuplas.')
#Exibição em loop dos números radomizados na tupla
print('Os números sorteados foram: ', end='')
for numero in numeros_sorteado:
    print(f'{numero}', end=' ')
#Primeiro e ultimo da tupla ordenada ou maior e menor da tupla random
print(f'\nPrimeiro numero em ordem crescente: {numeros_sorteado_sorted[0]}'
      f' | Ultimo numero em ordem crescente: {numeros_sorteado_sorted[-1]}')
#Exibição em loop da tupla ordenada
print('Números sorteados em ordem crescente: ', end='')
for numero in numeros_sorteado_sorted:
    print(f'{numero}', end=' ')
