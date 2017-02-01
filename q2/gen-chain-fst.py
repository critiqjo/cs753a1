#!/bin/python3

valid_words = ["bad", "cab", "dad", "bead", "cede",
               "dead", "added", "accede", "decade"]
last_state = 0
final_states = []

for word in valid_words:
    last_state += 1
    print("0 ", last_state, " ", word[0], " ", word[0])
    for c in word[1:]:
        print(last_state, " ", last_state + 1, " ", c, " ", c)
        last_state += 1
    final_states += [last_state]

for state in final_states:
    print(state)
