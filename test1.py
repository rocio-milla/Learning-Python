def sum(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    if num2 == 0:
        raise Exception("Can't divide by 0")
    return num1/num2


def simpleCalculator():
    num1 = 0
    num2 = 0
    type= ""
    simplecalculatoroptions = {1: sum, 2: substract, 3: multiply, 4: divide}
    def chooseOperation():
        nonlocal num1, num2, type
        num1 = int(input("Num1: "))
        num2 = int(input("Num2: "))

        print("Please select one:\n1: sum\n2: substract\n3: multiply\n4:divide")

        type = int(input(""))

    chooseOperation()
    try:
        print(simplecalculatoroptions[type](num1, num2))
        restart = input("Want to do it again? (y/n)")

        if restart == "y":
            simpleCalculator()
        else:
            print("Thanks for try this test!")

    except Exception as e:
        print("Something went wrong\n", e.args)
        simpleCalculator()


simpleCalculator()