from tkinter import *
import tkinter.messagebox
from Board import *

class Gui():
	def __init__(self):
		self.askName()
		self.root = Tk()
		self.root.geometry("400x200")
		self.labels=[]
		for i in range(5):
			for j in range(6):
					self.labels.append(Label(self.root,text="00"))
					self.labels[-1].grid(row=i,column=j)
	
		self.labels.append(Label(self.root,text="selected board: None"))
		self.labels[-1].grid(row=1,column=6)
		self.labels.append(Label(self.root,text="Player: "+self.board.players[self.board.t].name))
		self.labels[-1].grid(row=3,column=6)

		self.button1=Button(self.root,text="choose a random board",command=self.chooseS)
		self.button1.grid(row=5,column=6)
		self.button2=Button(self.root,text="choose a building",command=self.selectBuilding)
		self.button2.grid(row=6,column=6)
		self.button3=Button(self.root,text="put on gameboard",command=self.selectB,state=DISABLED)
		self.button3.grid(row=7,column=6)


		self.root.mainloop()

	def askName(self):
		askname=Tk()
		askname.geometry("400x110")
		Label(askname,text="please input plater1's name").grid(row=0)
		name1=Entry(askname)
		name1.grid(row=0,column=1)
		Label(askname,text="please input plater2's name").grid(row=1)
		name2=Entry(askname)
		name2.grid(row=1,column=1)

		Button(askname,text="submit",command=lambda:[self.createBoard(name1.get(),name2.get()),askname.destroy()]).grid(row=2)
		
		askname.mainloop()

	def createBoard(self,n1,n2):
		if n1=="":
			n1="player1"
		if n2=="":
			n2="player2"
		self.board=Board(Player(n1),Player(n2))

	def chooseS(self,level=None):
		if level==None:
			message=self.board.randomSelect()
		else:
			message=self.board.chooseBuilding(level)
		if message!=None:
			tkinter.messagebox.showinfo("error",tmessage)
		else:
			self.labels[-2]['text']="selected board: "+self.board.players[self.board.t].selectedBoard.toString()
			self.button1['state']=DISABLED
			self.button2['state']=DISABLED
			self.button3['state']=NORMAL
			self.root.update()

	def selectBuilding(self):
		c=Tk()
		c.geometry("200x100")
		for i in self.board.playerBuildings[self.board.t]:
			if i[1]!=0:
				Button(c,text="level "+str(i[0].level)+",number left: "+str(i[1]),command=lambda i=i:[self.chooseS(level=i[0].level),c.destroy()]).grid(column=1)
			else:
				Label(c,text="level "+str(i[0].level)+",number left: "+str(i[1])).grid(column=1)

		c.mainloop()

	def selectB(self):
		s=Tk()
		s.geometry("200x200")
		for i in range(5):
			for j in range(6):
				if self.board.playboard[i][j]==None:
					Button(s,text=self.labels[6*i+j]['text'],fg=self.labels[i*6+j]["fg"],command=lambda i=i,j=j:[self.putCard(i,j),s.destroy()]).grid(row=i,column=j)
				else:
					Label(s,text=self.labels[6*i+j]['text'],fg=self.labels[i*6+j]["fg"]).grid(row=i,column=j)
		s.mainloop()


	def putCard(self,x,y):
		if self.board.players[self.board.t].selectedBoard==None:
			tkinter.messagebox.showinfo("error","you need to select a board first")
		elif self.labels[x*6+y]['text']!="00":
			tkinter.messagebox.showinfo("error","you need to select an empty area")
		else:
			self.board.putBoard(x,y)
			if self.board.playboard[x][y].toString()[0]=="B":
				if self.board.playboard[x][y].owner==self.board.players[0]:
					self.labels[x*6+y]["fg"]="DarkGreen"
				else:
					self.labels[x*6+y]["fg"]="Orange"
			elif abs(self.board.playboard[x][y].value)<=6:
				if(self.board.playboard[x][y].value>0):
					self.labels[x*6+y]["fg"]="Blue"
				else:
					self.labels[x*6+y]["fg"]="FireBrick"
			else:
				self.labels[x*6+y]["fg"]="Black"

			self.labels[x*6+y]["text"]=self.board.playboard[x][y].toString()

			self.labels[-2]['text']="selected board: None"
			self.labels[-1]['text']="Player: "+self.board.players[self.board.t].name
			self.button1['state']=NORMAL
			self.button2['state']=NORMAL
			self.button3['state']=DISABLED
			self.root.update()











