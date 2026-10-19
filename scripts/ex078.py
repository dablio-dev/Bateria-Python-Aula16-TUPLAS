nomes = ('pedro', 'thiago', 'joao', 'maria', 'eva', 'kevin')
notas = (9.5, 8.4, 6.0, 4.5, 8.9, 5.0)
msg_aprovacao = ''
while True:
    try:
        consulta_nome = str(input('Nome a ser consultado: ')).strip().lower()
        indice_nome = nomes.index(consulta_nome)
        break
    except ValueError:
        print('Nome não encontrado, tente novamente ...')

if notas[indice_nome] >= 7:
    msg_aprovacao = '\033[1;32mAPROVADO\033[m'
elif notas[indice_nome] >= 5:
    msg_aprovacao = '\033[1;33mEM RECUPERAÇÃO\033[m'
else:
    msg_aprovacao = '\033[1;31mREPROVADO\033[m'
print(f'Nome: {nomes[indice_nome]} | Nota: {notas[indice_nome]}'
      f'\nCom esta nota o aluno {nomes[indice_nome]} está: {msg_aprovacao}')
