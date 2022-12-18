import sys

exposed = set()
double_exposed = set()

for line in open('input.txt' if len(sys.argv) < 2 else sys.argv[1]):
  coords = [int(x) for x in line.strip().split(',')]
  for d in ((0.5,0,0), (-0.5,0,0), (0,0.5,0), (0,-0.5,0), (0,0,0.5), (0,0,-0.5)):
    face = tuple(cc + dd for cc, dd in zip(coords, d))
    if face in exposed:
      double_exposed.add(face)
    else:
      exposed.add(face)

print(len(exposed) - len(double_exposed))
