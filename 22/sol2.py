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

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

for line in open(fname):
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

def move(pos, d):
  if fname == 'input.txt':
    size = 50
    paired_regions = [
      [(0,1), NORTH, (3,0), WEST],
      [(0,1), EAST, (0,2), WEST],
      [(0,1), SOUTH, (1,1), NORTH],
      [(0,1), WEST, (2,0), WEST],
      [(0,2), NORTH, (3,0), SOUTH],
      [(0,2), EAST, (2,1), EAST],
      [(0,2), SOUTH, (1,1), EAST],
      [(1,1), WEST, (2,0), NORTH],
      [(1,1), SOUTH, (2,1), NORTH],
      [(2,0), EAST, (2,1), WEST],
      [(2,0), SOUTH, (3,0), NORTH],
      [(2,1), SOUTH, (3,0), EAST]]
  else:
    size = 4
    paired_regions = [
      [(0,2), NORTH, (1,0), NORTH],
      [(0,2), EAST, (2,3), EAST],
      [(0,2), SOUTH, (1,2), NORTH],
      [(0,2), WEST, (1,1), NORTH],
      [(1,0), EAST, (1,1), WEST],
      [(1,0), SOUTH, (2,2), SOUTH],
      [(1,0), WEST, (2,3), SOUTH],
      [(1,1), EAST, (1,2), WEST],
      [(1,1), SOUTH, (2,2), WEST],
      [(1,2), SOUTH, (2,2), NORTH],
      [(1,2), EAST, (2,3), NORTH],
      [(2,2), EAST, (2,3), WEST]]
  cur_reg = (pos[0] // size, pos[1] // size)
  new_pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
  new_reg = (new_pos[0] // size, new_pos[1] // size)
  if cur_reg == new_reg:
    return new_pos, d
  new_reg = None
  new_side = None
  for p in paired_regions:
    if p[0] == cur_reg and p[1] == d:
      new_reg = p[2]
      new_side = p[3]
      break
    if p[2] == cur_reg and p[3] == d:
      new_reg = p[0]
      new_side = p[1]
      break
  offset = (new_reg[0] * size, new_reg[1] * size)
  cw_pos = 0
  if d == NORTH:
    cw_pos = (pos[1] % size)
  elif d == EAST:
    cw_pos = (pos[0] % size)
  elif d == SOUTH:
    cw_pos = size - (pos[1] % size) - 1
  elif d == WEST:
    cw_pos = size - (pos[0] % size) - 1

  new_pos = None
  if new_side == NORTH:
    new_pos = (offset[0], offset[1] + size - cw_pos - 1)
  elif new_side == EAST:
    new_pos = (offset[0] + size - cw_pos - 1, offset[1] + size - 1)
  elif new_side == SOUTH:
    new_pos = (offset[0] + size - 1, offset[1] + cw_pos)
  elif new_side == WEST:
    new_pos = (offset[0] + cw_pos, offset[1])
  return new_pos, (new_side + 2) % 4

    

def get(pos):
  return data[pos[0]][pos[1]]

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
      nxt, new_dir = move(pos, d)
      if get(nxt) == WALL:
        break
      else:
        pos = nxt
        d = new_dir
  idx += 1


print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + d)
