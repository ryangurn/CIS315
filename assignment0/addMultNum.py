import fileinput

for line in fileinput.input():
    # print the lines manually, and remove the automatic \n
    # this ensures that there is not a double carrage return
    # print(line, end="")

    # split the string by spaces and check the rest moving forward
    split = line.split(" ")
    if len(split) > 1:
        x = int(split[0])
        y = int(split[1])

        # print the x and y values for testing
        # print("x({}), y({})".format(x, y), end="\n")

        # print proper output
        print("{} {}".format(x+y, x*y))
