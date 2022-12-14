import collections

EMPTY = 0
SAND = 1
ROCK = 2

grid = collections.defaultdict(lambda: collections.defaultdict(lambda: EMPTY))
max_y = None

for line in open('input.txt'):
  spl = line.strip().split(' -> ')
  for i in range(len(spl) - 1):
    first = [int(x) for x in spl[i].split(',')]
    second = [int(x) for x in spl[i + 1].split(',')]
    delta = [(s - f) / abs(s - f) if s != f else 0 for f,s in zip(first,second)]
    pt = first
    while pt[0] != second[0] or pt[1] != second[1]:
      grid[pt[0]][pt[1]] = ROCK
      pt[0] += delta[0]
      pt[1] += delta[1]
      if max_y is None or pt[1] > max_y:
        max_y = pt[1]
    grid[pt[0]][pt[1]] = ROCK

num = 0

done = False

while not done:
  pt = (500, 0)
  while True:
    found = False
    for d in ((0,1), (-1,1), (1,1)):
      nextpt = ((pt[0] + d[0]), (pt[1] + d[1]))
      if grid[nextpt[0]][nextpt[1]] == EMPTY:
        found = True
        break
    if found:
      pt = nextpt
    if not found:
      grid[pt[0]][pt[1]] = SAND
      if pt[0] == 500 and pt[1] == 0:
        done = True
      num += 1
      break
    if pt[1] == max_y + 1:
      grid[pt[0]][pt[1]] = SAND
      num += 1
      break

print(num)
