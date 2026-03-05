from typing import List

import math

def main():

    """
    Create and populate a Pascal's Triangle
    and then print it in two formats
    """

    print("---------------------")
    print("| codedrome.com     |")
    print("| Pascal's Triangle |")
    print("---------------------\n")

    pt = create(8)

    populate(pt)

    print_left(pt)

    print("")

    print_centre(pt)


def create(rowcount: int) -> List:

    """
    Create an empty list and then append lists of 0s, each list one longer than the previous
    """

    pt = []

    for r in range(1, rowcount + 1):

        pt.append([0] * r)

    return pt


def populate(pt: List) -> None:

    """
    Populate an uninitialized list with actual values
    """

    for r in range(0, len(pt)):

        for c in range(0, len(pt[r])):

            pt[r][c] = int(math.factorial(r) / (math.factorial(c) * math.factorial(r - c)))


def print_left(pt: List) -> None:

    """
    Prints the triangle in a left-aligned format to demonstrate data structure
    """

    for r in range(0, len(pt)):

        for c in range(0, len(pt[r])):

            print(f"{pt[r][c]:<-4d}", end="")

        print("")


def print_centre(pt: List) -> None:

    """
    Prints the triangle in a conventional centred format
    """

    inset = int(((((len(pt) * 2) - 1) / 2) * 3))

    for r in range(0, len(pt)):

        print(" " * inset, end="")

        for c in range(0, len(pt[r])):

            print(f"{pt[r][c]:<-3d}   ", end="")

        print("")

        inset-= 3


if __name__ == "__main__":

    main()