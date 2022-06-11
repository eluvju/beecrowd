# Read two nteger values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

# Input
# The input has two integer numbers.

# Output
# Print the relative message to the input as stated above.

X,Y = map(int, input().split(" "))

if (X%Y==0)or(Y%X==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
