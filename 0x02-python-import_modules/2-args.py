#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    val = len(sys.argv)
    if val == 1:
        print("{} arguments.".format(val - 1))
    elif val == 2:
        print("{} argument:".format(val - 1))
    else:
        print("{} arguments:".format(val - 1))

    for x in range(1, val):
        print("{}: {}".format(x, sys.argv[x]))
