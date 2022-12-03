total = 0

for line in open('input.txt'):
  line = line.strip()
  l = line[:len(line) // 2]
  r = line[len(line) // 2:]
  o = ord(list(set(l).intersection(set(r)))[0])
  if (o > 96):
    total += o - 96
  else:
    total += o - 64 + 26
print(total)
