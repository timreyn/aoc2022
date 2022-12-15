import re
import sys

f = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
ly = int(sys.argv[2]) if len(sys.argv) >= 3 else 2000000

ranges = []

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
  dist = abs(sx - bx) + abs(sy - by)
  dy = abs(sy - ly)
  if dy <= dist:
    start = sx - (dist - dy)
    end = sx + (dist - dy)
    if ly == by and start == bx:
      start += 1
    if ly == by and end == bx:
      end -= 1
    if start <= end:
      AddRange(ranges, (start, end))

print(ranges)
total = 0
for r in ranges:
  total += r[1] - r[0] + 1
print(total)
