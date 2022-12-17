import sys

data = ''
for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  data = line.strip()

idx = 0

def get():
  global idx
  out = data[idx]
  idx += 1
  idx = idx % len(data)
  return out

rocks = [
  [(4, 2), (4, 3), (4, 4), (4, 5)],
  [(5, 2), (4, 3), (5, 3), (6, 3), (5, 4)],
  [(4, 2), (4, 3), (4, 4), (5, 4), (6, 4)],
  [(4, 2), (5, 2), (6, 2), (7, 2)],
  [(4, 2), (5, 2), (4, 3), (5, 3)],
]

moves = {'<': -1, '>': 1}

grid = set()

def isvalid(rock):
  for r in rock:
    if r[0] < 0:
      return False
    if r[1] < 0 or r[1] > 6:
      return False
    if r in grid:
      return False
  return True

def cycles(ri, ry):
  for i in range(len(ri) // 3):
    if i == 0:
      continue
    if (ri[-1] - ri[-1 - i] == ri[-1 - i] - ri[-1 - 2 * i] and
        ri[-1 - i] - ri[-1 - 2 * i] == ri[-1 - 2 * i] - ri[-1 - 3 * i] and
        ry[-1] - ry[-1 - i] == ry[-1 - i] - ry[-1 - 2 * i] and
        ry[-1 - i] - ry[-1 - 2 * i] == ry[-1 - 2 * i] - ry[-1 - 3 * i]):
      return ri[-1] - ri[-1 - i],  ry[-1] - ry[-1 - i]
  return 0, 0

reset_i = []
reset_y = []
more_rocks = None
extra_y = 0

for i in range(2022 if len(sys.argv) < 3 else int(sys.argv[2])):
  rock = rocks[i % len(rocks)][:]
  if more_rocks is not None:
    more_rocks -= 1
    if more_rocks < 0:
      break
  if not grid:
    maxy = -1
  else:
    maxy = max([x[0] for x in grid])
  rock = [(r[0] + maxy, r[1]) for r in rock]

  while True:
    # Move horizontally.
    mv = moves[get()]
    if idx == 0 and more_rocks is None:
      reset_i += [i]
      reset_y += [max([x[0] for x in grid])]
      print('reset ' + str(i) + ' ' + str(max([x[0] for x in grid])))
      # The amount added per read through the input seems to be constant,
      # or at least cycle.
      ii, yy = cycles(reset_i, reset_y)
      if ii:
        extra_y = (1000000000000 - i) // ii * yy
        more_rocks = (1000000000000 - i) % ii
        print(str(extra_y) + ' extra height')
        print(str(more_rocks) + ' more rocks')
    newrock = [(r[0], r[1] + mv) for r in rock]
    if isvalid(newrock):
      rock = newrock

    # Move vertically:
    newrock = [(r[0] - 1, r[1]) for r in rock]
    if isvalid(newrock):
      rock = newrock
    else:
      break
  for r in rock:
    grid.add(r)

maxy = max([x[0] for x in grid])
if maxy < 20:
  for i in range(maxy, -1, -1):
    out = '|' + ''.join(['#' if (i, j) in grid else '.' for j in range(7)]) + '|'
    print(out)

print(maxy + extra_y)
