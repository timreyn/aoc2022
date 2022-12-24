import math
import sys

grid = []

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  if '##' not in line:
    grid += [line[1:-2]]

def is_accessible(i, j, turn):
  for di, dj, ch in ((1,0,'v'), (-1,0,'^'), (0,1,'>'), (0,-1,'<')):
    ii = (i - turn * di) % len(grid)
    jj = (j - turn * dj) % len(grid[0])
    if grid[ii][jj] == ch:
      return False
  return True

cycles = len(grid) * len(grid[0]) // math.gcd(len(grid), len(grid[0]))

def run(init_i, init_j, init_t, target_i, target_j):
  depths = {}
  queue = [(init_i,init_j,x) for x in range(cycles) if is_accessible(init_i, init_j, x)]
  for i, j, t in queue:
    depths[(i, j, t)] = (t - init_t) % cycles + init_t
    if (t - init_t) % cycles == 0:
      depths[(i, j, t)] = cycles + init_t
  queue.sort(key=lambda x: depths[x])
  
  while queue:
    n = queue.pop(0)
    best = depths[n]
    for di, dj in ((0,1), (0,-1), (1,0), (-1,0), (0,0)):
      ni = n[0] + di
      nj = n[1] + dj
      t = best + 1
      if ni < 0 or ni >= len(grid):
        continue
      if nj < 0 or nj >= len(grid[0]):
        continue
      if not is_accessible(ni, nj, t):
        continue
      if (ni, nj, t % cycles) in depths:
        continue
      depths[(ni, nj, t % cycles)] = t
      if ni == target_i and nj == target_j:
        return t + 1
        
      queue += [(ni, nj, t % cycles)]
      queue.sort(key=lambda x: depths[x])
    print(len(queue))

t1 = run(0, 0, 0, len(grid) - 1, len(grid[0]) - 1)
print(t1)
t2 = run(len(grid) - 1, len(grid[0]) - 1, t1, 0, 0)
print(t2)
t3 = run(0, 0, t2, len(grid) - 1, len(grid[0]) -1)
print(t3)
