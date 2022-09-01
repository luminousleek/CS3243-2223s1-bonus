graph = {
    'S': {('A', 6)},
    'A': {('B', 1), ('G', 4)},
    'B': {('G', 2)},
    'G': {}
}

def hstar(node):
    # TODO Implement this, can just hardcode here.
    raise NotImplementedError
def h1(node):
    return 0
def h2(node):
    return {'S':8, 'A':1, 'B':1, 'G':0}[node]
def h3(node):
    return {'S':9, 'A':3, 'B':2, 'G':0}[node]
def h4(node):
    return {'S':6, 'A':3, 'B':1, 'G':0}[node]
def h5(node):
    return {'S':8, 'A':4, 'B':2, 'G':0}[node]
def h_q5d(node):
    # TODO Implement this
    raise NotImplementedError

def admissible_constraint(h_val, hstar_val, **kwargs):
    return h_val <= hstar_val

def consistent_constraint(h_val, h_val_successor, cost, **kwargs):
    return h_val <= cost + h_val_successor
    # TODO Implement this
    raise NotImplementedError

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

print_constraint([h1, h2, h3, h4, h5, h_q5d], [admissible_constraint, consistent_constraint], hstar)

from collections import defaultdict
from priority_queue import PriorityQueue # This is the same one as in AIMA
def astar_search(graph, h, goal_test, explored_order):

    cost_fn_g = defaultdict(lambda: 0)
    f = lambda node: cost_fn_g[node] + h(node)
    node = 'S'
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    # TODO Implement this
    raise NotImplementedError

print("A*STAR - Order of the nodes that are explored.")
explored_order = []
astar_search(graph, h4, lambda node: node=='G', explored_order=explored_order)
print('-'.join(explored_order))