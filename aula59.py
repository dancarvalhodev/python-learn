"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros
de indices inexistentes na lista
"""
import os

acoes_permitidas = ['i', 'a', 'l', 's']
lista_de_compras = []

while True:
    print('Selecione uma opção')
    acao = input('[i]nserir | [a]pagar | [l]istar | [s]air: ').lower()

    if acao not in acoes_permitidas:
        print('Opção inválida!')
        continue
    elif acao == 's':
        print('Saindo...')
        break
    elif acao == 'i':
        os.system('clear')
        item = input('Valor: ')
        lista_de_compras.append(item)
    elif acao == 'l':
        if len(lista_de_compras) == 0:
            print('Nada para listar')
        
        for item in enumerate(lista_de_compras):
            indice, valor = item
            print(f'{indice} {valor}')
    elif acao == 'a':
        try:
            indice = input('Escolha o índice para apagar: ')
            del lista_de_compras[int(indice)]
        except ValueError:
            print('Por favor digite um inteiro.')
        except IndexError:
            print('Não foi possivel apagar esse índice.')
        except:
            print('Erro desconhecido')
    else:
        print('Erro interno')
        break


    



