import sys

grid = []

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  grid += [[int(x) for x in line.strip()]]

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1,0)]

total = 0

for i in range(len(grid)):
  for j in range(len(grid[i])):
    visible = False
    for direc in DIRECTIONS:
      visible_this_dir = True
      ii = i + direc[0]
      jj = j + direc[1]
      while ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[i]):
        if grid[ii][jj] >= grid[i][j]:
          visible_this_dir = False
        ii += direc[0]
        jj += direc[1]
      if visible_this_dir:
        visible = True
    if visible:
      total += 1
print(total)
