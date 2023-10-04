print("wolfram is running")

# wolfram rule 30 cellular automation script

# lattice size (length)
lattice_size = 30

# number of simulation time steps (number of iterations)
time_steps = 50


print(lattice_size)

print(type(lattice_size))

lattice = []

for i in range(lattice_size):
    lattice.append(0)

# display length
print(lattice)
print("length = ", len(lattice))

# display midpoint of lattice
mid_point = len(lattice) // 2
print("midpoint = ", mid_point)

# set midpoint to 1
lattice[mid_point] = 1
print(lattice)

# for t in range(time_steps):
    # create a temporary lattice in memory to store previous/next values

trio_state = []
for i in range(lattice_size-2):

    i += 1

    left = lattice[i-1]
    current = lattice[i]
    right = lattice[i+1]

    state = left, current, right

    # add 3-cell state to array
    trio_state.append(state)

# print(trio_state)

new_state = []

for i in trio_state:
    print(i)
    # check formation of state, ruin rule 30

    if i == (0, 0, 0) or i == (1, 1, 1) or i == (1, 1, 0) or i == (1, 0, 1):
        new_state.append(0)

    else:
        new_state.append(1)

print(lattice)
print(new_state)

    # print "graphics" of 1D lattice