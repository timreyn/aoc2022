import sys

lines = {}

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  spl = line.strip().split(' ')
  if len(spl) == 2:
    lines[spl[0][:-1]] = int(spl[1])
  else:
    lines[spl[0][:-1]] = spl[1:]

print(lines)

def evl(v1, op, v2):
  if op == '*':
    return v1 * v2
  if op == '+':
    return v1 + v2
  if op == '-':
    return v1 - v2
  if op == '/':
    return v1 // v2

done = False

while not done:
  ints = 0
  for var,val in lines.items():
    if isinstance(val, list):
      if isinstance(lines[val[0]], int) and isinstance(lines[val[2]], int):
        lines[var] = evl(lines[val[0]], val[1], lines[val[2]])
        ints += 1
        if var == 'root':
          done = True
    else:
      ints += 1

print(lines['root'])
