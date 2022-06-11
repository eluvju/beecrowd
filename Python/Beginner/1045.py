# Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:
# if A ≥ B + C, write the message: NAO FORMA TRIANGULO
# if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
# if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
# if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
# if the three sides are the same size, write the message: TRIANGULO EQUILATERO
# if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
# Input
# The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

# Output
# Print all the classifications of the triangle presented in the input.

A,B,C = map(float, input().split(" "))

LIST = [A,B,C]
LIST.sort()
    
if (LIST[2] >= (LIST[1]+LIST[0])):
    print('NAO FORMA TRIANGULO')

elif ((LIST[2]**2) == ((LIST[1]**2)+(LIST[0]**2))):
        print('TRIANGULO RETANGULO')
elif ((LIST[2]**2) > ((LIST[1]**2)+(LIST[0]**2))):
        print('TRIANGULO OBTUSANGULO')
elif ((LIST[2]**2) < ((LIST[1]**2)+(LIST[0]**2))):
        print('TRIANGULO ACUTANGULO')
if (LIST[2] == LIST[1]) and (LIST[1] == LIST[0]):
        print('TRIANGULO EQUILATERO')
elif (LIST[2] == LIST[1]) or (LIST[1] == LIST[0]):
        print('TRIANGULO ISOSCELES')