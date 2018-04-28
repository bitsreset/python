#Write a program to print the:
#a.Number of lowercase “a” and “o” in the following sentence.
#b.Number of uppercase “L” and “N” in the following sentence.

s = "Discover, Learning, with, Edureka"

count_a = 0
count_o = 0
count_L = 0
count_N = 0

for each_char in s:
    if each_char == 'a':
        count_a += 1
    elif each_char == 'o':
        count_o += 1
    elif each_char == 'L':
        count_L += 1
    elif each_char == 'N':
        count_N += 1

print("a# {} b# {} L# {} N# {} \n ".format( count_a , count_o , count_L , count_N ))
        
