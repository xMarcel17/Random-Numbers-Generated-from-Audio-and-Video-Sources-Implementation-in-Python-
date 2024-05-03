file = open('temp testing.txt', 'r')
file2 = open('wynik.txt', 'w')
temp = 0
pot = 7
for i in range(0,892696):
    if(int(file.read(1))):
        temp = temp + 2**pot
    pot-=1
    if(pot==-1):
        file2.write(str(temp)+'\n')
        temp = 0
        pot = 7