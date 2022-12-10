import sys

value = 1
lines = [line.strip() for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1])]
total = 0
queue = []

cycle_num = 0
i = 0

while cycle_num < 250:
  cycle_num += 1
  if cycle_num in [20, 60, 100, 140, 180, 220]:
    total += cycle_num * value
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

print(total)
