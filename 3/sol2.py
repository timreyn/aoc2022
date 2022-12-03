total = 0
current = []

for line in open('input.txt'):
  line = line.strip()
  current += [line]
  if len(current) < 3:
    continue
  vals = set(current[0])
  for c in current:
    vals = vals.intersection(set(c))
  o = ord(list(vals)[0])
  if (o > 96):
    total += o - 96
  else:
    total += o - 64 + 26
  current = []
print(total)
