most = []
current = 0

for line in open('input.txt'):
  if not line.strip():
    most = sorted(most + [current], reverse=True)[:3]
    current = 0
  else:
    current += int(line.strip())

most = sorted(most + [current], reverse=True)[:3]
print(sum(most))
