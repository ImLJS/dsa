# Prims Algorithm for Minimum Spanning Tree

# Prim's Algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
# This algorithm maintains a set of vertices that have been visited and a set of vertices that have not been visited.
# The algorithm starts with an arbitrary vertex and adds the vertex with the smallest edge weight to the visited set.
# The algorithm continues to add the vertex with the smallest edge weight to the visited set until all vertices have been visited.
# The algorithm uses a min heap to keep track of the vertices that have not been visited and the edge weights between the visited and unvisited vertices.
# The algorithm returns the total weight of the minimum spanning tree.

# Time Complexity: O(E log V)
# Space Complexity: O(V)

# Prim's Algorithm using min heap

from heapq import heappush, heappop


def prims_algorithm(n, get_edge_weight):
    """
    Template for Prim's Algorithm using min heap

    Args:
        n: Number of vertices (0 to n-1)
        get_edge_weight: Function that returns weight between two vertices

    Returns:
        Total weight of the Minimum Spanning Tree
    """
    seen = set()  # Set of vertices that have been visited
    total_cost = 0  # Total weight of the Minimum Spanning Tree
    min_heap = [(0, 0)]  # (weight, vertex)

    while len(seen) < n:  # Continue until all vertices have been visited
        weight, curr_vertex = heappop(
            min_heap
        )  # Get the vertex with the smallest edge weight

        if curr_vertex in seen:  # Skip if the vertex has already been visited
            continue

        seen.add(curr_vertex)  # Add the vertex to the visited set
        total_cost += weight  # Add the edge weight to the total cost

        for next_vertex in range(
            n
        ):  # Add the vertices that have not been visited to the min heap
            if next_vertex not in seen:  # Skip if the vertex has already been visited
                edge_weight = get_edge_weight(
                    curr_vertex, next_vertex
                )  # Get the edge weight between the two vertices
                heappush(
                    min_heap, (edge_weight, next_vertex)
                )  # Add the edge weight and the vertex to the min heap

    return total_cost  # Return the total weight of the Minimum Spanning Tree


# Example for points problem:
def minCostConnectPoints(points):  # points = [[x1, y1], [x2, y2], ...]
    def get_manhattan_distance(
        i, j
    ):  # Function to calculate the Manhattan distance between two points
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    return prims_algorithm(len(points), get_manhattan_distance)