# implementing graph using adjacency matrix

def add_vertex(v):
    global graph
    global vertices
    global vertices_no
    if v in vertices:
        print("verix",v,"already exist!")
    else:
        vertices_no+=1
        vertices.append(v)  
        if vertices_no>1: 
            for vertex in graph:
               vertex.append(0)
        temp=[]
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)   

def add_edge(v1, v2, weight):
    global graph
    global vertices_no
    global vertices
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        index1=vertices.index(v1)
        index2=vertices.index(v2)
        graph[index1][index2]=weight

def print_graph():
    global graph
    global vertices_no
    
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j]!=0:
                print(vertices[i],"->",vertices[j],"  with cost = ",graph[i][j])

vertices=[]
graph=[]
vertices_no=0

add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)


add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print_graph()
print("Internal representation of the graph: ", graph)          