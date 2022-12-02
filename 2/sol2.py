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
  'X': LOSS,
  'Y': DRAW,
  'Z': WIN
}

scores = {
  WIN: 6,
  DRAW: 3,
  LOSS: 0,
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3
}

def yourguess(theirs, result):
  if result == DRAW:
    return theirs
  if result == WIN:
    return (theirs + 1) % 3
  if result == LOSS:
    return (theirs - 1) % 3
   

score = 0

for line in open('input.txt'):
  line = line.strip()
  theirs = inputs[line[0]]
  result = inputs[line[-1]]
  yours = yourguess(theirs, result)
  score += scores[yours] + scores[result]

print(score)
