def cek_angka(a,b,c):
    if a != b and b != c and c != a:
        if (a + b) == c or (b + c) == a or (a + c) == b:
            return True
        else:
            return False
    else:
        return False