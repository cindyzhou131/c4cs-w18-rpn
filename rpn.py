#!/usr/bin/env python3
import sys
from termcolor import colored, cprint

def calculate(arg):
    stack = list()
    for token in arg.split():
        # print(token)
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            # print(len(stack))
            if(len(stack) >= 2):
                arg1 = stack.pop()
                arg2 = stack.pop()
            else:
                cprint('Malform expression!', 'green', 'on_red')
                return


            if(token == '+'):
                stack.append(arg1 + arg2)
            elif(token == '-'):
                stack.append(arg1 - arg2)
            elif(token == '*'):
                stack.append(arg1 * arg2)
            elif(token == '/'):
                stack.append(arg1/arg2)
    # print(len(stack))
    if(len(stack) == 1):
        return stack.pop()
    else:
        cprint('Malform expression!', 'green', 'on_red')
        # stack.append(token)







def main():
    while True:
        cprint('RNP CALCULATOR', 'magenta', attrs=['blink'])
        calculate(input("rnp calc> "))


if __name__ == '__main__':
     main()
