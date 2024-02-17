# Binary to decimal converter
# Giuseppe Manconi
def splitting(binary):
    return [int(digit) for digit in str(binary)]
def validity(value):
    is_valid = 0
    for digit in value:
        if digit == 0 or digit == 1:
            is_valid += 0
        else:
            is_valid += 1
    return is_valid
def converter(value):
    inverted = value[::-1]
    decimal = 0
    for index, bit in enumerate(inverted):
        decimal += bit * 2 ** index
    return decimal

it_is_valid = 0
binary_input = input("Enter a binary value: ")
splitted = splitting(binary_input)
it_is_valid = validity(splitted)
if it_is_valid == 0:
    print("The decimal value of",binary_input,"is:",converter(splitted))
else: 
    print("The value inserted is not a binary value!")


