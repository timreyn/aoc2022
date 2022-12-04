total = 0

for row in open('input.txt'):
  vals = row.strip().split(',')
  l = [int(x) for x in vals[0].split('-')]
  r = [int(x) for x in vals[1].split('-')]
  all_vals = sorted(l + r)
  if all_vals[0] in l and all_vals[1] in r:
    total += 1
  elif all_vals[0] in r and all_vals[1] in l:
    total += 1

print(total)
