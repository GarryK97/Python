import heapq

"""
Graph implementation for best_trades
"""
class Trade_Graph:
    def __init__(self, num_vertices):
        """
        Initialize Graph object
        :param num_vertices: Total number of vertices
        :Complexity:  Best Time: O(V), Worst Time: O(V), Auxiliary Space: O(V)
                            V = Total number of vertices in graph
        """
        self.vertices = [None for x in range(num_vertices)]
        for i in range(num_vertices):
            self.vertices[i] = Trade_Vertex(i)

    def add_edge(self, edge):
        """
        Adds edge to each vertex, by using Edge object
        :param edge: Edge object to add
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        vertex = self.vertices[edge.u]
        vertex.add_edge(edge)


"""
Vertex implementation for best_trades
"""
class Trade_Vertex:
    def __init__(self, id):
        """
        Initialize Vertex object
        :param id: id of vertex
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        self.id = id
        self.edges = []     # Stores all the edges of a vertex

    def add_edge(self, edge):
        """
        adds an edge to this vertex
        :param edge: Edge object to add
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        self.edges.append(edge)


"""
Edge implementation for best_trades
"""
class Trade_Edge:
    def __init__(self, u, v, w):
        """
        Initialize Edge object
        :param u: Source Vertex (Start Vertex) id
        :param v: Destination Vertex (End Vertex) id
        :param w: Weight of the edge
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        self.u = u  # Source
        self.v = v  # Destination
        self.w = w  # Exchange amount



def best_trades(prices, starting_liquid, max_trades, townspeople):
    """
    Calculates the best trade with the given max_trades, using Bellman-Ford algorithm
    :param prices: List of prices of each Liquid
    :param starting_liquid: Starting Liquid ID
    :param max_trades: Maximum number of trades
    :param townspeople: List of Lists, Trades offered by each people
    :return: the Optimal Profit found
    :Complexity:  Best Time: O(TM), Worst Time: O(TM), Auxiliary Space: O(TM)
                            T = Total number of Trade offers
                            M = Max_trades
    """
    a_graph = Trade_Graph(len(prices))  # Initialize Graph by number of liquids. So, vertex = each liquid

    # Adds all the trade offers as edges to the graph
    for people in townspeople:
        for offer in people:
            u = offer[0]
            v = offer[1]
            w = offer[2]

            a_graph.add_edge(Trade_Edge(u, v, w))

    # Initialize a table for Bellman-Ford algorithm, the table will store the optimal amount of each liquid
    amount = [[float("-inf") for i in range(max_trades+1)] for j in range(len(prices))]
    amount[starting_liquid][0] = 1

    # Starts Bellman-Ford algorithm, repeat Max_trades time
    for i in range(1, max_trades+1):
        for liquid in amount:   # Copy the previous i
            liquid[i] = liquid[i-1]

        for vertex in a_graph.vertices:
            for edge in vertex.edges:   # Relax all the edges
                price_stored = prices[edge.v] * (amount[edge.v][i-1])
                price_new = prices[edge.v] * (amount[edge.u][i-1] * edge.w)
                if price_stored < price_new:    # If new optimal price is found, replace the table.
                    amount[edge.v][i] = amount[edge.u][i-1] * edge.w

    # Gets the maximum price using the table obtained.
    max_price = 0
    for i in range(len(amount)):
        if max_price < amount[i][-1] * prices[i]:
            max_price = amount[i][-1] * prices[i]

    return round(max_price)



# ============================= Q3 ============================


