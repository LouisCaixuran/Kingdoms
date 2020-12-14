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
		else:
			return "no building with that level left"



	def putBoard(self,x,y):
		if self.players[self.t].selectedBoard.isV==False:
			self.playerBuildings[self.t][self.players[self.t].selectedBoard.level-1][1]-=1
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

	#def showBoard(self):
	#	for i in self.playboard:
	#		for j in i:
	#			if j==None:
	#				print(" ",end=",")
	#			else:
	#				print(j.toString(),end=",")
	#		print()

	def checkScore(self):
		row=[]
		col=[]
		#process the witch
		for i in range(5):
			for j in range(6):
				if self.playboard[i][j].value==10:
					try:
						if self.playboard[i-1][j].isV==False:
							self.playboard[i-1][j]=Building(self.playboard[i-1][j].level+1,self.playboard[i-1][j].owner)
					except Exception as e:
						pass
					try:
						if self.playboard[i+1][j].isV==False:
							self.playboard[i+1][j]=Building(self.playboard[i+1][j].level+1,self.playboard[i+1][j].owner)
					except Exception as e:
						pass
					try:
						if self.playboard[i][j-1].isV==False:
							self.playboard[i][j-1]=Building(self.playboard[i][j-1].level+1,self.playboard[i][j-1].owner)
					except Exception as e:
						pass
					try:
						if self.playboard[i][j+1].isV==False:
							self.playboard[i][j+1]=Building(self.playboard[i][j+1].level+1,self.playboard[i][j+1].owner)
					except Exception as e:
						pass
					self.playboard[i][j].value=0

		#process the mountain
		for i in self.playboard:
			smr=[]
			for j in i:
				if j.value!=7 :
					if j.isV==True:
						smr.append(j.value)
					else:
						smr.append(j)
				else:
					row.append(smr)
					smr=[]
			row.append(smr)

		for i in range(6):
			newcol=[]
			for j in range(5):
				if self.playboard[j][i].value!=7:
					if self.playboard[j][i].isV==True:
						newcol.append(self.playboard[j][i].value)
					else:
						newcol.append(self.playboard[j][i])					
				else:
					col.append(newcol)
					newcol=[]
			col.append(newcol)

		final=row+col

		#process the dragon
		for i in final:
			if 8 in i:
				for k in range(len(i)):
					if isinstance(i[k],int):
						if i[k]>0 and i[k]!=9:
							i[k]=0


		#process the gold
		for i in final:
			if 9 in i:
				for k in range(len(i)):
					if isinstance(i[k],int):
						if i[k]!=9:
							i[k]*=2
						else:
							i[k]=0

		#calculate final score
		for i in final:
			score=0
			l=[0,0]
			for j in i:
				if isinstance(j,int):
					score+=j
			#		print(j,end="+")
				else:
					l[self.players.index(j.owner)]+=j.level
			#print("="+str(score),end=",")
			#print(l)

			self.players[0].score+=l[0]*score
			self.players[1].score+=l[1]*score




