print("wolfram is running")

# wolfram rule 30 cellular automaton script

# number of simulation time steps (number of iterations)
time_steps = 15

# lattice size (length)
lattice_size = time_steps*2

# Define characters for representing 0 and 1
characters = ['□', '■']  # Unicode block elements for square

# print(lattice_size)
# print(type(lattice_size))

lattice = []

for i in range(lattice_size):
    lattice.append(0)

# display length
# print(lattice)
print("length = ", len(lattice))

# display midpoint of lattice
mid_point = len(lattice) // 2
print("midpoint = ", mid_point)

# set midpoint to 1
lattice[mid_point] = 1

# Display the initial state
for cell in lattice:
    print(characters[cell], end='')
print()  # Move to the next line


for t in range(time_steps):

    # Create an array to hold the state of three adjacent cells for each cell
    trio_state = []
    for i in range(lattice_size):
        left = lattice[i - 1] if i - 1 >= 0 else 0
        current = lattice[i]
        right = lattice[i + 1] if i + 1 < lattice_size else 0
        state = left, current, right
        trio_state.append(state)

    # Generate the new state based on the rules of Rule 30
    new_state = []
    for i in range(lattice_size):
        if trio_state[i] == (0, 0, 0) or trio_state[i] == (1, 1, 1) or trio_state[i] == (1, 1, 0) or trio_state[i] == (1, 0, 1):
            new_state.append(0)
        else:
            new_state.append(1)

    # print(lattice)
    # print(new_state)

    lattice = new_state

    # Display the new state
    for cell in new_state:
        print(characters[cell], end='')
    print()  # Move to the next line

exit()