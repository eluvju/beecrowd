# Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

# Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

# Input
# Four integer numbers representing the start and end time of the game.

# Output
# Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . Which means: the game lasted XXX hour(s) and YYY minutes.

# Convert All the variable in Minutes.


A,B,C,D = list(map(int, input().split(" ")))

dif = ((B*60)+D)-((A*60)+C)

if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60

if (A == C) and (B == D):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:    
    print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")