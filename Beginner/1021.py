# Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

# Input
# The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

# Output
# Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.

notes = float(input())

print(notes)
print("{} nota(s) de R$ 100.00".format(int(notes/100)))
aux = (notes % 100)
print("{} nota(s) de R$ 50.00".format(int(aux/50)))
aux = (aux % 50)
print("{} nota(s) de R$ 20.00".format(int(aux/20)))
aux = (aux % 20)
print("{} nota(s) de R$ 10.00".format(int(aux/10)))
aux = (aux % 10)
print("{} nota(s) de R$ 5.00".format(int(aux/5)))
aux = (aux % 5)
print("{} nota(s) de R$ 2.00".format(int(aux/2)))
aux = (aux % 2)

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(aux/1)))
aux = (aux % 1)
Break = (aux * 100)

print("{} moeda(s) de R$ 0.50".format(int(Break/50)))
Break = (Break % 50)
print("{} moeda(s) de R$ 0.25".format(int(Break/25)))
Break = (Break % 25)
print("{} moeda(s) de R$ 0.10".format(int(Break/10)))
Break = (Break % 10)
print("{} moeda(s) de R$ 0.05".format(int(Break/5)))
Break = (Break % 5)
print("{} moeda(s) de R$ 0.01".format(int(Break/1)))