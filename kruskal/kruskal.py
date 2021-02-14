from dsu import DSU
 
class Kruskal:
	def __init__ (self, edges_graph = None):
		if edges_graph is None:
			self.edges_graph = []
		else:
			self.edges_graph = edges_graph

		self.parents = [i for i in range(0, 2*len(self.edges_graph))] #count vertex on graph with n edges(max)	
		self.headParents = DSU(self.parents)	#the same, but it a object class DSU

	def Work(self):
		self.headParents = DSU([i for i in range(0, 2*len(self.edges_graph))])
		lenTree = 0 #length tree now
		mst = []
		self.edges_graph.sort(key=lambda w: w[2])	#sort edges
		for edge in self.edges_graph:	
			if not self.headParents.Find(int(edge[0])) == self.headParents.Find(int(edge[1])):	#if they not including
				self.headParents.Unite(edge[0], edge[1])
				lenTree += edge[2]
				print("We choose this edge - " + str(edge))

				mst.append(edge)
		print("Our graph " + str(self.edges_graph))
		print("His lenght equal = " + str(lenTree))

		return mst

def main():
	ex1 = [(1, 2, 7),		#example
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

	ex2 = 	[(1, 2, 9),
			(1,6,7),
			(1,5,5),
			(2,6,2),
			(2,3,4),
			(3,6,1),
			(3,4,2),
			(4,6,4),
			(4,5,9),
			(5,6,3)]


	test = Kruskal(ex1)
	test.Work()   #the same output for graph already finding MST(literaly for already graph MST we saw the same MST graph)
	test.Work()
	print("Our MST graph = " + str(test.Work()))  #output our MST graph

if __name__ == '__main__':
    main()

#empty row
