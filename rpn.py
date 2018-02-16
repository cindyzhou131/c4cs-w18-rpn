#!/usr/bin/env python3

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
                print("error")

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
        print("Malformed expression")
        # stack.append(token)







def main():
    while True:
        calculate(input("rnp calc> "))


if __name__ == '__main__':
     main()
