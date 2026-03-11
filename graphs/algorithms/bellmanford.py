def bellman_ford(edges, vertices, start):
    """
    Simple Bellman-Ford algorithm implementation

    Args:
        edges: List of tuples (from_vertex, to_vertex, weight)
        vertices: Number of vertices in graph
        start: Starting vertex

    Returns:
        distances: List of distances from start to each vertex
    """
    # Step 1: Initialize distances
    distances = [float("inf")] * vertices
    distances[start] = 0

    # Step 2: Relax edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Step 3: Check for negative cycles
    for u, v, w in edges:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            print("Graph contains negative cycle")
            return None

    return distances


# Example usage
if __name__ == "__main__":
    # Example graph
    # Edge format: (from_vertex, to_vertex, weight)
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, -3), (2, 3, 2), (3, 1, 1)]

    num_vertices = 4  # Number of vertices (0 to 3)
    start_vertex = 0  # Starting vertex

    # Run algorithm
    distances = bellman_ford(edges, num_vertices, start_vertex)

    # Print results
    if distances:
        for vertex in range(num_vertices):
            print(
                f"Distance from vertex {start_vertex} to vertex {vertex}: {distances[vertex]}"
            )