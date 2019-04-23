#!/usr/bin/env python3

"""
Name: jranderson
Date: 04.19.19
Purpose: Sum13
"""

import argparse
import os
import sys

# ---------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Unlucky 13 Sum",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("file", help="Input File", metavar="FILE")

    return parser.parse_args()


# ---------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# ---------------------------------------------------------
def die(msg="Something bad happened"):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# ---------------------------------------------------------
def unlucky13(nums):
    """sum numbers to 13"""

    sum_list = []
    for i in range(0, len(nums)):
        if nums[i] == "13":
            continue
        elif (nums[i - 1] == "13") and i != 0:
            continue
        else:
            sum_list.append(int(nums[i]))

    return sum(sum_list)


# ---------------------------------------------------------
def main():
    """Sko-Codin!"""

    args = get_args()
    inputfile = args.file

    if not os.path.isfile(inputfile):
        die('"{}" is not a file'.format(inputfile))

    luckysum = 0
    input_fh = open(inputfile).read().split()
    for i, line in enumerate(input_fh):
        numlist = line.split(",")
        # print(numlist)
        luckysum = unlucky13(nums=numlist)
        print("lucky sum: {}".format(luckysum))


# ----------------------------------------------------------
if __name__ == "__main__":
    main()
