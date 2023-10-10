# binary string for manipulation
binary_string = '11011010'

# reset total for each program run
total = 0

length = len(binary_string)

# check if length is less than or equal to 8
if length <= 8:

    # if string index is less than the length (aka, if index exists)
    if(0 < length):
         # convert if the index value is 1
        if binary_string[0] == '1':
            total += 2**(length-1)

# repeats for other potential values (up to 8)

    if(1 < length):
        if binary_string[1] == '1':
            total += 2**(length-2)

    if(2 < length):
        if binary_string[2] == '1':
            total += 2**(length-3)

    if(3 < length):
        if binary_string[3] == '1':
            total += 2**(length-4)

    if(4 < length):
        if binary_string[4] == '1':
            total += 2**(length-5)

    if(5 < length):
        if binary_string[5] == '1':
            total += 2**(length-6)

    if(6 < length):
        if binary_string[6] == '1':
            total += 2**(length-7)

    if(7 < length):
        if binary_string[7] == '1':
            total += 2**(length-8)

# check if length is over 8 bits
if len(binary_string) > 8:
    print("Error: Binary string is over 8 bits. Please use a smaller string.")
    exit()

print(total)
exit()