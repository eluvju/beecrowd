POSITIVO = 0
NEGATIVO = 0
PAR = 0
IMPAR = 0

for N in range(5):
    X = int(input())
    if (X%2)== 0:
            PAR += 1
    else:
        IMPAR += 1
    if X > 0:
        POSITIVO += 1
    elif X < 0:
        NEGATIVO += 1
        
print(f'{PAR} valor(es) par(es)')
print(f'{IMPAR} valor(es) impar(es)')
print(f'{POSITIVO} valor(es) positivo(s)')
print(f'{NEGATIVO} valor(es) negativo(s)')