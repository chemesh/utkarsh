from math import *
from os import error

err = "invalid. Enter -h for help"         # error message
res = 0                                    # result of last calculation
operators = {                              # dictionary for operators and their arithematic calculations given 2 parametrs x,y
        '+': lambda x,y:  x + y,
        '-': lambda x,y:  x - y,
        '*': lambda x,y:  x * y,
        '/': lambda x,y:  x / y,
        '^': lambda x,y:  pow(x,y),
        'sqrt': lambda x,y:    sqrt(x)
}



def simpleCalc(x,y,op):
    """
    x,y = float values
    op = operator of the acceptable operators

    return the arithematic statement of 'x op y'
    """
    return operators[op](x,y)


print("this is simpleCalc.\n Enter -h for help")
while True:
    expression = input()
    if expression == "exit":
        break

    elif expression == "-h":
        print(
        "acceptable inputs:\n" +
            "\t '[operator] [operand] [opertor]'\n" +
            "\t '[operand] [opertor]' - left operator will be the result of the last calculation\n" +
            "\t (if performed on first calculation, left operand will be 0)\n\n" +

        "operand must be a number (either a float or integer)\n" +
        "operator must be one of the following: ", list(operators.keys()),"\n\n" +
         
        "examples: 3 + 4 ; -5 ^ 2 ; 7.34 / 32 ; 16 sqrt\n" + 
        "**note: 'sqrt' opartor only needs the left operand to perform so '[operand] sqrt' will work\n\n" +

        "enter 'exit' to terminate the program"
        )

    elif expression == "":
        continue

    else:
        try:
            x,op,y = expression.split(" ")
            res = simpleCalc(float(x),float(y),op)
            if res == int(res):
                res = int(res)
            print("result: ",res)
            
        except ValueError:
            try:
                a,b = expression.split(" ")
                if (a in operators.keys()):
                    res = simpleCalc (res,float(b),a)
                else:
                    res = simpleCalc(float(a),0,b)

                if res == int(res):
                    res = int(res)

                print("result: ",res)
            except ValueError:
                print(err,"\n")
            except KeyError:
                print (err,"\n")
        except KeyError:
            print (err,"\n")