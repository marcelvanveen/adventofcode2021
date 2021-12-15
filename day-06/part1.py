from lib import read_state

state = read_state()

for d in range(80):
    state = state.next_day()

print(state.get_total_fish())