"""
Graph implementation for opt_delivery
"""
class Graph:
    def __init__(self, num_vertices):
        """
        Initialize Graph object
        :param num_vertices: Total number of vertices
        :Complexity:  Best Time: O(V), Worst Time: O(V), Auxiliary Space: O(V)
                            V = Total number of vertices in graph
        """
        self.vertices = [None for x in range(num_vertices)]
        for i in range(num_vertices):
            self.vertices[i] = Vertex(i)

    def add_edges_list(self, edges_list):
        """
        Gets List of edges in (u, v, w) format and adds all the edge to this graph
        :param edges_list: List of edges in (u, v, w) format
        :Complexity:  Best Time: O(E), Worst Time: O(E), Auxiliary Space: O(1)
                            E = Total number of Edges
        """
        for edge in edges_list:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            vertex = self.vertices[u]
            vertex.add_edge(Edge(u, v, w))

            # Adds Undirected edge, simply swap u and v
            vertex2 = self.vertices[v]
            vertex2.add_edge(Edge(v, u, w))

    def get_vertex_byid(self, id):
        """
        Gets the vertex by using its id
        :param id: Vertex id to get
        :return: a Vertex with matching id
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        return self.vertices[id]

    def reset_vertices(self):
        """
        Reset the status of all the vertices in this graph
        :Complexity:  Best Time: O(V), Worst Time: O(V), Auxiliary Space: O(1)
                            V = Total number of vertices in graph
        """
        for vertex in self.vertices:
            vertex.previous = None
            vertex.cost = float("inf")

"""
Vertex implementation for opt_delivery
"""
class Vertex:
    def __init__(self, id):
        """
        Initialize Vertex object
        :param id: the id of Vertex
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        self.id = id
        self.edges = []
        self.previous = None
        self.cost = float("inf")

    def add_edge(self, edge):
        """
        Adds an edge to this vertex, using Edge object
        :param edge: Edge object to add
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        self.edges.append(edge)


"""
Edge implementation for opt_delivery
"""
class Edge:
    def __init__(self, u, v, w):
        """
        Initialize Edge object
        :param u: Source Vertex (Start Vertex) id
        :param v: Destination Vertex (End Vertex) id
        :param w: Weight of the edge
        :Complexity:  Best Time: O(1), Worst Time: O(1), Auxiliary Space: O(1)
        """
        self.u = u  # Source
        self.v = v  # Destination
        self.w = w  # Exchange amount


def opt_delivery(n, roads, start, end, delivery):
    """
    Finds the optimal cost of going to 'end' city from 'start' city.
    :param n: Number of cities
    :param roads: List of tuples (u, v, w), which represents a road
    :param start: the starting city
    :param end: the destination city
    :param delivery: a tuple (u, v, p) represents a delivery.
                    U = pick-up city, V = Delivery Destination, P = Profit of the delivery
    :return: (Optimal cost, Optimal Path) found
    :Complexity:  Best Time: O(V^2), Worst Time: O(V^2), Auxiliary Space: O(V)
                            V = Total number of vertices in graph
    """

    def update_heap(graph, min_heap):
        """
        Updates the heap when the costs of vertices are changed.
        :param graph: Graph object
        :param min_heap: heap to update
        :Complexity:  Best Time: O(V), Worst Time: O(V), Auxiliary Space: O(1)
                            V = Total number of vertices in graph
        """
        for i in range(len(min_heap)):
            vertex_id = min_heap[i][1]
            vertex = graph.vertices[vertex_id]
            min_heap[i] = (vertex.cost, vertex.id)
        heapq.heapify(min_heap)

    def backtrack_path(graph, start, end):
        """
        Backtrack the previous id of vertices and reconstruct the optimal path.
        :param graph: Graph object
        :param start: the source vertex id
        :param end: the destination vertex id
        :return: Reconstructed Path, using backtracking
        :Complexity:  Best Time: O(1), Worst Time: O(V), Best Auxiliary Space: O(1), Worst Auxiliary Space: O(V)
                                            V = Total number of vertices in graph
        """
        if start == end:    # If same start and end, there will be no previous. So return directly to prevent error
            return [end]

        path = []
        path.insert(0, end)
        previous_vertex_id = graph.vertices[end].previous
        previous_vertex = graph.vertices[previous_vertex_id]
        while previous_vertex_id != start:
          path.insert(0, previous_vertex_id)
          previous_vertex_id = graph.vertices[previous_vertex.id].previous
          previous_vertex = graph.vertices[previous_vertex_id]
        path.insert(0, start)
        return path

    def find_lowest_cost(graph, start, end):
        """
        Finds the optimal path that requires the lowest travelling cost from start to end, using Dijkstra algorithm
        :param graph: Graph object
        :param start: the source vertex id
        :param end: the destination vertex id
        :return: Optimal cost and Optimal path found
        :Complexity:  Best Time: O(V^2), Worst Time: O(V^2), Auxiliary Space: O(V)
                            V = Total number of vertices in graph
        """
        graph.reset_vertices()  # Resets the status of all the vertices in the graph before computes
        minheap = []    # a list to implement min heap
        # Initialize the min heap. Each element is a tuple (cost, vertex_id)
        for vertex in graph.vertices:
            if vertex.id == start:
                minheap.append((0, start))
                vertex.cost = 0
            else:
                minheap.append((float("inf"), vertex.id))
        heapq.heapify(minheap)  # Make the list as min heap, O(V) time complexity

        while len(minheap) > 0:  # = Visit every vertex in the graph, O(V) time complexity
            current_cost, current_vid = heapq.heappop(minheap)
            current_vertex = graph.get_vertex_byid(current_vid)
            for edge in current_vertex.edges:   # Go every edge of a vertex
                discovored_vertex = graph.vertices[edge.v]
                discovored_cost = discovored_vertex.cost
                if current_cost + edge.w < discovored_cost:     # if a new optimal cost is found, replace it
                    discovored_vertex.cost = current_cost + edge.w
                    discovored_vertex.previous = current_vertex.id  # Store the previous vertex to reconstruct path later.

            update_heap(graph, minheap)     # Updates the heap after the change of the costs of vertices. O(V) time complexity

        optimal_cost = graph.vertices[end].cost  # Gets the optimal cost
        optimal_path = backtrack_path(graph, start, end)    # Reconstruct the optimal path

        return optimal_cost, optimal_path

    # ====== Actual Codes for opt_delivery
    a_graph = Graph(n)  # Initialize a graph. So, Cities = vertices
    a_graph.add_edges_list(roads)   # Adds roads as edges. So, Roads = Edges

    # Calculates the optimal cost and path without delivery
    optimal_cost_nodelivery, optimal_path_nodelivery = find_lowest_cost(a_graph, start, end)


    # Calculates the optimal cost and path of going start to pick-up city
    optimal_cost_to_pickup, path1 = find_lowest_cost(a_graph, start, delivery[0])

    # Calculates the optimal cost and path of going pick-up to delivery destination city
    optimal_cost_to_deliver, path2 = find_lowest_cost(a_graph, delivery[0], delivery[1])

    # # Calculates the optimal cost and path of going delivery destination city to end city
    optimal_cost_to_end, path3 = find_lowest_cost(a_graph, delivery[1], end)


    # Sum up the cost and path of performing delivery
    optimal_cost_delivery = (optimal_cost_to_pickup + optimal_cost_to_deliver + optimal_cost_to_end) - delivery[2]
    optimal_path_delivery = path1[:-1] + path2 + path3[1:]  # Slicing to prevent adding same path again

    # Compare optimal cost of performing delivery and no delivery.
    if optimal_cost_delivery >= optimal_cost_nodelivery:
        final_optimal_cost = optimal_cost_nodelivery
        final_optimal_path = optimal_path_nodelivery
    else:
        final_optimal_cost = optimal_cost_delivery
        final_optimal_path = optimal_path_delivery

    return final_optimal_cost, final_optimal_path