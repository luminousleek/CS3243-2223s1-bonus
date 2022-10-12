def goal_test_producer(nodes_checked):
    def goal_test(node):
        nodes_checked.append(node)
        return node=='G'
    return goal_test

def depth_limited_search(graph, goal_test, limit=50):
    """[Figure 3.17]"""

    def recursive_dls(node, graph, limit, frontier):
        if goal_test(node):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            frontier = set([ (s, 2-(limit-1)) for s in graph[node] ]).union(frontier)
            for child in sorted(graph[node]):
                print("\t" * (2-(limit-1)), f"Frontier: {frontier}")
                print("\t" * (2-(limit-1)), f"Pop: {child}")
                frontier.remove((child, 2-(limit-1)))
                result = recursive_dls(child, graph, limit - 1, frontier)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls('S', graph, limit=limit, frontier=set())

# Code credits - https://github.com/luminousleek/CS3243-2223s1-bonus
# Modified from one of students' submission
def bfs_early_graph(graph, goal_test, start='S'):
    if goal_test(start):
      return start
    explored, frontier = set([start]), [start]
    while frontier:
        print("Frontier:", frontier)
        node = frontier.pop(0)
        print("Pop from frontier", node)
        print("Reached:", sorted(explored))
        for child in sorted(graph[node] - explored - set(frontier)):
            if goal_test(child):
                return child
            frontier.append(child)
            explored.add(child)
        print()
    return None

print("==========Q2a depth_limited_search==========")
graph = {
    'S': {'A', 'B', 'D'},
    'A': {'S', 'C'},
    'B': {'S', 'D'},
    'C': {'A', 'D', 'G'},
    'D': {'S', 'B', 'C', 'E'},
    'E': {'D', 'G'},
    'G': set()
}
print("\t" * (0), f"Frontier: {[('S',0)]}")
print("\t" * (0), 'Pop: S')
print(depth_limited_search(graph, goal_test_producer([]), 2))
print()

print("==========Q2bi bfs_early_graph==========")
bfs_early_graph(graph, goal_test_producer([]), 'S')
print()

from collections import defaultdict
from priority_queue import PriorityQueue # This is the same one as in AIMA
def astar_search_graphv1_late(graph, h, goal_test, explored_order):

    cost_fn_g = defaultdict(lambda: 0)
    f = lambda node: cost_fn_g[node] + h(node)
    node = 'S'
    path_dict = {'S':''}
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set(['S'])
    # raise NotImplementedError
    print("Frontier: ", [ (s, v, path_dict[s]) for v,s in frontier.heap])
    print(f"Reached: {explored}\n")
    while frontier:
        node = frontier.pop()
        explored_order.append(node)
        if goal_test(node):
            return path_dict[node] + node
        for child, cost in graph[node]:
            # if child not in explored:
            #     print(child, f(child))
            if child not in explored:
                cost_fn_g[child] = cost + cost_fn_g[node]
                explored.add(child)
                if child not in frontier:
                    frontier.append(child)
                    path_dict[child] = path_dict[node] + node
                    # print(f"Insert {child}")
                else:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
                        path_dict[child] = path_dict[node] + node
                        print(f"Update {child}")
        print("Pop:", node)
        print(f"Explored: {explored}")
        print("Frontier: ", [ (s, v, path_dict[s]) for v,s in frontier.heap])
        print()
    return None

print("==========Q2bii astar_search_graphv1_late==========")
graph = {
    'S': {('A', 5), ('B', 4), ('D', 10)},
    'A': {('S', 5), ('C',2)},
    'B': {('S', 4), ('D', 6)},
    'C': {('A', 2), ('D', 2), ('G', 7)},
    'D': {('S', 10), ('B', 6), ('C', 2), ('E', 3)},
    'E': {('D', 3), ('G', 1)},
    'G': set()
}

def h(node):
    return {'S':12, 'A':5, 'B':7, 'C':6, 'D':3, 'E':1, 'G':0}[node]

explored_order = []
astar_search_graphv1_late(graph, h, lambda node: node=='G', explored_order=explored_order)
print(explored_order)
print()

def astar_search(graph, h, goal_test, explored_order):

    cost_fn_g = defaultdict(lambda: 0)
    f = lambda node: cost_fn_g[node] + h(node)
    node = 'S'
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    path_dict = {'S':''}
    explored = set()
    # raise NotImplementedError
    while frontier:
        node = frontier.pop()
        explored_order.append(node)
        if goal_test(node):
            return path_dict[node] + node
        explored.add(node)
        for child, cost in graph[node]:
            cost_fn_g[child] = cost + cost_fn_g[node]
            if child not in explored and child not in frontier:
                frontier.append(child)
                path_dict[child] = path_dict[node] + node
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
                    path_dict[child] = path_dict[node] + node
    return None

print("==========Q2biii astar_search==========")
print("Optimal path:", astar_search(graph, h, lambda node: node=='G', explored_order=explored_order))
print()

def admissible_constraint(h_val, hstar_val, **kwargs):
    return h_val <= hstar_val

def consistent_constraint(h_val, h_val_successor, cost, **kwargs):
    return h_val <= cost + h_val_successor
    # TODO Implement this
    # raise NotImplementedError
    return False

def print_constraint(h_fns, constraint_fns, hstar_fn, show_violation=False):
    for h_fn in h_fns:
        print(f"{h_fn.__name__}")
        for constraint_fn in constraint_fns:
            constraint_satisfied = True
            for node, edges in graph.items():
                for successor_node, cost in edges:
                    # constraint must be true for all edges
                    constraint_satisfied &= constraint_fn(h_val=h_fn(node), h_val_successor=h_fn(successor_node), hstar_val=hstar_fn(node), cost=cost)
                    if not constraint_satisfied and show_violation:
                        print(f"Violation - {node}--{cost}-->{successor_node}")
            print(f"{constraint_fn.__name__} = {constraint_satisfied}")

print("==========Q2biv Is the heuristic given consistent?==========")
print_constraint([h], [consistent_constraint], h, show_violation=True)
print()

# print_all([dfs_early_tree, dfs_early_graph, bfs_early_tree, bfs_early_graph])
print("==========Q2bv w*g(n)+ (1-w)*h(n)==========")
w = 0.3

def astar_search_graphv1_late(graph, h, goal_test, explored_order):

    cost_fn_g = defaultdict(lambda: 0)
    def f(node):
        f_val = w*cost_fn_g[node] + (1-w)*h(node)
        print(f"f({node}) = {f_val}")
        return f_val
    node = 'S'
    path_dict = {'S':''}
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set(['S'])
    # raise NotImplementedError
    while frontier:
        node = frontier.pop()
        explored_order.append(node)
        if goal_test(node):
            return path_dict[node] + node
        for child, cost in graph[node]:
            # if child not in explored:
            #     print(child, f(child))
            if child not in explored:
                cost_fn_g[child] = cost + cost_fn_g[node]
                explored.add(child)
                if child not in frontier:
                    frontier.append(child)
                    path_dict[child] = path_dict[node] + node
                else:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
                        path_dict[child] = path_dict[node] + node
    return None

def h(node):
    return {'S':9, 'A':1, 'G':0}[node]

graph = {
    'S': {('G', 10), ('A', 8)},
    'A': {('G', 1)},
    'G': set()
}

print("Non-optimal path", astar_search_graphv1_late(graph, h, lambda node: node=='G', explored_order=[]))