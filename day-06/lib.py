import sys

class State:
    timers = []

    def __init__(self):
        self.timers = [0] * 9

    def add_fish(self, timer: int, amount: int):
        self.timers[timer] += amount

    def next_day(self):
        next_day = State()
        next_day.add_fish(6, self.timers[0])
        next_day.add_fish(8, self.timers[0])

        for i in range(1, 9):
            next_day.add_fish(i-1, self.timers[i])

        return next_day

    def get_total_fish(self):
        return sum(self.timers)

    def __repr__(self):
        return "State (%s)" % (self.timers)

def read_state() -> State:
    state = State()
    for i in sys.stdin.readline().strip().split(","):
        state.add_fish(int(i), 1)

    return state