produto_preco = (str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')),
                 str(input('Digite o nome do produto: ')).strip().lower(), float(input('Digite o preço: ')))
precos = ()
maior_50 = 0
print('-' * 30)
print('PRODUTOS'.center(15, ' '), '| ', 'PREÇOS'.center(11, ' '))
for itens in range (0, len(produto_preco), 2):
    if produto_preco[itens + 1] > 50:
        maior_50 += 1
    precos += (produto_preco[itens+1],)
    print(f'{produto_preco[itens]:<15} | R${produto_preco[itens + 1]:<.2f}')
print(f'Maior preço registrado: R${max(precos):.2f} | Menor preço registrado: R${min(precos):.2f}'
      f'\nProdutos custando mais de R$50.00: {maior_50}'
      f'\nValor total da compra: R${sum(precos):.2f}')