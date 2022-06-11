# Write a program that reads two scores of a student. Calculate and print the average of these scores. Your program must accept just valid scores [0..10]. Each score must be validated separately.

# Input
# The input file contains many floating-point numbers​​, positive or negative. The program execution will be finished after the input of two valid scores.

# Output
# When an invalid score is read, you should print the message "nota invalida".
# After the input of two valid scores, the message "media = " must be printed followed by the average of the student. The average must be printed with 2 numbers after the decimal point.

N = 0
MEDIA = 0

while N < 2:

    NOTA = float(input())
    if NOTA >= 0 and NOTA <= 10:
        N = N + 1
        MEDIA = MEDIA + NOTA

    else:
        print("nota invalida")


MEDIA = (MEDIA / 2)
print(f"media = {MEDIA:.2f}")
