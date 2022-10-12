class Node:
  
  def __init__(self, value, is_term) -> None:
    self.value = value
    self.is_term = is_term
    self.children = list()
    self.next = None

  def set_children(self, children):
    self.children = children

  def set_value(self, value):
    self.value = value

  def set_next(self, next):
    self.next = next

  def print_path(self):
    if self.is_term:
      return str(self.value)

    return self.value + ', ' + self.next.print_path()

c1 = Node('c1', False)
c1.set_children([Node(8, True), Node(7, True)])

c2 = Node('c2', False)
c2.set_children([Node(3, True), Node(9, True)])

c3 = Node('c3', False)
c3.set_children([Node(9, True), Node(8, True)])

c4 = Node('c4', False)
c4.set_children([Node(2, True), Node(4, True)])

c5 = Node('c5', False)
c5.set_children([Node(1, True), Node(8, True)])

c6 = Node('c6', False)
c6.set_children([Node(8, True), Node(9, True)])

c7 = Node('c7', False)
c7.set_children([Node(9, True), Node(9, True)])

c8 = Node('c8', False)
c8.set_children([Node(3, True), Node(4, True)])

b1 = Node('b1', False)
b1.set_children([c1, c2])

b2 = Node('b2', False)
b2.set_children([c3, c4])

b3 = Node('b3', False)
b3.set_children([c5, c6])

b4 = Node('b4', False)
b4.set_children([c7, c8])

a1 = Node('a1', False)
a1.set_children([b1, b2])

a2 = Node('a2', False)
a2.set_children([b3, b4])

s = Node('s', False)
s.set_children([a1, a2])

def max_value(node: Node, alpha, beta):
  if node.is_term:
    return node.value, None
  max_eval = -1000
  move = None
  for child in node.children:
    eval, a_new = min_value(child, alpha, beta)
    if eval > max_eval:
      max_eval, move = eval, child
      node.set_next(move)
      alpha = max(alpha, max_eval)
    if max_eval >= beta:
      print(f'max pruned, curr: {node.value}, pruned branches: {[nde.value for nde in node.children[node.children.index(child) + 1:]]}')
      return max_eval, move
  return max_eval, move

def min_value(node: Node, alpha, beta):
  if node.is_term:
    return node.value, None
  min_eval = 1000
  for child in node.children:
    eval, a_new = max_value(child, alpha, beta)
    if eval < min_eval:
      min_eval, move = eval, child
      node.set_next(move)
      beta = min(beta, min_eval)
    if min_eval <= alpha:
      print(f'min pruned, curr: {node.value}, pruned branches: {[nde.value for nde in node.children[node.children.index(child) + 1:]]}')
      return min_eval, move
  return min_eval, move

def ab_search(node: Node):
  value, move = max_value(node, -1000, 1000)
  return move

next = ab_search(s)
print(f'path to optimum: {s.print_path()}')
