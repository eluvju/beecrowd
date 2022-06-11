# Make a program that reads 3 integer values and present the greatest 
# one followed by the message "eh o maior". Use the following formula:
#
# 
A, B, C = map(int, input().split(" "))

maior = ((A+B+abs(A-B))/2)
result = ((int(maior)+C+abs(int(maior)-C))/2)

print(f'{result:.0f} eh o maior')