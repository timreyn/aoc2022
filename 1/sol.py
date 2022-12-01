most = 0
current = 0

for line in open('input.txt'):
  if not line.strip():
    most = max(most, current)
    current = 0
  else:
    current += int(line.strip())

most = max(most, current)
print(most)
