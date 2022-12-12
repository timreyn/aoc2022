grid = []
start = None
for line in open('input.txt'):
  gridline = []
  for char in line.strip():
    if char == 'S':
      gridline += [0]
    elif char == 'E':
      start = (len(grid), len(gridline))
      gridline += [25]
    else:
      gridline += [ord(char) - 97]
  grid += [gridline]

optimal = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
optimal[start[0]][start[1]] = 0

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def valid_moves(pos):
  val = grid[pos[0]][pos[1]]
  for d in dirs:
    nextpos = (pos[0] + d[0], pos[1] + d[1])
    if nextpos[0] < 0 or nextpos[1] < 0 or nextpos[0] >= len(grid) or nextpos[1] >= len(grid[0]):
      continue
    nextval = grid[nextpos[0]][nextpos[1]]
    if nextval >= val - 1:
      yield nextpos

queue = [start]

while queue:
  p = queue[0]
  queue = queue[1:]
  opt = optimal[p[0]][p[1]]
  for pp in valid_moves(p):
    cur_opt = optimal[pp[0]][pp[1]]
    if cur_opt == -1 or opt + 1 < cur_opt:
      optimal[pp[0]][pp[1]] = opt + 1
      queue += [pp]

best = 9999999

for x in range(len(grid)):
  for y in range(len(grid[x])):
    if grid[x][y] == 0 and optimal[x][y] > 0 and optimal[x][y] < best:
      best = optimal[x][y]
print(best)
