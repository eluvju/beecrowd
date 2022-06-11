# Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:

# Perimetro = XX.X

# If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:

# Area = XX.X

# Input
# The input file has tree floating point numbers.

# Output
# Print the result with one digit after the decimal point.

# Referência: https://mundoeducacao.uol.com.br/matematica/condicao-existencia-um-triangulo.htm#:~:text=Só%20irá%20existir%20um%20triângulo,soma%20dos%20outros%20dois%20lados.


A,B,C, = map(float,input().split(" "))

if ((B-C) < A) and (A < (B+C)):
    aux1 = True
else:
    aux1 = False
if ((A-C) < B) and (B < (A+C)):
    aux2 = True
else:
    aux2 = False
if ((A-B) < C) and (C < (A+B)):
    aux3 = True
else:
    aux3 = False
        
if aux1 == True and aux2 == True and aux3 == True:
    triangulo = True

else:
    triangulo = False
    
if triangulo == True:
    PERIMETRO = A+B+C
    print(f'Perimetro = {PERIMETRO}')
else:
    AREA = (((A+B)*C)/2)
    print(f'Area = {AREA}')
    
# Solution:

A,B,C = map(float,input().split())
if (A+B)>C and (A+C)>B and (B+C)>A:
    perimeter = (A+B+C)
    print(f"Perimetro = {perimeter:0.1f}")
else:
    area = 0.5*(A+B)*C
    print(f"Area = {area:0.1f}")
