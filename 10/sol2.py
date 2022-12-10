import sys

value = 1
lines = [line.strip() for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1])]
queue = []
out = ''

i = 0

for cycle_num in range(240):
  if abs(value - len(out)) <= 1:
    out += '#'
  else:
    out += '.'
  if len(out) == 40:
    print(out)
    out = ''
  if queue:
    value += queue[0]
    queue = []
  else:
    line = lines[i] if i < len(lines) else 'noop'
    i += 1
    if line == 'noop':
      continue
    else:
      queue += [int(line.split(' ')[-1])]
