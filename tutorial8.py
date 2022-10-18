def implies(a, b):
  return not a or b

def kb_1(x1, x2, x3):
  return (x1 or x2) and implies(x1, x3) and (not x2)

def kb_2(x1, x2, x3):
  return (x1 or x3) and implies(x1, not x2)

def alpha_1(x1, x2, x3):
  return x3 or x2

def alpha_2(x1, x2, x3):
  return not x2

def print_truth_table(kb, alpha):
  print('x1    | x2    | x3    | kb    | alpha')
  for x1 in [True, False]:
    for x2 in [True, False]:
      for x3 in [True, False]:
        kb_val = kb(x1, x2, x3)
        alpha_val = alpha(x1, x2, x3)
        # all the (" " * 5 - len(str(x1))) stuff is just to make the print look nice
        # print('-------------------------------------')
        print(f'{str(x1) + " "*(5-len(str(x1)))} | {str(x2) + " "*(5-len(str(x2)))} | {str(x3) + " "*(5-len(str(x3)))} | {str(kb_val) + " "*(5-len(str(kb_val)))} | {alpha_val}')
  


print("------part a--------")
print_truth_table(kb_1, alpha_1)
print()
print("------part b--------")
print_truth_table(kb_2, alpha_2)