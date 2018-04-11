#! /usr/bin/env python3

#import modules
import argparse

#define functions
def get_args():
    #create an ArgumentParser object ('parser') thtat will hild all info necessary to parse command line
    parser=argparse.ArgumentParser(description="This script returns the fibonacci number at a specified position in the fibonacci sequence")

    #define positional arguments
    parser.add_argument("num",help="The fibonacci number you wish to calculate", type = int)

    #define the optional arguments
    parser.add_argument("-v","--verbose", help="print verbose output", action='store_true')

    #parse the arguments
    return parser.parse_args()

#function to calculate the fibonacci sequence
def fib(n):
    #do the calculation
    a,b = 0,1
    for i in range(n):
        a,b=b,a+b
    #return the value
    return a

def main():
    if args.verbose:
        print("The Fibonacci number for ",args.num," is ",fib(args.num))

    else:
        #fib_num=fib(args.num)
        #above if num is wanted to be used for other stuff
        print(fib(args.num))

args=get_args()

main()
