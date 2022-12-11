import sys

monkeys = []
monkey = {}
mod = 1

class Operation():
  def __init__(self, expr):
    spl = expr.split('=')[-1].strip().split(' ')
    self.oper = spl[1]
    self.lhs = spl[0]
    self.rhs = spl[2]

  def eval(self, old):
    lhs = old if self.lhs == 'old' else int(self.lhs)
    rhs = old if self.rhs == 'old' else int(self.rhs)
    if self.oper == '+':
      return lhs + rhs
    else:
      return lhs * rhs


for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  line = line.strip()
  if line.startswith('Monkey'):
    monkeys += [{'items': [], 'operation': None, 'divisor': 0, 'true': -1, 'false': -1, 'inspections': 0}]
    monkey = monkeys[-1]
  elif line.startswith('Starting items'):
    monkey['items'] = [int(x.strip()) for x in line.split(':')[-1].split(',')]
  elif line.startswith('Operation'):
    monkey['operation'] = Operation(line.split(':')[-1].strip())
  elif line.startswith('Test'):
    monkey['divisor'] = int(line.split(' ')[-1])
    mod *= monkey['divisor']
  elif line.startswith('If true'):
    monkey['true'] = int(line.split(' ')[-1])
  elif line.startswith('If false'):
    monkey['false'] = int(line.split(' ')[-1])

for rd in range(10000):
  for monkey in monkeys:
    for item in monkey['items']:
      newval = monkey['operation'].eval(item) % mod
      if newval % monkey['divisor'] == 0:
        monkeys[monkey['true']]['items'] += [newval]
      else:
        monkeys[monkey['false']]['items'] += [newval]
      monkey['inspections'] += 1
    monkey['items'] = []

inspections = sorted([monkey['inspections'] for monkey in monkeys])
print(inspections[-1] * inspections[-2])
