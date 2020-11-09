def calc(num1, num2, choice):
    # add the two numbers
    if choice == "sum":
        return num1 + num2
    # subtract the second from the first 
    if choice == "diff":
        return num1 - num2
    # subtract the first from the second
    if choice == "-diff":
        return num2 - num1
    # multiply the two numbers
    if choice == "multiply":
        return num1 * num2
    # divide the first number by the second
    if choice == "divide":
        return num1 / num2
    # divide the second number by the first
    if choice == "-divide":
        return num2 / num1
    # take the power of num2 for num1
    if choice == "power":
        return num1**num2
    # take the power of num1 for num2
    if choice == "-power":
        return num2**num1
    # find the average of two values
    if choice == "avg":
        return (num1 + num2) / 2
    # pop the warning if no appropriate input is given
    else:
        print("The calculator cannot find a proper way to operate, please enter the valid inputs.")