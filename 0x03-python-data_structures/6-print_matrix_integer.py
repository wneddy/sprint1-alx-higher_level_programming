#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for entity in range(len(matrix)):
        for figure in range(len(matrix[elem])):
            if (figure != 0):
                print(end=" ")
            print("{:d}".format(matrix[entity][figure]), end="")
        print()
