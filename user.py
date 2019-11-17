class User:
    def __init__(self, nickname,ip, porta, connectionSocket):
        self.nickname=nickname
        self.ip=ip
        self.porta=porta
        self.connectionSocket=connectionSocket
        
    
    def __str__(self):
        return ('<' + str(self.nickname) + ',' + str(self.ip) + ',' + str(self.porta) + '>')
    
    def getNick(self):
        return self.nickname
    
    def getIp(self):
        return self.ip
    
    def getPorta(self):
        return self.porta
    
    def getSocket(self):
        return self.connectionSocket
    