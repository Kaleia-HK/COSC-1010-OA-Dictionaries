# Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values.
# (Use the Internet to get a list of the states and their capitals.)
#
# The program should then randomly quiz the user by displaying the name of a state and asking the user to enter
# that state’s capital. The program should keep a count of the number of correct and incorrect responses.

import us
import random

count_correct = 0
count_incorrect = 0
tries = 0
states = us.states.mapping('name', 'capital')

while tries <= 10:
    random_state = random.choice(list(states))
    cap = input(f"What is the capital of {random_state}?").lower().strip()
    correct_cap = states[random_state]
    correct_cap = correct_cap.lower()

    if cap != correct_cap:
        print(f"Incorrect, the capital is {correct_cap}")
        count_incorrect += 1

    else:
        print(f"Correct, the capital is {correct_cap}")
        count_correct += 1

    tries += 1

print(f"Incorrect: {count_incorrect}  Correct: {count_correct}")