import socket 
from Board import *
from Player import *

class Server():
	def __init__(self,player):
		self.serverPlayer=new Player(player)
		self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server.bind(('localhost',6999))
		server.listen(5)



	def running(self):
		while True:
			conn,addr = server.accept()
			player= conn.recv(1024)
			self.clientPlayer=new Player(player)
			self.board=new Board(self.serverPlayer,self.clientPlayer)
			while not self.board.ifFinished:
				if self.board.players[self.board.t]==self.serverPlayer:
					self.action() 
				else
					conn.send(self.board.toString())
					self.board=conn.resv(4096)


	
	def action(self):

