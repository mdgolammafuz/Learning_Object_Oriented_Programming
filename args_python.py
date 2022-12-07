# ARgs let us take any number of (non-keyword) argumemnts for the function

def get_sum(*args):

    sum = 0

    for x in args:

        sum += x

    return sum


print(get_sum(4, 3, 4, 5))
