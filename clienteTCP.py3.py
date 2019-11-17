# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula
#

# importacao das bibliotecas
from socket import *
import threading as th
from user import User

def nicknameSelect(clientSocket):
    nickSolicitacao=clientSocket.recv(1024).decode('utf-8')
    nickname=input(nickSolicitacao)
    clientSocket.send(nickname.encode('utf-8'))
    return nickname
    
def quitUser(clientSocket):
    clientSocket.close() # encerramento o socket do cliente
    
def sendMessage(clientSocket):
    while(1):
        sentence=input()
        clientSocket.send(sentence.encode('utf-8'))
        

def readMessage(clientSocket):
    while(1):    
        message = clientSocket.recv(1024).decode('utf-8')
        print(message)
        if message == 'sair()':
            quitUser(clientSocket)
    


# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

nicknameSelect(clientSocket)
newUserEntrou=clientSocket.recv(1024).decode('utf-8')
print(newUserEntrou)

send = th.Thread(target=readMessage, args=(clientSocket, ))
send.start()
read = th.Thread(target=sendMessage, args=(clientSocket, ))
read.start()

'''
    sentence=input("Digite sua mensagem:")
    sentMessage(clientSocket, sentence)
     # envia o texto para o servidor
'''
#quitUser(clientSocket)

# o servidor deve iniciar
# Seridor fica aguardando novas conexões constantemente
# o cliente deve se conectar ao servidor
# o servidor deve enviar uma solicitação do nickname ao cliente
# o cliente deve escolher um nickname e enviar ao servidor
# o servidor deve receber o nickname
# o servidor deve salvar o <nick, ip, porta> em uma lista de usuários
# o servidor envia para todos os usuários que um novo usuário entrou
# o cliente deve receber a mensagem de que um novo usuário entrou
# O servidor deve enviar para todos os usuários as mensagens enviadas e quem enviou
# O cliente deve poder mandar mensagem a todo momento
# O cliente deve receber mensagens novas a todo momento

