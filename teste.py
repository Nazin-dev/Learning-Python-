import os
import time
 
 
start = True  # Variável de controle de laço
lista = []
tempo_espera = 2
limpar_console = os.system('cls')
 
# Programa persistindo dados enquanto está rodando
while start:
    # Tela inicial
    print('-' * 5, 'Lista de Compras', '-' * 5)
 
    # Exibir a lista de compras
    print(f'A sua lista atual é = {lista}')
    print()
    print('Escolha entre uma das opções abaixo: ')
    print('[1] Acrescentar item')
    print('[2] Remover item')
    print('[3] Modificar item')
    print('[4] Fechar programa')
 
    #  Opção de acrescentar item
    opcao = input('Digite uma das opções citadas: ')
    if opcao == '1':
        limpar_console  # Limpa o console
 
        print(f'Lista atual = {lista}')
        item = input('Digite o nome do item que deseja adicionar: ')
        lista.append(item)
        print(f'O item "{item}" foi adicionado na lista.')
 
        time.sleep(tempo_espera)
        limpar_console  # Limpa o console
        continue
 
    #  Opção de remover item
    elif opcao == '2':
        item = input('Digite o nome do item que deseja remover: ')
        if item in lista:
            limpar_console  # Limpa o console
            lista.remove(item)
            print(
                f'O item "{item}" foi removido da lista.')
 
            time.sleep(tempo_espera)
            limpar_console  # Limpa o console
        else:
            limpar_console  # Limpa o console
            print(
                f'O item {item} não se encotra na lista atual = {lista}')
 
            time.sleep(tempo_espera)
            continue
 
    #  Opção de modificar item
    elif opcao == '3':
        item = input('Digite o nome do item que deseja modificar: ')
        if item in lista:
            limpar_console  # Limpa o console
 
            indice = lista.index(item)
            item_modificado = input(
                f'Digite o nome do item que irá substituir {item}: ')
            lista[indice] = item_modificado
 
            print(f'O item {item} foi substituído por {item_modificado}.')
 
            time.sleep(tempo_espera)
            limpar_console  # Limpa o console
            continue
        else:
            limpar_console  # Limpa o console
            print(f'O item {item} não está na lista')
            time.sleep(tempo_espera)
            continue
    elif opcao == '4':
        limpar_console
        print('Fechando o programa...')
        time.sleep(tempo_espera)
        start = False
    else:
        limpar_console  # Limpa o console
        print('Digite somente entre as opções "1", "2" e "3".')
        time.sleep(tempo_espera)
        continue