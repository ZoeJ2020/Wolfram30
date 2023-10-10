# same project as integer_2.py, but with additional input checks and no limit on string length.

# binary string for manipulation
binary_string = '11011010'

# reset total for each program run
total = 0

length = len(binary_string)

# create sets to compare
str_set = set(binary_string)
bin_set = {'0', '1'}

# if sets match, continue. if not, quit program and display error

if bin_set == str_set or str_set == {'0'} or str_set == {'1'}:
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

else: 
    # error message
    print("Error: String entered is non-binary. Please check your input.")



