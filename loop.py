jumlah = int(input("masukan jumlah barisnya : "))
for i in range(1, jumlah+1):
        for j in range(jumlah-i):
            print(' ', end=' ')
        for j in range(2*i-1):         
            print("✌️ ", end="")
        print("\r")

for i in range(jumlah-1,0,-1):
    for j in range(jumlah-i):
        print(' ', end=' ')
    
    for j in range(2*i-1):
        print('✌️ ',end='')
    print("\r")

