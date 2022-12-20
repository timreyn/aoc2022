import sys

data = []
key = 811589153

for i, line in enumerate(open('input.txt' if len(sys.argv) < 2 else sys.argv[1])):
  data += [[int(line.strip()) * key, i]]

l = len(data)

for it in range(10):
  for i in range(l):
    for j in range(l):
      if data[j][1] == i:
        val = data.pop(j)
        newpos = (j + val[0]) % (l-1)
        if newpos == 0 and val[0] < 0:
          newpos = l-1
        data.insert(newpos, val)
        break

for i in range(len(data)):
  if data[i][0] == 0:
    print(data[(i + 1000) % l][0] + data[(i + 2000) % l][0] + data[(i + 3000) % l][0])
