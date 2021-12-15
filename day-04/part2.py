import sys, lib

numbers, cards = lib.read_input()

drawn = []
unlucky_cards = cards
for n in numbers:
    drawn.append(n)
    got_bingo = [c for c in unlucky_cards if c.bingo(drawn)]

    unlucky_cards = [c for c in unlucky_cards if c not in got_bingo]
    if len (unlucky_cards) == 0:
        for c in got_bingo:
            print(c.score(drawn))