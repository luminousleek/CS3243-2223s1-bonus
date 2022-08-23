graph = {
    'S': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'E'},
    'D': set(),
    'E': {'D'},
    'A': {'F'},
    'F': {'G'},
    'G': set(),
}

def goal_test_producer(nodes_checked):
    def goal_test(node):
        nodes_checked.append(node)
        return node=='G'
    return goal_test

def dfs_tree(graph, goal_test, start='S'):
    frontier = [start]
    while frontier:
        node = frontier.pop()
        if goal_test(node):
            return node
        frontier.extend(sorted(graph[node]))
    return None

def dfs_graph(graph, goal_test, start='S'):
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop()
        if goal_test(node):
            return node
        explored.add(node)
        frontier.extend(sorted(graph[node] - explored - set(frontier)))
    return None

def bfs_tree(graph, goal_test, start='S'):
    frontier = [start]
    while frontier:
      node = frontier.pop(0) # remove first item from list
      if goal_test(node):
        return node
      frontier.extend(sorted(graph[node]))
    return None

def bfs_graph(graph, goal_test, start='S'):
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop(0) # remove first item from list
        if goal_test(node):
            return node
        explored.add(node)
        frontier.extend(sorted(graph[node] - explored - set(frontier)))
    return None

def print_all(fns):
    for fn in fns:

        print(f"{fn.__name__}: ", end='')
        nodes_checked = []
        fn(graph, goal_test_producer(nodes_checked))
        print('-'.join(nodes_checked))

print_all([dfs_tree, dfs_graph, bfs_tree, bfs_graph])

# Now implement with early goal test to see the difference
def dfs_early_tree(graph, goal_test, start='S'):
    if goal_test(start):
        return start
    frontier = [start]
    while frontier:
        node = frontier.pop()
        for nde in sorted(graph[node]):
            if goal_test(nde):
                return nde
            frontier.append(nde)
    return None

def dfs_early_graph(graph, goal_test, start='S'):
    if goal_test(start):
      return start
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop()
        for nde in sorted(graph[node] - explored - set(frontier)):
          if goal_test(nde):
            return nde
          frontier.append(nde)
        explored.add(node)
    return None

def bfs_early_tree(graph, goal_test, start='S'):
    if goal_test(start):
      return start
    frontier = [start]
    while frontier:
        node = frontier.pop(0)
        for nde in sorted(graph[node]):
          if goal_test(nde):
            return nde
          frontier.append(nde)
    return None

def bfs_early_graph(graph, goal_test, start='S'):
    if goal_test(start):
      return start
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop(0)
        for nde in sorted(graph[node] - explored - set(frontier)):
          if goal_test(nde):
            return nde
          frontier.append(nde)
        explored.add(node)
    return None

print_all([dfs_early_tree, dfs_early_graph, bfs_early_tree, bfs_early_graph])