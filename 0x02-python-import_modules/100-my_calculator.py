#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as calc
    size = len(argv) - 1

    if (size != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    e = int(argv[1])
    d = int(argv[3])
    oprt = argv[2]

    if (operator == "+"):
        print("{:d} {} {:d} = {:d}".format(e, oprt, d, calc.add(e, d)))
    elif (oprt == "-"):
        print("{:d} {} {:d} = {:d}".format(e, oprt, d, calc.sub(e, d)))
    elif (oprt == "*"):
        print("{:d} {} {:d} = {:d}".format(e, oprt, d, calc.mul(e, d)))
    elif (oprt == "/"):
        print("{:d} {} {:d} = {:d}".format(e, oprt, d, calc.div(e, d)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
