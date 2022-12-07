
special = 5


def get_total(a, b):

    # enclosed scope variable declared inside a function

    total = a + b
    print("The value of the special variable that can be accessed in enclosed scope is : ", special)

    def double_it():

        # local variable
        double = total * 2

        print("The value of the special variable that can be accessed in the local scope as well  is : ", special)

    double_it()

    return print("Total of the numbers you have given is : ", total)


get_total(1, 2)
