# P1 (X1,Y1) E P1(X2,Y2)

X1, Y1 = map(float, input().split(" "))
X2, Y2 = map(float, input().split(" "))

DISTANCE = pow((X2 - X1)**2 + (Y2 - Y1)**2,0.5)

print(f'{DISTANCE:.4f} Resultado')

