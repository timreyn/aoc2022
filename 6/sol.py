for line in open('input.txt'):
  recent = []
  num = 0
  for char in line.strip():
    recent = (recent + [char])[-4:]
    num += 1
    if len(set(recent)) == 4:
      print(num)
      break
