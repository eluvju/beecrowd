# Write an algorithm that reads two floating values (x and y), which should represent the coordinates of a point in a plane. Next, determine which quadrant the point belongs, or if you are at one of the Cartesian axes or the origin (x = y = 0).

# If the point is at the origin, write the message "Origem".

# If the point is at X axis write "Eixo X", else if the point is at Y axis write "Eixo Y".

# Input
# The input contains the coordinates of a point.

# Output
# The output should display the quadrant in which the point is.

X,Y = map(float, input().split(" "))

if (X == 0) and (Y == 0):
    print('Origem')
elif (X == 0):
    print('Eixo Y')
elif (Y == 0):
    print('Eixo X')    
elif (X > 0) and (Y > 0):
    print('Q1')
elif (X < 0) and (Y > 0):
    print('Q2')
elif (X < 0) and (Y < 0):
    print('Q3')
elif (X > 0) and (Y < 0):
    print('Q4')
