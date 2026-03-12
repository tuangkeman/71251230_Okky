def ganjil(bawah,atas):
    if bawah < atas:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah: ",end="" )
        for i in range(atas):
            if i > bawah:
                if i % 2 != 0:
                    print(i,end="")
                    if i < atas -1:
                        print(" ",end="")
                 
        print(f".")
    elif bawah > atas:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah: ",end="" )
        for i in range(bawah, 0 , -1):
            if i > atas:
                if i % 2 !=0:
                    print(i,end="")
                    if i > atas+1:
                        print(" ",end="")
        print(f".")
ganjil(10,30)
ganjil(97,82)