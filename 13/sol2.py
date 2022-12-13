data = []

for line in open('input.txt'):
  line = line.strip()
  if line:
    data += [eval(line)]

LESS_THAN = 1
SAME = 2
GREATER_THAN = 3

def compare(l, r):
  if isinstance(l, int) and isinstance(r, int):
    if l < r:
      return LESS_THAN
    if l > r:
      return GREATER_THAN
    if l == r:
      return SAME
  if isinstance(l, int) and isinstance(r, list):
    return compare([l], r)
  if isinstance(l, list) and isinstance(r, int):
    return compare(l, [r])
  if isinstance(l, list) and isinstance(r, list):
    for i in range(min(len(l), len(r))):
      sub = compare(l[i], r[i])
      if sub != SAME:
        return sub
    if len(l) < len(r):
      return LESS_THAN
    if len(l) > len(r):
      return GREATER_THAN
    return SAME

a = 0
b = 0

for x in data + [[[2]], [[6]]]:
  if compare([[2]], x) == GREATER_THAN:
    a += 1
  if compare([[6]], x) == GREATER_THAN:
    b += 1

print((a+1) * (b+1))
