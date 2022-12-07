# ARgs let us take any number of (keyword) argumemnts for the function

def get_sum(**kwargs):

    sum = 0

    for x in kwargs:

        sum += x

    return round(sum, 2)


print(get_sum(coffee=4.2, cake=3.1, lemon_tea=4.3, candy=5))
