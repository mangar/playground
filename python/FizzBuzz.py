# -*- coding: utf-8 -*

import configparser

_config = configparser.ConfigParser()
_config.read('FizzBuzz.ini')
config = _config['DEFAULT']

flag_debug = False


#
#
def index(fizz=config['Fizz'], buzz=config['Buzz'], fizzbuzz=config['FizzBuzz']):

    out = []
    numbers = [1,2,3,4,5,10,15,20]

    oo = {"original":numbers, "out":out}

    for a in numbers:

        if flag_debug:
            print(str(a) + "..." + str(a % 3) + " ... " + str((a % 3) == 0))

        if (((a % 3) == 0) and ((a % 5) == 0)):
            out.append(fizzbuzz)

        elif ((a % 3) == 0):
            out.append(fizz)

        elif ((a % 5) == 0):
            out.append(buzz)

        else:
            out.append(a)      

#    oo["out"] = out

    return oo



#
#
def index_test():
    result = index(fizz="xxx")['out']
    assert result[0] == 1
    assert result[2] == "xxx"






print(config['Fizz'])


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


print("Test:")
index_test()



