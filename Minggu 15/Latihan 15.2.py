def cek(kalimat):
    kalimat = kalimat.replace(" ", "").lower()
    return pali(kalimat)
 
def pali(s):

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return pali(s[1:-1])

kalimat = input("Masukkan kalimat: ")
if cek(kalimat):
    print(f'"{kalimat}" adalah palindrom')
else:
    print(f'"{kalimat}" bukan palindrom')