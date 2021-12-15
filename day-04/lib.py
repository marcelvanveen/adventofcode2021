import numpy as np
import sys
import re


class BingoCard:

    vector: np.ndarray

    def __init__(self, vector: np.ndarray):
        self.vector = vector

    def bingo(self, numbers) -> bool:
        return np.any(
            np.apply_along_axis(
                np.all,
                0,
                np.apply_along_axis(
                    np.in1d,
                    0,
                    np.hstack((self.vector, self.vector.transpose())),
                    numbers
                )
            )
        )

    def score(self, drawn) -> int:
        return np.sum(np.setdiff1d(self.vector, drawn)) * drawn[-1]

    def __repr__(self):
        return "BingoCard (%sx%x)" % (self.vector.shape[0], self.vector.shape[1])


def read_input():
    numbers = [int(n) for n in sys.stdin.readline().strip().split(",")]
    cards = []
    while sys.stdin.readline() != "":
        cards.append(
            BingoCard(
                np.array(
                    [
                        re.split("\s+", l.strip())
                        for l in [
                            sys.stdin.readline(),
                            sys.stdin.readline(),
                            sys.stdin.readline(),
                            sys.stdin.readline(),
                            sys.stdin.readline(),
                        ]
                    ]
                ).astype(int)
            )
        )

    return (numbers, cards)