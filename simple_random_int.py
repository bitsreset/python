import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

#create a string
string_number = str(a) + str(b)

random_number = int(string_number) % (b - a)

stdio.write('between ')
stdio.write(a)
stdio.write(' , ')
stdio.write(b)
stdio.write(' random numbers is = ')
stdio.write(random_number)
