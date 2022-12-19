import collections
import math
import re
import sys

data = []

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  m = re.match('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', line.strip())
  data += [{
    'o': {'o': int(m.group(2))},
    'c': {'o': int(m.group(3))},
    'b': {'o': int(m.group(4)), 'c': int(m.group(5))},
    'g': {'o': int(m.group(6)), 'b': int(m.group(7))},
  }]
  if len(data) >= 3:
    break

MAX_TIME = 32

class State(object):
  def __init__(self, data):
    self.robots = collections.defaultdict(int)
    self.robots['o'] = 1
    self.ore = collections.defaultdict(int)
    self.time = 0
    self.data = data
    self.score = 0

  def adv(self, to_buy, time):
    new = State(self.data)
    new.robots = self.robots.copy()
    new.ore = self.ore.copy()
    for rr, cc in self.data[to_buy].items():
      new.ore[rr] -= cc
    for rr, num in self.robots.items():
      new.ore[rr] += num * time
    new.robots[to_buy] += 1
    new.time = self.time + time
    new.score = self.score
    if to_buy == 'g':
      new.score += MAX_TIME - new.time
    return new

  def time_needed(self, r):
    time_needed = 0
    for rr, cc in self.data[r].items():
      if self.robots[rr] == 0:
        return -1
      t = max(math.ceil((cc - self.ore[rr]) / self.robots[rr]), 0) + 1
      time_needed = max(time_needed, t)
    return time_needed

  def next_states(self):
    for r in ['g', 'b', 'c', 'o']:
      cost = self.data[r]
      time_needed = self.time_needed(r)
      if time_needed >= 0 and self.time + time_needed < MAX_TIME:
        yield self.adv(r, time_needed)

  def max_score(self):
    # Best case -- assume you spend every remaining turn building obsidian and geode.
    time = self.time
    score = self.score
    obsidian_ore = self.ore['b']
    obsidian_robots = self.robots['b']
    while time < MAX_TIME:
      time += 1
      if obsidian_ore >= self.data['g']['b']:
        score += (MAX_TIME - time)
        obsidian_ore -= self.data['g']['b']
      obsidian_ore += obsidian_robots
      obsidian_robots += 1
    return score

  def str(self):
    return '<t: %d> <ore: %s> <robots: %s> <score: %d> <max_score: %d>' % (self.time, str(dict(self.ore)), str(dict(self.robots)), self.score, self.max_score())

def sortkey(state):
  return -1 * (10000 * state.robots['g'] + 1000 * state.robots['b'] + 10 * state.robots['b'] + state.robots['c'])

score = 1

for d in data:
  if len(sys.argv) >= 3 and (i+1) != int(sys.argv[2]):
    continue
  s = State(d)
  best = 0
  queue = [State(d)]
  it = 0
  while queue:
    it += 1
    n = queue[0]
    queue.pop(0)
    if n.time < MAX_TIME:
      for s in n.next_states():
        if s.max_score() > best:
          queue += [s]
    best = max(best, n.score)
    queue.sort(key=sortkey)
  score *= best
  print(best)
print(score)
