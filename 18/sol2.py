import sys

pts = set()

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  coords = [int(x) for x in line.strip().split(',')]
  pts.add(tuple(coords))

low = min([min([f[i] for f in pts]) - 1 for i in (0,1,2)])
high = max([max([f[i] for f in pts]) + 1 for i in (0,1,2)])

queue = []
visited = set()
faces = set()

for i in range(low, high + 1):
  for j in range(low, high + 1):
    for k in range(low, high + 1):
      if i == low or i == high or j == low or j == high or k == low or k == high:
        queue += [(i,j,k)]

while queue:
  pt = queue[0]
  queue.pop(0)
  if pt in visited:
    continue
  visited.add(pt)
  for d in ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)):
    newpt = tuple((dd + pp for dd, pp in zip(d, pt)))
    if min(newpt) < low or max(newpt) > high:
      continue
    if newpt in pts:
      faces.add(tuple((dd / 2 + pp for dd, pp in zip(d, pt))))
    else:
      queue += [newpt]

print(len(faces))
