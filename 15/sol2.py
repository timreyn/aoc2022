import re
import sys

f = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
n = int(sys.argv[2]) if len(sys.argv) >= 3 else 4000000

ranges = [list() for i in range(n + 1)]

def AddRange(ranges, r):
  for i in range(len(ranges)):
    rr = ranges[i]
    if r[0] <= rr[1] and rr[0] <= r[1]:
      new = (min(r[0], rr[0]), max(r[1], rr[1]))
      ranges.remove(rr)
      return AddRange(ranges, new)
  ranges.append(r)
  return ranges

for line in open(f):
  m = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line.strip())
  sx, sy = (int(m.group(1)), int(m.group(2)))
  bx, by = (int(m.group(3)), int(m.group(4)))
  print((sx, sy), (bx, by))
  dist = abs(sx - bx) + abs(sy - by)
  for ly in range(n + 1):
    dy = abs(sy - ly)
    if dy <= dist:
      start = sx - (dist - dy)
      end = sx + (dist - dy)
      '''
      commented this out because spots with a beacon can't be the position of the distress beacon
      if ly == by and start == bx:
        start += 1
      if ly == by and end == bx:
        end -= 1
      '''
      if start <= end:
        AddRange(ranges[ly], (start, end))

print('RESULTS')
total = 0
for ly in range(len(ranges)):
  r = sorted(ranges[ly])
  lastx = -1
  for r in sorted(ranges[ly], key=lambda x: x[0]):
    if r[0] > lastx + 1 and lastx + 1 >= 0 and lastx + 1 <= n:
      print((lastx + 1, ly))
      print((lastx + 1) * 4000000 + ly)
    lastx = r[1]
  pass
