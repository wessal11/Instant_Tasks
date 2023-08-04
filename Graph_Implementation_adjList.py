# we will creat a directed and weighted graph
# using an adjacency list

def add_vertix(node):
    global graph
    global vertix_no
    if node in graph:
        print("node ", node,"already exist!")
    else:
        vertix_no+=1
        graph[node]=[]

def Add_WeightedEdges(v1,v2,w):
    global graph
    if v1 not in graph:
        print(v1,"doesn\'t exist in the graph")
    elif v2 not in graph:
        print(v2,"doesn\'t exist in the graph")
    else:
        temp=[v2,w]
        graph[v1].append(temp)

def print_graph():
    global graph
    for node in graph:
        for edge in graph[node]:
            print(node,"->",edge[0],"with weight =",edge[1])
    
graph={}
vertix_no=0
add_vertix('A')
add_vertix('B')
add_vertix('C')
add_vertix('D')
add_vertix('E')

Add_WeightedEdges('A','B',10)
Add_WeightedEdges('A','D',20)
Add_WeightedEdges('B','D',5)
Add_WeightedEdges('C','A',7)
Add_WeightedEdges('D','E',16)
Add_WeightedEdges('E','C',6)

print_graph()

print("The internal graph representation",graph)
