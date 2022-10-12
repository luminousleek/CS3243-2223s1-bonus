class Node:
  
  def __init__(self, value, is_term) -> None:
    self.value = value
    self.is_term = is_term
    self.children = list()

  def set_children(self, children):
    self.children = children

  def set_value(self, value):
    self.value = value

v1 = Node('v1', False)
v1.set_children([Node(2, True), Node(4, True)])

v2 = Node('v2', False)
v2.set_children([Node(8, True), Node(3, True), Node(0, True)])

v3 = Node('v3', False)
v3.set_children([Node(3, True), Node(7, True), Node(9, True)])

v4 = Node('v4', False)
v4.set_children([Node(0, True), Node(12, True)])

u1 = Node('u1', False)
u1.set_children([v1, v2])

u2 = Node('u2', False)
u2.set_children([v3, v4, Node(10, True)])

s = Node('s', False)
s.set_children([u1, u2])

def max_value(node: Node, alpha, beta):
  if node.is_term:
    return node.value, None
  v = -1000
  move = None
  for child in node.children:
    v_new, a_new = min_value(child, alpha, beta)
    print(f'max value, curr: {node.value}, child: {child.value}, v_new: {v_new}, alpha: {alpha}, beta: {beta}')
    if v_new > v:
      v, move = v_new, child
      alpha = max(alpha, v)
    if v >= beta:
      print(f'max pruned, curr: {node.value}, child: {child.value}, move: {move.value}')
      return v, move
    print(f'max value, curr: {node.value}, child: {child.value}, alpha: {alpha}, beta: {beta}')
  return v, move

def min_value(node: Node, alpha, beta):
  if node.is_term:
    return node.value, None
  v = 1000
  for child in node.children:
    v_new, a_new = max_value(child, alpha, beta)
    print(f'min value, curr: {node.value}, child: {child.value}, v_new: {v_new}, alpha: {alpha}, beta: {beta}')
    if v_new < v:
      v, move = v_new, child
      beta = min(beta, v)
    if v <= alpha:
      print(f'min pruned, curr: {node.value}, child: {child.value}, move: {move.value}')
      return v, move
    print(f'min value, curr: {node.value}, child: {child.value}, alpha: {alpha}, beta: {beta}')
  return v, move

def ab_search(node: Node):
  value, move = max_value(node, -1000, 1000)
  return move

print(ab_search(s).value)