def decimalToBinary(value):
    print(value%2)
    if value == 1:
        return value
    else:
        value = value//2
        return decimalToBinary(value)

decimalToBinary(7)

        