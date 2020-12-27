# -*- coding: utf-8 -*


flag_debug = False


def index(fizz="Fizz", buzz="Buzz", fizzbuzz="FizzBuzz"):

    out = []
    numbers = [1,2,3,4,5,10,15,20]

    oo = {"original":numbers, "out":out}

    for a in numbers:

        if flag_debug:
            print(str(a) + "..." + str(a % 3) + " ... " + str((a % 3) == 0))

        if (((a % 3) == 0) & ((a % 5) == 0)):
            out.append(fizzbuzz)

        elif ((a % 3) == 0):
            out.append(fizz)

        elif ((a % 5) == 0):
            out.append(buzz)

        else:
            out.append(a)      

#    oo["out"] = out

    return oo





print("-------")
#out = index("f", "b", "fb")
result = index()

print("Original:")
print(result["original"])


print("-------")
print("Result:")
for o in result["out"]:
    print(">> " + str(o))

print("-------")


