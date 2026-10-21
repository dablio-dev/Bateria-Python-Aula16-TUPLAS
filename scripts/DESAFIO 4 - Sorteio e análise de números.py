from random import sample
numeros_sorteado = tuple(sample(range(1, 50), 6))
print('Os números sorteados foram: ', end='')
for numeros in numeros_sorteado:
    print(f'{numeros}', end=' ')
numeros_sorteado_sorted = tuple(sorted(numeros_sorteado))


