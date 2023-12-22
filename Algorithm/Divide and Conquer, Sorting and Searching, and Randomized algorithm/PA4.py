import random

# Random Contraction Algorithm
def karger_random_contraction_algorithm(graph):
    # while there are more than 2 vertices
    # graph: {vertices, edges}
    while len(graph) > 2:
        # pick a remaining edge (u, v) uniformly at random
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        
        # merge / contract u and v into a single vertex
        # remove self loops
        merge_single_vertex(graph, u, v)
        
    # return cut represented by final 2 vertices
    min_cut = len(list(graph.values())[0])
    return min_cut

# Merge u and v: change the extending edges relations
def merge_single_vertex(graph, u, v):
    # merge v into u
    graph[u].extend(graph[v])

    # replace all v-related edges with u-related edges
    for vertex in graph[v]:
        graph[vertex].remove(v)
        graph[vertex].append(u)
    
    # remove self loops
    graph[u] = [vertex for vertex in graph[u] if vertex != u]
    
    # remove vertex v
    del graph[v]


# Iterate to find the min-cut
def iteration(graph, count):
    min_cut = float("inf")
    for _ in range(count):
        # Make a copy of the graph for each iteration
        current_graph = {k: v[:] for k, v in graph.items()}
        # find the min_cut
        current_min_cut = karger_random_contraction_algorithm(current_graph)
        if current_min_cut < min_cut: min_cut = current_min_cut
        # print(min_cut)
    return min_cut


def main():
    graph = dict()
    fhandle = open("PA4.txt", 'r')
    for line in fhandle:
        vertices = line.split("\t")
        related_vertices = list(map(int, vertices[1:-1]))
        graph[int(vertices[0])] = related_vertices
    fhandle.close()
    # print(graph.items())
    print("Min-cut:", iteration(graph, 1000))

if __name__ == "__main__":
    main()
        