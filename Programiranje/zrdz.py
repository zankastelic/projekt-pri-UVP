def pretvori_v_letno_obrestno_mero(mesecna_obrestna_mera):
    return round(100 * (1 + mesecna_obrestna_mera) ** 12 - 100)
