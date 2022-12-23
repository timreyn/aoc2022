import collections
import sys

pts = set()

should_draw = 'draw' in sys.argv

def bounds(ps):
  p = list(ps)[0]
  mini = p[0]
  maxi = p[0]
  minj = p[1]
  maxj = p[1]
  for p in ps:
    mini = min(p[0], mini)
    maxi = max(p[0], maxi)
    minj = min(p[1], minj)
    maxj = max(p[1], maxj)
  return mini, maxi, minj, maxj

def draw(ps):
  mini, maxi, minj, maxj = bounds(ps)
  for i in range(mini, maxi + 1):
    out = ''
    for j in range(minj, maxj + 1):
      if (i, j) in ps:
        out += '#'
      else:
        out += '.'
    print(out)
  print()


for i, line in enumerate(open('input.txt' if len(sys.argv) < 2 else sys.argv[1])):
  for j, val in enumerate(line.strip()):
    if val == '#':
      pts.add((i, j))

if should_draw:
  draw(pts)

dirs = [
  [(-1, -1), (-1, 0), (-1, +1), 'N'], # NORTH
  [(1, -1), (1, 0), (1, 1), 'S'], # SOUTH
  [(-1, -1), (0, -1), (1, -1), 'W'], # WEST
  [(-1, 1), (0, 1), (1, 1), 'E'], # EAST
]

for mv in range(int(10 if len(sys.argv) < 3 else sys.argv[2])):
  moves = {}
  targets = collections.defaultdict(int)

  for i, j in pts:
    if should_draw:
      print('considering (%d,%d)' % (i,j))
    newpt = None
    count = 0
    for ii in range(i-1, i+2):
      for jj in range(j-1, j+2):
        if (ii, jj) in pts:
          count += 1
    if count == 1:
      if should_draw:
        print('  skipping')
      continue
    for ds in dirs:
      if should_draw:
        print('  considering ' + ds[-1])
      valid = True
      for idx, d in enumerate(ds[:-1]):
        if (i + d[0], j + d[1]) in pts:
          if should_draw:
            print('  %d failed' % idx)
          valid = False
          break
      if valid:
        newpt = (i + ds[1][0], j + ds[1][1])
        if should_draw:
          print('    moving %s to (%d, %d)' % (ds[3], newpt[0], newpt[1]))
        break
    if newpt is not None:
      moves[(i,j)] = newpt
      targets[newpt] += 1

  dirs = dirs[1:] + [dirs[0]]
  newpts = set()
  
  for old in pts:
    if old not in moves:
      newpts.add(old)
    else:
      new = moves[old]
      if targets[new] > 1:
        newpts.add(old)
      else:
        newpts.add(new)

  pts = newpts
  if should_draw:
    draw(pts)

mini, maxi, minj, maxj = bounds(pts)
print((maxi - mini + 1) * (maxj - minj + 1) - len(pts))
