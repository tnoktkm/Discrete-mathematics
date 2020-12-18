import random

class DSU:
	def __init__(self, parents: []):
		self.parents = parents

	def MakeSet(self, x):
		self.parents[x] = x

	def Find(self, x):
		if (self.parents[x] == x):
			return x
		else:
			return self.Find(self.parents[x])

	def Unite(self, x, y):
		x = self.Find(x)
		y = self.Find(y)
		if (random.random()):
			"""Не нашел как swap функция в Python"""
			c = x
			x = y
			y = c
		self.parents[x] = y
"""
Долго думал как же лучше реализовать класс Краскал.
Чтобы для каждой вершины сделать его дерево(множестов) содержащий только его самого, но
тогда нужно знать все вершины, а мы вводим так: (вершина1, вершина2, вес)
Не понятно как сделать ввести граф, чтобы потом еще поддреживать массив(список) предков для DSU?


"""
