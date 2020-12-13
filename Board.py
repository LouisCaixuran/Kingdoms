from Player import *
import random

class Board():
	def __init__(self,player1,player2):
		self.players=[player1,player2]
		p1Building=[[Building(1,player1),4],[Building(2,player1),3],[Building(3,player1),2],[Building(4,player1),1]]
		p2Building=[[Building(1,player2),4],[Building(2,player2),3],[Building(3,player2),2],[Building(4,player2),1]]
		self.playerBuildings=[p1Building,p2Building]
		self.initGame()

	def randomSelect(self):
		if self.boards:
			r=random.randint(0,len(self.boards)-1)
			self.players[self.t].selectedBoard=self.boards[r]
			del(self.boards[r])
			return None
		else:
			return "No board left"

	def chooseBuilding(self,level):
		if self.playerBuildings[self.t][level-1][1]>0:
			self.players[self.t].selectedBoard=self.playerBuildings[self.t][level-1][0]
			self.playerBuildings[self.t][level-1][1]-=1
		else:
			return "no building with that level left"



	def putBoard(self,x,y):
		self.playboard[x][y]=self.players[self.t].selectedBoard
		self.players[self.t].selectedBoard=None
		self.t=0 if self.t==1 else 1

	def ifFinished(self):
		for i in self.playboard:
			if None in i:
				return False
		return True

	def initGame(self):
		self.boards=[]
		self.t=0
		for i in self.playerBuildings:
			i[0][1]=4
		for i in range(1,7):
			self.boards.append(ValueBoard(-1*i))
			self.boards.append(ValueBoard(i))
			self.boards.append(ValueBoard(i))
		self.boards.append(ValueBoard(7))
		self.boards.append(ValueBoard(7))
		self.boards.append(ValueBoard(8))
		self.boards.append(ValueBoard(9))
		self.boards.append(ValueBoard(10))
		self.rowScore=[0 for i in range(5)]
		self.colScore=[0 for i in range(6)]
		self.playboard=[[None for i in range(6)]for j in range(5)]

	def showBoard(self):
		for i in self.playboard:
			for j in i:
				if j==None:
					print(" ",end=",")
				else:
					print(j.toString(),end=",")
			print()


