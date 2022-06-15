POSITIVO = 0

for N in range(6):
    X = float(input())
    if X > 0:
        POSITIVO += 1
        
print(f'{POSITIVO} valores positivos')