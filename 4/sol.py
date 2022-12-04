total = 0

for row in open('input.txt'):
  vals = row.strip().split(',')
  l = [int(x) for x in vals[0].split('-')]
  r = [int(x) for x in vals[1].split('-')]

  if l[0] <= r[0] and l[1] >= r[1]:
    total += 1
  elif r[0] <= l[0] and r[1] >= l[1]:
    total += 1

print(total)
