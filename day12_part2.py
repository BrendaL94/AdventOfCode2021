"""https://adventofcode.com/2021 """

# day12 Part 2

from collections import defaultdict
from collections import Counter

file = open("input_day12.txt", "r")
paths = file.readlines()
file.close()

# Graph Class adapted from: https://www.geeksforgeeks.org/find-paths-given-source-destination/
class Graph:
  
    def __init__(self, vertices, distinct_vertices):
        self.V = vertices
        self.distinct_vertices = distinct_vertices
        self.graph = defaultdict(list)
        self.pathsCount = 0
        self.allPaths = []
        
        
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
            if ' '.join(path) not in self.allPaths:
                self.allPaths.append(' '.join(path))
                self.pathsCount += 1
                # print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if (i in visited):
                    if (i.isupper()):
                        visited.append(i)
                        self.printAllPathsUtil(i, d, visited, path)
                        
                    # Part 2: visited small cave second time                
                    else:
                        counter = Counter([x for x in path if x.islower()])
                        mostCommon = counter.most_common(1)
                        iCount = counter[i]
                        if (mostCommon[0][1] < 2):
                            visited.append(i)
                            self.printAllPathsUtil(i, d, visited, path)
                        elif (iCount < 1):
                            visited.append(i)
                            self.printAllPathsUtil(i, d, visited, path)
                        
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        if u not in visited:
            visited.append(u)  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        visited = self.distinct_vertices.copy()
        visited.remove('start')
        
        # Create an array to store paths
        path = []
         
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
    
    # Prints total number of paths from 's' to 'd'
    def printNumPaths(self):
        print('Number of Paths: {}'.format(self.pathsCount))
        # print(self.allPaths)


distinct_vertices = []
for i in paths:
    if i.split('-')[0].strip('\n') not in distinct_vertices:
        distinct_vertices.append(i.split('-')[0].strip('\n'))
    if i.split('-')[1].strip('\n') not in distinct_vertices:
       distinct_vertices.append(i.split('-')[1].strip('\n'))   

g = Graph(len(distinct_vertices), distinct_vertices)
for i in paths:
    g.addEdge(i.split('-')[0].strip('\n'), i.split('-')[1].strip('\n'))

g.printAllPaths('start', 'end')

g.printNumPaths()