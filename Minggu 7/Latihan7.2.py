n = int(input("n = "))

for i in range(n,0,-1):
    faklah = 1
    for j in range(1,i+1):
        faklah *= j

    print(faklah,end=" ")

    for k in range(i,0,-1):
        print(k, end=" ")
    print()
