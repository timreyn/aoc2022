import sys

OPEN = 10
WALL = 11
MISSING = 12

saw_blank = False

data = []
inst = ''
pos = None
width = 0
height = 0

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  if not line.strip():
    saw_blank = True
  if saw_blank:
    inst = line.strip()
  else:
    l = []
    for x in line:
      if x == '.':
        if pos is None:
          pos = (len(data), len(l))
        l += [OPEN]
      elif x == '#':
        l += [WALL]
      else:
        l += [MISSING]
    data += [l]
    height += 1
    width = max(width, len(l))

for row in data:
  while len(row) < width:
    row.append(MISSING)

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = EAST

def get(pos):
  return data[pos[0] % height][pos[1] % width]

idx = 0
while idx < len(inst):
  if inst[idx] == 'R':
    d = (d + 1) % 4
  elif inst[idx] == 'L':
    d = (d - 1) % 4
  else:
    end = idx
    while end < len(inst) and inst[end] != 'R' and inst[end] != 'L':
      end += 1
    amt = int(inst[idx:end])
    idx = end - 1
    for it in range(amt):
      nxt = ((pos[0] + dirs[d][0]) % height, (pos[1] + dirs[d][1]) % width)
      while get(nxt) == MISSING:
        nxt = ((nxt[0] + dirs[d][0]) % height, (nxt[1] + dirs[d][1]) % width)
      if get(nxt) == WALL:
        break
      else:
        pos = nxt
  idx += 1


print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + d)
