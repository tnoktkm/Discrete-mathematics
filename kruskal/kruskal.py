from dsu import DSU
 


def main():
	class Kruskal:
		def __init__ (self, edges_graph = None):
			if edges_graph is None:
				self.edges_graph = []
			self.parents = [0]	


		def EnterEdgesKeyboard(self):
			count_edge = int(input("Enter count Edge - "))
			#List with indexs from 1 to countVertices and with the same value
			for i in range(1, count_edge):
				self.parents.append(i)

			self.headParents = DSU(self.parents)


			for i in range(count_edge):
				first_vertex, second_vertex, weight = input().split()
				first_vertex = int(first_vertex)
				second_vertex = int(second_vertex)
				weight = int(weight)

				self.edges_graph.append((first_vertex, second_vertex, weight))

		def Testing(self):
			#self.EnterEdges()
			lenTree = 0 #length now tree
			self.edges_graph.sort(key=lambda w: w[2])	#sort edges
			for edge in self.edges_graph:	
				if not self.headParents.Find(int(edge[0])) == self.headParents.Find(int(edge[1])):	#if they not including
					self.headParents.Unite(edge[0], edge[1])
					lenTree += edge[2]
					print("We choose this edge - " + str(edge))
			print("We used " + str(self.edges_graph))
			print("His lenght equal = " + str(lenTree))


	def ApplyExample(test = None):		
		#List with indexs from 0 to countVertices and with the same value
		test.parents = [i for i in range(0, 8)]

		test.headParents = DSU(test.parents)	#create dsu struct

		test.edges_graph = [(1, 2, 7),		#example
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

		#self.edges_graph = [(1, 2, 9),
							#(1,6,7),
							#(1,5,5),
							#(2,6,2),
							#(2,3,4),
							#(3,6,1),
							#(3,4,2),
							#(4,6,4),
							#(4,5,9),
							#(5,6,3)]
				

	test = Kruskal()
	ApplyExample(test)
	test.Testing()

if __name__ == '__main__':
    main()

#empty row
