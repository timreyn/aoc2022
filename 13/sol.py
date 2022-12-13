data = []
current = {}

for line in open('input.txt'):
  line = line.strip()
  if not line:
    data += [current]
    current = {}
  elif 'left' in current:
    current['right'] = eval(line)
  else:
    current['left'] = eval(line)

if current:
  data += [current]

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

total = 0

for i, pair in enumerate(data):
  if compare(pair['left'], pair['right']) == LESS_THAN:
    total += (i + 1)
print(total)
