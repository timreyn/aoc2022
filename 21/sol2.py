import sys
import math

lines = {}

class ConstNode(object):
  def __init__(self, num, denom):
    self.num = num // math.gcd(num, denom)
    self.denom = denom // math.gcd(num, denom)
  def __repr__(self):
    return '%d / %d' % (self.num, self.denom)
  def simplify(self):
    return self

class InputNode(object):
  def __repr__(self):
    return 'INPUT'
  def simplify(self):
    return self

def evl(v1, op, v2):
  if op == '*':
    return ConstNode(v1.num * v2.num, v1.denom * v2.denom)
  if op == '+':
    return ConstNode((v1.num * v2.denom + v2.num * v1.denom), (v1.denom * v2.denom))
  if op == '-':
    return ConstNode((v1.num * v2.denom - v2.num * v1.denom), (v1.denom * v2.denom))
  if op == '/':
    return ConstNode(v1.num * v2.denom, v1.denom * v2.num)

nodes = {'humn': InputNode()}

class Node(object):
  def __init__(self, k1, op, k2):
    if isinstance(k1, str):
      if k1 not in nodes:
        nodes[k1] = Node(*lines[k1])
      self.l = nodes[k1]
    else:
      self.l = k1
    if isinstance(k2, str):
      if k2 not in nodes:
        nodes[k2] = Node(*lines[k2])
      self.r = nodes[k2]
    else:
      self.r = k2
    self.op = op

  def _simplify(self):
    self.l = self.l.simplify()
    self.r = self.r.simplify()
    l = self.l
    r = self.r
    op = self.op
    if isinstance(l, ConstNode) and isinstance(r, ConstNode):
      return evl(l, op, r)
    if self.op == '*':
      if isinstance(r, ConstNode):
        return Node(r, '*', l)
      if isinstance(l, ConstNode) and isinstance(r, Node) and r.op in ('+', '-'):
        newleft = Node(l, '*', r.l)
        newright = Node(l, '*', r.r)
        return Node(newleft, r.op, newright)
      if isinstance(l, ConstNode) and isinstance(r, Node) and r.op == '*' and isinstance(r.l, ConstNode):
        return Node(evl(l, '*', r.l), '*', r.r)
    if self.op == '/':
      '''
      if isinstance(r, ConstNode) and isinstance(l, Node) and l.op in ('+', '-'):
        newleft = Node(l.l, '/', r)
        newright = Node(l.r, '/', r)
        return Node(newleft, l.op, newright)
      if isinstance(r, ConstNode) and isinstance(l, Node) and l.op == '*':
        if isinstance(l.l, ConstNode):
          return Node(ConstNode(l.l.val / r.val), '*', l.r)
      '''
      if isinstance(r, ConstNode):
        return Node(l, '*', evl(ConstNode(1,1), '/', r))
    if self.op == '-' and isinstance(r, ConstNode):
      return Node(l, '+', evl(ConstNode(0,1), '-', r))
    if self.op == '+':
      if isinstance(r, ConstNode):
        return Node(r, '+', l)
      if isinstance(l, ConstNode) and isinstance(r, Node) and r.op == '+' and isinstance(r.l, ConstNode):
        return Node(evl(l, '+', r.l), '+', r.r)
      if isinstance(l, ConstNode) and isinstance(r, Node) and r.op == '-' and isinstance(r.l, ConstNode):
        return Node(evl(l, '-', r.l), '+', r.r)
      if isinstance(l, ConstNode) and l.num == 0:
        return r
    if self.op == '=':
      if isinstance(l, ConstNode):
        return Node(r, '=', l)
      if isinstance(l, Node) and l.op == '+' and isinstance(l.l, ConstNode) and isinstance(r, ConstNode):
        return Node(l.r, '=', evl(r, '-', l.l))
      if isinstance(l, Node) and l.op == '*' and isinstance(l.l, ConstNode) and isinstance(r, ConstNode):
        return Node(l.r, '=', evl(r, '/', l.l))
      if isinstance(l, Node) and l.op == '-' and isinstance(l.l, ConstNode) and isinstance(r, ConstNode):
        return Node(evl(l.l, '-', r), '=', l.r)
        
    return self
  def simplify(self):
    init = str(self)
    out = self._simplify()
    fin = str(out)
    if init != fin:
      print('%s --> %s' % (init, fin))
    return out

  def __repr__(self):
    return '[%s %s %s]' % (str(self.l), self.op, str(self.r))

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  spl = line.strip().split(' ')
  if spl[0] == 'root:':
    spl[2] = '='
  if spl[0] == 'humn:':
    lines['humn'] = InputNode()
  elif len(spl) == 2:
    lines[spl[0][:-1]] = int(spl[1])
    nodes[spl[0][:-1]] = ConstNode(int(spl[1]), 1)
  else:
    lines[spl[0][:-1]] = [spl[1], spl[2], spl[3]]

out = Node(*lines['root'])
for i in range(50):
  out = out.simplify()
  print(out)
  print()
