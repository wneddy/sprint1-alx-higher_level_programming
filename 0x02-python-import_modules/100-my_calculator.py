#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as calc
    size = len(argv) - 1

    if (size != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    oprt = argv[2]

    if (operator == "+"):
        print("{:d} {} {:d} = {:d}".format(a, oprt, b, calc.add(a, b)))
    elif (oprt == "-"):
        print("{:d} {} {:d} = {:d}".format(a, oprt, b, calc.sub(a, b)))
    elif (oprt == "*"):
        print("{:d} {} {:d} = {:d}".format(a, oprt, b, calc.mul(a, b)))
    elif (oprt == "/"):
        print("{:d} {} {:d} = {:d}".format(a, oprt, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
