#CIT-223-054/2024
#STEPHEN MUIGA KIRAGU

# A* SEARCH ALGORITHM
# This program finds the shortest path from a start node
# to a goal node using the A* Search Algorithm.

# Formula:
# f(n) = g(n) + h(n)
# g(n) = actual cost from start node
# h(n) = estimated cost to goal (heuristic)

import heapq

# Graph representation
# Each node has neighbors with travel cost
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

def a_star(start, goal):

    # Priority queue
    open_list = []

    # Add starting node
    heapq.heappush(open_list, (0, start))

    # Store shortest known path cost
    g_cost = {
        start: 0
    }

    # Store parent nodes
    parent = {
        start: None
    }

    while open_list:

        # Get node with smallest f(n)
        current_f, current_node = heapq.heappop(open_list)

        print(f"\nVisiting Node: {current_node}")

        # Goal reached
        if current_node == goal:

            path = []

            while current_node:
                path.append(current_node)
                current_node = parent[current_node]

            path.reverse()

            return path

        # Explore neighbors
        for neighbor, cost in graph[current_node]:

            # Calculate new path cost
            new_g = g_cost[current_node] + cost

            # If better path found
            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                # f(n) = g(n) + h(n)
                f_cost = new_g + heuristic[neighbor]

                # Add to priority queue
                heapq.heappush(open_list, (f_cost, neighbor))

                # Save parent
                parent[neighbor] = current_node

                print(f"Adding {neighbor} with f(n) = {f_cost}")

    return None

# Run A*
path = a_star('A', 'G')

print("\nShortest Path Found:")
print(" -> ".join(path))