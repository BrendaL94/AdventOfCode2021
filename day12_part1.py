"""https://adventofcode.com/2021 """

# day12 Part 2
from collections import defaultdict

file = open("input_day12.txt", "r")
paths = file.readlines()
file.close()

# paths = """start-A,
# start-b,
# A-c,
# A-b,
# b-d,
# A-end,
# b-end""".split(',')

# Graph Class adapted from: https://www.geeksforgeeks.org/find-paths-given-source-destination/
class Graph:
  
    def __init__(self, distinct_vertices):
        self.distinct_vertices = distinct_vertices
        self.graph = defaultdict(list)
        self.pathsCount = 0
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  
    def printAllPathsUtil(self, u, d, visited, path):
 
        # Mark the current node as visited and store in path
        if u in visited:
            visited.remove(u)
        path.append(u)

        # reached destination
        if u == d:
            self.pathsCount += 1
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if (i in visited) or (i.isupper()):
                    self.printAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        if u not in visited:
            visited.append(u)  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        visited = self.distinct_vertices.copy()
        print(self.graph)
        # Create an array to store paths
        path = []
         
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
    
    # Prints total number of paths from 's' to 'd'
    def printNumPaths(self):
        print('Number of Paths: {}'.format(self.pathsCount))


distinct_vertices = []
for i in paths:
    if i.split('-')[0].strip('\n') not in distinct_vertices:
        distinct_vertices.append(i.split('-')[0].strip('\n'))
    if i.split('-')[1].strip('\n') not in distinct_vertices:
       distinct_vertices.append(i.split('-')[1].strip('\n'))   

g = Graph(distinct_vertices)
for i in paths:
    g.addEdge(i.split('-')[0].strip('\n'), i.split('-')[1].strip('\n'))

g.printAllPaths('start', 'end')

g.printNumPaths()