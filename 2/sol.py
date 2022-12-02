ROCK = 0
PAPER = 1
SCISSORS = 2

WIN = 10
LOSS = 11
DRAW = 12

inputs = {
  'A': ROCK,
  'B': PAPER,
  'C': SCISSORS,
  'X': ROCK,
  'Y': PAPER,
  'Z': SCISSORS
}

scores = {
  WIN: 6,
  DRAW: 3,
  LOSS: 0,
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3
}

def result(yours, theirs):
  out = (yours - theirs) % 3
  if out == 2:
    return LOSS
  if out == 0:
    return DRAW
  if out == 1:
    return WIN
   

score = 0

for line in open('input.txt'):
  line = line.strip()
  theirs = inputs[line[0]]
  yours = inputs[line[-1]]
  score += scores[yours] + scores[result(yours, theirs)]

print(score)
