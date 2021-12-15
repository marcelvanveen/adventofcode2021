import lib, sys

numbers, cards = lib.read_input()

drawn = []
for n in numbers:
    drawn.append(n)
    for c in cards:
        if c.bingo(drawn):
            print(c.score(drawn))
            sys.exit()
