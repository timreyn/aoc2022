import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

total = 0

vals = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

for line in open(fname):
  val = 0
  for x in line.strip():
    val = val * 5 + vals[x]
  total += val
  print(val)

print(total)

out = ''

while total > 0:
  m = total % 5
  if m in (0, 1, 2):
    out = str(m) + out
    total = total // 5
    continue
  elif m == 3:
    out = '=' + out
    total = total // 5 + 1
  else:
    out = '-' + out
    total = total // 5 + 1

print(out)
