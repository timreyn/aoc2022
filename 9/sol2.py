import sys

LEN = 2 if len(sys.argv) < 2 else int(sys.argv[1])

pos = [[0,0] for i in range(LEN)]
tailpositions = set()
tailpositions.add('%d,%d' % (pos[-1][0], pos[-1][1]))

dirs = {'U': (1,0), 'D': (-1,0), 'L': (0,-1), 'R': (0,1)}

for line in open('input.txt' if len(sys.argv) < 3 else sys.argv[2]):
  dir = dirs[line[0]]
  ct = int(line.strip()[2:])
  for i in range(ct):
    pos[0][0] += dir[0]
    pos[0][1] += dir[1]
    for j in range(LEN - 1):
      delta = [pos[j][0] - pos[j+1][0], pos[j][1] - pos[j+1][1]]
      if abs(delta[0]) > 1 or abs(delta[1])> 1:
        if delta[0] > 0:
          pos[j+1][0] += 1
        elif delta[0] < 0:
          pos[j+1][0] -= 1
        if delta[1] > 0:
          pos[j+1][1] += 1
        elif delta[1] < 0:
          pos[j+1][1] -= 1
    tailpositions.add('%d,%d' % (pos[-1][0], pos[-1][1]))
print(len(tailpositions))
