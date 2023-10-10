# initialise empty string
bin_string = ""

# conversion function:
def convert(x):
    # use global string in function
    global bin_string

    # get remainder and quotient values from current number
    remainder = x%2
    quotient = x//2

    # remainder = bit, add to string
    bin_string = bin_string + str(remainder)

    # repeat if quotient is not 0
    if quotient != 0:
        convert(quotient)
    
    else:
        # reverse binary string to display correctly
        bin_string = bin_string[::-1]
        print(bin_string)

        # stop program
        quit()

# get decimal number input
decimal = int(input("please enter a decimal number to convert to binary: "))

# call function to begin conversion
convert(decimal)