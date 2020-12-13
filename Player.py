class Player:
	def __init__(self,name):
		self.score=0
		self.name=name
		self.selectedBoard=None

class Building:
	def __init__(self,level,owner):
		self.level=level
		self.owner=owner

	def toString(self):
		return "B "+str(self.level)

class ValueBoard:
	def __init__(self,value):
		self.value=value
		self.type="p" if value>0 else "n"
		if value==7:
			self.type="mt" #mountain
		if value==8:
			self.type="dg" #dragon
		if value==9:
			self.type="gd" #gold
		if value==10:
			self.type="wt" #witch

	def toString(self):
		if abs(self.value)<=6:
			if self.value<0:
				return str(self.value)
			else:
				return "+"+str(self.value)
		else:
			return self.type

