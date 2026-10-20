palavras_tuplas = ('tupla', 'imutavel', 'indice', 'fatiamento', 'sequencia')
for palavras in palavras_tuplas:
    print(f'\nNa palavra: {palavras.upper()} temos as vogais: ', end='')
    palavra_vogal = None
    ant_repeat = ''
    for vogais in palavras:
        if vogais in 'aeiou':
            if vogais in ant_repeat:
                continue
            else:
                ant_repeat += str(vogais)
                print(f'{vogais.upper()} ', end='')
                palavra_vogal = True
    if palavra_vogal == None:
        print('Esta palavra não possui vogal.', end='')