def je_prastevilo(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    else:
        if n % 2 == 0 or n % 3 == 0:
            return False
        else:
            return True
