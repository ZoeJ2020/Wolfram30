# binary string for manipulation
binary_string = '11011010'

# reset total for each program run
total = 0

length = len(binary_string)

# if length is too long, display error and quit program
if length > 8:
    print("Error: Binary string is longer than 8 bits. Please use a smaller string.")
    exit()

# length does not meet if statement requirements, program continues...

# loop for each bit in string
for i in range(length):

    # current power is the length minus the current bit index plus 1
    power = length-(i+1)

    bit = binary_string[i]

    # if current bit = 1, calculate value based on what the current power is
    # and add to total
    if bit == '1':
        total += 2**power

# print when loop is complete
print(total)
exit()