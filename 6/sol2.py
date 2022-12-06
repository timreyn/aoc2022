for line in open('input.txt'):
  recent = []
  num = 0
  for char in line.strip():
    recent = (recent + [char])[-14:]
    num += 1
    if len(set(recent)) == 14:
      print(num)
      break
