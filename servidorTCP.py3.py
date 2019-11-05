# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 65000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Sala de chat iniciada na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  connectionSocket.send("Escolha seu nickname:".encode('utf-8'))
  nickname = connectionSocket.recv(1024)
  newUserEntrou='%s entrou...' % (nickname)
  print (newUserEntrou)
  connectionSocket.send(newUserEntrou)
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  print ('%s escreveu: %s' % (nickname, sentence))
  connectionSocket.send(sentence) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
  print('%s saiu!' % (nickname))
serverSocket.close() # encerra o socket do servidor