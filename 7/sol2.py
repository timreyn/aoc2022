total = 0
def set_size(pwd, tree, fname, size):
  if pwd:
    if pwd[0] not in tree:
      tree[pwd[0]] = {}
    set_size(pwd[1:], tree[pwd[0]], fname, size)
  else:
    tree[fname] = size

pwd = []
tree = {}
for line in open('input.txt'):
  spl = line.strip().split(' ')
  if len(spl) > 1 and spl[1] == 'cd':
    if spl[2] == '/':
      pwd = []
    elif spl[2] == '..':
      pwd = pwd[:-1]
    else:
      pwd += [spl[2]]
  elif len(spl) > 1 and spl[1] == 'ls':
    pass
  else:
    if spl[0] == 'dir':
      pass
    else:
      total += int(spl[0])
      set_size(pwd, tree, spl[1], int(spl[0]))

target = total - (70000000 - 30000000)

best = 70000000

def get_size(t):
  global best
  cur_sum = 0
  for a in t:
    if type(t[a]) is dict:
      cur_sum += get_size(t[a])
    else:
      cur_sum += t[a]
  if cur_sum >= target and cur_sum < best:
    best = cur_sum
  return cur_sum

get_size(tree)
print(best)
