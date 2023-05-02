# Client
Client do Servidor
Nesse código, o cliente primeiro cria o socket e estabelece a conexão com o servidor usando o método connect().
Em seguida, exibe um menu de opções para o usuário e aguarda a entrada de uma opção.
Dependendo da opção escolhida pelo usuário, o cliente envia uma mensagem para o servidor usando o método send() e aguarda a resposta do servidor usando o método recv().
Quando o usuário escolhe a opção de encerrar a conexão, o cliente fecha a conexão usando o método close().
