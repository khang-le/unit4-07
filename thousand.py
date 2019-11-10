#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program does some calculation


def main():
    for counter in range(1000, 2001):
        if counter % 5 != 4:
            print(counter, " ", end="")
        else:
            print(counter)


if __name__ == "__main__":
    main()
