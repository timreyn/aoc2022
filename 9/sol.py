import sys

head = [0,0]
tail = [0,0]
tailpositions = set()
tailpositions.add('%d,%d' % (tail[0], tail[1]))

dirs = {'U': (1,0), 'D': (-1,0), 'L': (0,-1), 'R': (0,1)}

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  dir = dirs[line[0]]
  ct = int(line.strip()[2:])
  for i in range(ct):
    head[0] += dir[0]
    head[1] += dir[1]
    delta = (head[0] - tail[0], head[1] - tail[1])
    if abs(delta[0]) == 2:
      tail[0] += delta[0] / 2
      tail[1] += delta[1]
    elif abs(delta[1]) == 2:
      tail[1] += delta[1] / 2
      tail[0] += delta[0]
    tailpositions.add('%d,%d' % (tail[0], tail[1]))
print(len(tailpositions))
