# Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

# Input
# The input contains three integer numbers.

# Output
# Present the output as requested above.

A,B,C = map(int,input().split(" "))

LIST = [A,B,C]
LIST.sort()

print(F'{LIST[0]}\n{LIST[1]}\n{LIST[2]}\n')
print(f'{A}\n{B}\n{C}')