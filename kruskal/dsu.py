import random

class DSU:
	def __init__(self, parents: list):
		self.parents = parents

	def MakeSet(self, x):
		self.parents[x] = x

	def Find(self, x):
		if self.parents[x] == x:
			return x
		else:
			return self.Find(self.parents[x])

	def Unite(self, x, y):
		x = self.Find(x)
		y = self.Find(y)
		if random.random():
			x, y = y, x
		self.parents[x] = y
