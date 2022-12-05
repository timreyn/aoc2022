import re

state = [[] for i in range(9)]

for line in open('input.txt'):
  line = line.rstrip()
  if '[' in line:
    for i in range(9):
      if len(line) >= i * 4 + 2:
        nextval = line[i * 4 + 1]
        if nextval != ' ':
          state[i].insert(0, nextval)
  elif 'move' in line:
    m = re.match('move ([0-9]*) from ([0-9]*) to ([0-9]*)', line)
    to_move = int(m.group(1))
    fr = int(m.group(2))
    to = int(m.group(3))
    state[to - 1] += state[fr - 1][-1 * to_move:]
    for i in range(to_move):
      state[fr - 1].pop()

print(state)
print(''.join([s[-1] for s in state]))
