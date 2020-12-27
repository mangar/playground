# -*- coding: utf-8 -*


flag_debug = False


def index():

    out = []
    numbers = [1,2,3,4,5,10,15,20]

    for a in numbers:

        if flag_debug:
            print(str(a) + "..." + str(a % 3) + " ... " + str((a % 3) == 0))

        if (((a % 3) == 0) & ((a % 5) == 0)):
            out.append("FizzBuzz")
        elif ((a % 3) == 0):
            out.append("Fizz")
        elif ((a % 5) == 0):
            out.append("Buzz")
        else:
            out.append(a)      


    return out


print("-------")
out = index()

for o in out:
    print(">> " + str(o))

print("-------")