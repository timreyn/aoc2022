import collections
import re
import sys

class Valve(object):
  def __init__(self, line):
    match = re.match('Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
    self.id = match.group(1)
    self.flow = int(match.group(2))
    self.out = match.group(3).split(', ')

  def str(self):
    return '<id:%s flow:%d out:[%s]>' % (self.id, self.flow, ','.join(self.out))

class State(object):
  def __init__(self, valves, distances):
    self.open = []
    self.score = 0
    self.times = [0, 0]
    self.valves = valves
    self.curs = ['AA', 'AA']
    self.distances = distances

  def move_to_and_open(self, valve, idx):
    state = State(self.valves, self.distances)
    state.open = self.open[:] + [valve]
    state.times = self.times[:]
    state.curs = self.curs[:]
    state.times[idx] += self.distances[self.curs[idx]][valve] + 1
    state.score = self.score + (26 - state.times[idx]) * self.valves[valve].flow
    state.curs[idx] = valve
    return state

  def max_possible(self):
    out = self.score
    for v in self.distances:
      v = self.valves[v]
      if v.flow == 0 or v.id in self.open:
        continue
      best = 0
      for idx in [0, 1]:
        if self.times[idx] + self.distances[self.curs[idx]][v.id] < 26:
          best = max(best, 26 - self.times[idx] - self.distances[self.curs[idx]][v.id] - 1)
      out += best * v.flow
    return out

  def str(self):
    return '<open:[%s] score:%d time:[%s] cur:[%s]>' % (','.join(self.open), self.score, ','.join([str(x) for x in self.times]), ','.join(self.curs))

valves = {}
visited = []

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  valve = Valve(line.strip())
  valves[valve.id] = valve

distances = collections.defaultdict(dict)

for v in valves.values():
  if v.flow == 0 and v.id != 'AA':
    continue
  distances[v.id][v.id] = 0
  queue = [v.id]
  while queue:
    n = queue.pop(0)
    for m in valves[n].out:
      if m not in distances[v.id]:
        distances[v.id][m] = distances[v.id][n] + 1
        queue += [m]
    queue.sort(key=lambda x:distances[v.id][x])

to_delete = [x for x in valves if valves[x].flow == 0]
for x in distances.values():
  for y in to_delete:
    del x[y]
print(distances)

to_visit = [State(valves, distances)]
best = 0

while to_visit:
  state = to_visit.pop(0)
  #print('visiting %s; queue length %d' % (state.str(), len(to_visit)))
  if state.max_possible() < best:
    continue
  for v in distances:
    valve = valves[v]
    if valve.id in state.open or valve.flow == 0:
      continue
    # Only move whichever one is earlier.
    if state.times[0] < state.times[1]:
      idx = 0
    else:
      idx = 1
    if distances[state.curs[idx]][valve.id] + state.times[idx] >= 26:
      continue
    n = state.move_to_and_open(valve.id, idx)
    if n.score > best:
      print(n.str())
      print(n.score)
      print(len(to_visit))
      best = n.score
    to_visit += [n]
  visited += [state]
  to_visit.sort(key=lambda x: x.score * -1)
  
print(best)
