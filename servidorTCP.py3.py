# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets
import threading as th
from user import User


def fluxoCliente(sock, addr):
  myUser=newUser(sock, addr)
  newUserEntrou='%s entrou...' % myUser.getNick()
  print(newUserEntrou)
  sendMessage(connectionSocket,  newUserEntrou)
  
  newMessage=th.Thread(target = receiveMessages, args=(connectionSocket,myUser, ))
  newMessage.start()
  
  
  '''
  message = 'None'
  while message != 'quit':
    message = connectionSocket.recv(1024).decode('utf-8')
    print(novoUsuario.getNick+': '+message)
    
    if message.find('(') != -1 and message.find(')') != -1:
      comando = message.split('(')
      if comando[0] == 'privado':
        privateMessage = comando[1].split(')')
        
      if comando[0] == 'lista':
  '''
    
       
def nickChoice(connectionSocket):
  sendMessage(connectionSocket, "Escolha seu nickname:")
  nickname = connectionSocket.recv(1024).decode('utf-8')
  return nickname

def newUser(connectionSocket, addr):
  nick=nickChoice(connectionSocket)
  newUser=User(nick, addr[0], addr[1])
  return newUser
  
def receiveMessages(connectionSocket, myUser):
  while(1):
    message=connectionSocket.recv(1024).decode('utf-8')
    print(myUser.getNick() + ":" + message)
    sendMessage(connectionSocket, message)
  

def sendMessage(connectionSocket, message):
  connectionSocket.send(message.encode('utf-8'))
    
    
  
  
# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 65000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes

print ('Sala de chat iniciada na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  t = th.Thread(target=fluxoCliente, args=(connectionSocket,addr,))
  t.start()
  #userList=newUser(userList, connectionSocket, addr)
  #n=len(userList)
  #newUserEntrou='%s entrou...' % userList[n-1][0]
  #print(newUser)
  #print (newUserEntrou)
  #connectionSocket.send(newUserEntrou.encode('utf-8'))
  #while(1):
  #  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  #  sentence = sentence.decode('utf-8')
  #  print ('%s escreveu: %s' % (userList[n-1][0], sentence))
  # connectionSocket.send(sentence.encode('utf-8')) # envia para o cliente o texto transformado
  #connectionSocket.close() # encerra o socket com o cliente
  #print('%s saiu!' % (nickname))
serverSocket.close() # encerra o socket do servidor