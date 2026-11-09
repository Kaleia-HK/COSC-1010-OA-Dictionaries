# Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values.
# (Use the Internet to get a list of the states and their capitals.)
#
# The program should then randomly quiz the user by displaying the name of a state and asking the user to enter
# that state’s capital. The program should keep a count of the number of correct and incorrect responses.

# Import the necessary information
import us
import random

# Organize the standard information
count_correct = 0
count_incorrect = 0
tries = 0
states = us.states.mapping('name', 'capital')

# Filter out the dictionary
states = {k: v for k, v in states.items() if v is not None}

asked_states = []

# Ask input from the user, check if wrong/right
while tries <= 9:
    try:
        random_state = random.choice(list(states))
        while random_state in asked_states:
            random_state = random.choice(list(states))

        cap = input(f"What is the capital of {random_state}?").strip()
        correct_cap = states[random_state]

        if cap.lower() != correct_cap.lower():
            print(f"Incorrect, the capital is {correct_cap}")
            count_incorrect += 1

        else:
            print(f"Correct, the capital is {correct_cap}")
            count_correct += 1

        tries += 1
        asked_states.append(random_state)
    except Exception as e:
        print(e)

# Display the results
print(f"Incorrect: {count_incorrect}  Correct: {count_correct}")
