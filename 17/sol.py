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

for i in range(2022 if len(sys.argv) < 3 else int(sys.argv[2])):
  rock = rocks[i % len(rocks)][:]
  if not grid:
    maxy = -1
  else:
    maxy = max([x[0] for x in grid])
  rock = [(r[0] + maxy, r[1]) for r in rock]

  while True:
    # Move horizontally.
    mv = moves[get()]
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

print(maxy + 1)
