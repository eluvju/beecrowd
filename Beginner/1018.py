N = int(input())

N100,RESTON100 = int((N/100)),(N%100)
N50,RESTON50 = int((RESTON100/50)),(RESTON100%50)
N20,RESTON20 = int((RESTON50/20)),(RESTON50%20)
N10,RESTON10 = int((RESTON20/10)),(RESTON20%10)
N5,RESTON5 = int((RESTON10/5)),(RESTON10%5)
N2,RESTON2 = int((RESTON5/2)),(RESTON5%2)
N1,RESTON1 = int((RESTON2/1)),(RESTON2%1)

print(f'{N:.0f}')
print(f'{N100} nota(s) de R$ 100,00')
print(f'{N50} nota(s) de R$ 50,00')
print(f'{N20} nota(s) de R$ 20,00')
print(f'{N10} nota(s) de R$ 10,00')
print(f'{N5} nota(s) de R$ 5,00')
print(f'{N2} nota(s) de R$ 2,00')
print(f'{N1} nota(s) de R$ 1,00')

# *****************************************
# RESOLUÇÃO 
#------------------------------------------!>
#
# notes = int(input())
#     print(notes)
#     print("{} nota(s) de R$ 100,00".format(int(notes/100)))
#     aux = (notes%100)
#     print("{} nota(s) de R$ 50,00".format(int(aux/50)))
#     aux = (aux%50)
#     print("{} nota(s) de R$ 20,00".format(int(aux/20)))
#     aux = (aux%20)
#     print("{} nota(s) de R$ 10,00".format(int(aux/10)))
#     aux = (aux%10)
#     print("{} nota(s) de R$ 5,00".format(int(aux/5)))
#     aux = (aux%5)
#     print("{} nota(s) de R$ 2,00".format(int(aux/2)))
#     aux = (aux%2)
#     print("{} nota(s) de R$ 1,00".format(int(aux/1))) 
    
#     print("{%d}:{%d}:{%d}",  )