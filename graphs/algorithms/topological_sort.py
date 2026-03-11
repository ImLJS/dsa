# Topological Sort

# Topological Sort is a linear ordering of vertices such that for every directed edge u -> v,
# vertex u comes before v in the ordering.

# Topological Sort is only possible in Directed Acyclic Graphs (DAGs).

# Topological Sort can be done using Depth First Search (DFS) or Breadth First Search (BFS).

# Topological Sort can be used to solve problems like scheduling tasks, course prerequisites, and more.

# The time complexity of Topological Sort is O(V + E), where V is the number of vertices and E is the number of edges.

# The space complexity of Topological Sort is O(V), where V is the number of vertices.

# Here is an example of Topological Sort using Depth First Search (DFS):


def topological_sort(graph):  # Depth First Search
    def dfs(node):
        if node in cycle:  # If the node is in the cycle set, return False
            return False
        if node in visited:  # If the node is in the visited set, return True
            return True

        cycle.add(node)  # Add the node to the cycle set
        for neighbor in graph[node]:  # For each neighbor of the node
            if not dfs(neighbor):  # If the neighbor is not visited, return False
                return False
        cycle.remove(node)  # Remove the node from the cycle set

        visited.add(node)
        result.append(node)
        return True

    visited = set()
    cycle = set()
    result = []

    for node in graph:
        if not dfs(node):
            return []  # Cycle detected, return empty list

    return result[::-1]  # Return reversed result for correct topological order


# Example usage:
if __name__ == "__main__":
    # Example graph represented as a dictionary
    example_graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}

    order = topological_sort(example_graph)
    if order:
        print("Topological order:", order)
    else:
        print("No valid topological order exists (cycle detected)")