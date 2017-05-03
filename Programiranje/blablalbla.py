def stevilo_dni(mesec, leto):
    if mesec == 2 and je_prestopno(leto):
        return 29
    elif mesec == 2:
        return 28
    elif mesec == 4 or mesec == 6 or mesec == 9 or mesec == 11:
        return 30
    else:
        return 31
