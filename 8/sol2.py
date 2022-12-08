import sys

grid = []

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  grid += [[int(x) for x in line.strip()]]

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1,0)]

best_score = 0

for i in range(len(grid)):
  for j in range(len(grid[i])):
    score = 1
    for direc in DIRECTIONS:
      this_score = 0
      ii = i + direc[0]
      jj = j + direc[1]
      while ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[i]):
        this_score += 1
        if grid[ii][jj] >= grid[i][j]:
          break
        ii += direc[0]
        jj += direc[1]
      score *= this_score
    if score >= best_score:
      print(i, j, score)
      best_score = score

print(best_score)
