#writes False if any one of them is greater than or equal to the sum of the other two and True 
#otherwise.
# (Note: This computation tests whether the three numbers could be the lengths of the sides of
# some triangle.)
#----------------------------------------------------------------------------------------------------
#if_side_of_trngl.py
#----------------------------------------------------------------------------------------------------
import stdio
import sys

side1 = int(sys.argv[1])
side2 = int(sys.argv[2])
side3 = int(sys.argv[3])

#Sum three sides
#find out the greater sides
#determine the shorter side
# greater side >= compute sum of shorter two sides - false else true

#Sum three sides
total=side1+side2+side3

greatest = side1
#compute greatest among three
if greatest < side2 :
	greatest = side2
elif greatest < side3 :
	greatest = side3

#compute greatest among three
smallest = side1
if smallest > side2:
	smallest = side2
elif smallest > side3:
	smallest = side3

smaller = total - ( greatest + smallest )

stdio.writeln(smallest)
stdio.writeln(smaller)
stdio.writeln(greatest)

if greatest  >= smallest + smaller :
	stdio.writeln("False,cannot form a triangle")
else :
	stdio.writeln("True,can form a triangle")
