import itertools

class Constraint:

  def __init__(self, left_mul, right_mul, op, name) -> None:
    self.left_mul = left_mul
    self.right_mul = right_mul
    self.op = op
    self.name = name

  def eval(self, left_val, right_val):
    left = left_val * self.left_mul
    right = right_val * self.right_mul
    if self.op == 'eq':
      return left == right
    elif self.op == 'gt':
      return left > right
    elif self.op == 'lt':
      return left < right
    elif self.op == 'gte':
      return left >= right
    elif self.op == 'lte':
      return left <= right
    else:
      return False


def check_ac(left_dom, right_dom, constraint: Constraint):
  new_left_dom = set()
  for left in left_dom:
    for right in right_dom:
      if constraint.eval(left, right):
        new_left_dom.add(left)
        break

  return new_left_dom


domains = {
  'a': set([1, 2, 3, 4]),
  'b': set([1, 2, 3, 4]),
  'c': set([1, 2, 3, 4])
}

ab = Constraint(2, 1, 'eq', 'ab')
ba = Constraint(1, 2, 'eq', 'ba')
bc = Constraint(1, 1, 'gte', 'bc')
cb = Constraint(1, 1, 'lt', 'cb')
ac = Constraint(1, 1, 'lt', 'ac')
ca = Constraint(1, 1, 'gte', 'ca')

queue = [ab, ba, bc, cb, ca, ac]
# print(f'initial: {domains}')
while queue:
  constraint = queue.pop(0)
  left_dom = domains[constraint.name[0]]
  right_dom = domains[constraint.name[1]]
  domains[constraint.name[0]] = check_ac(left_dom, right_dom, constraint)
  # print(f'arc: {constraint.name}, domains: {domains}')

print(domains)
lsts = [list(domains[x]) for x in domains]

min = 1000
soln = set()
for element in itertools.product(*lsts):
  a, b, c = element[0], element[1], element[2]
  if 2 * a == b and c < b and c >= a:
    sum = a + b + c
    if sum < min:
      min = sum
      soln = element

print(soln)