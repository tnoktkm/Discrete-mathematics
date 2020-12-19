from dsu import DSU
 
class Kruskal:
	def __init__ (self, edges_graph = None):
		if edges_graph is None:
			self.edges_graph = []
		self.parents = [0]


	def EnterEdges(self):
		count_edge = int(input("Enter count Edge - "))
		"""List with indexs from 1 to countVertices and with the same value"""
		for i in range(1, count_edge+2):
			self.parents.append(i)

		self.parents = DSU(self.parents)

		for i in range(count_edge):
			first_vertex, second_vertex, weight = input().split()
			first_vertex = int(first_vertex)
			second_vertex = int(second_vertex)
			weight = int(weight)

			self.edges_graph.append((first_vertex, second_vertex, weight))

	def Testing(self):
		"""
		self.EnterEdges()
		"""
		lenTree = 0
		self.edges_graph.sort(key=lambda w: w[2])
		for i in self.edges_graph:
			if not self.parents.Find(int(i[0])) == self.parents.Find(int(i[1])):
				self.parents.Unite(i[0], i[1])
				lenTree += i[2]
				print("We choose this edge - " + str(i))
		print("We used " + str(self.edges_graph))
		print("His lenght equal = " + str(lenTree))


	def ApplyExample(self):		
		"""List with indexs from 1 to countVertices and with the same value"""
		for i in range(1, 13):
			self.parents.append(i)

		self.parents = DSU(self.parents)

		self.edges_graph = [(1, 2, 7),
		(2, 3, 8),
		(1, 4, 5),
		(3, 5, 5),
		(2, 4, 9),
		(2, 5, 7),
		(4, 5, 15),
		(4, 6, 6),
		(5, 6, 8),
		(5, 7, 9),
		(7, 6, 11)]
			

test = Kruskal()
test.ApplyExample()
test.Testing()
