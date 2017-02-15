#wap that does the same thing as the built-in sum function. However, instead of 
def my_sum(*number_sequence):
    sum=0
    for number in number_sequence:
        sum +=  number

    return sum

print("sum is {0}".format(my_sum(*[-1,0,1])))
