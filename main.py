import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor esta

# Cria o socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket do cliente com o servidor
cliente.connect((HOST, PORT))

print('Cliente conectado ao servidor.')

while True:
    # Exibe o menu de opções
    print('\nOpções:')
    print('1 - Listar itens para votação')
    print('2 - Votar em um item')
    print('3 - Verificar ranking de votos')
    print('4 - Encerrar conexão')

    # Recebe a opção escolhida pelo usuário
    opcao = input('\nEscolha uma opção: ')

    # Envia o comando para o servidor
    if opcao == '1':
        # Listar itens para votação
        comando = 'LIST'
        cliente.send(comando.encode())

        # Recebe a lista de itens para votação
        lista_itens = cliente.recv(1024).decode()
        print(f'\nItens para votação: {lista_itens}')

    elif opcao == '2':
        # Votar em um item
        item = input('\nDigite o item para votar: ')
        comando = f'VOTE {item}'
        cliente.send(comando.encode())

        # Recebe a mensagem de confirmação do voto
        mensagem = cliente.recv(1024).decode()
        print(f'\n{mensagem}')

    elif opcao == '3':
        # Verificar ranking de votos
        comando = 'RANK'
        cliente.send(comando.encode())

        # Recebe o ranking de votos
        ranking = cliente.recv(1024).decode()
        print(f'\nRanking de votos:\n{ranking}')

    elif opcao == '4':
        # Encerrar conexão
        cliente.close()
        print('\nConexão encerrada.')
        break

    else:
        print('\nOpção inválida. Tente novamente.')
