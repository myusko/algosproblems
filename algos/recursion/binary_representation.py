# Write a function to compute the binary representation of a positive decimal integer. T
# The method should return a string.


def dec_to_bin(number):
    if number < 2:
        return str(number)
    else:
        return dec_to_bin(number / 2) + dec_to_bin(number % 2)
