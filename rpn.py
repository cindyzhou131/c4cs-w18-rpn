#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
import readline
import math


two_param = {'+', '-', '*', '/', '^', '%'}
one_param = {'sin', 'cos', 'tan'}
def calculate(arg):
    stack = list()
    for token in arg.split():
        # print(token)
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            # print(len(stack))
            if(value == 'pi'):

            elif(len(stack) >= 2 and token in two_param):
                arg1 = stack.pop()
                arg2 = stack.pop()



                if(token == '+'):
                    stack.append(arg1 + arg2)
                elif(token == '-'):
                    stack.append(arg1 - arg2)
                elif(token == '*'):
                    stack.append(arg1 * arg2)
                elif(token == '/'):
                    stack.append(arg1/arg2)
                elif(token == '^'):
                    stack.append(arg1**arg2)
                elif(toke == '%'):
                    stack.append(arg1%arg2)
            elif(len(stack) >= 1 and token in one_param):
                arg1 = stack.pop()
                if(token == 'sin'):
                    print(math.sin(arg1))
                    stack.append(math.sin(arg1))
                elif(token == 'cos'):
                    stack.append(math.cos(arg1))
                elif(token == 'tan'):
                    stack.append(math.tan(arg1))
            else:
                cprint('Malform expression!', 'green', 'on_red')
                return
                # math.degrees(x)

    # print(len(stack))
    if(len(stack) == 1):
        return stack.pop()
    else:
        cprint('Malform expression!', 'green', 'on_red')
        # stack.append(token)







def main():
    cprint('RNP CALCULATOR', 'magenta', attrs=['blink'])
    while True:
        cprint(calculate(input("rnp calc> ")), 'cyan')


if __name__ == '__main__':
     main()
