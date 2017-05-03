def vsota_prvih_kvadratov(n):
    vsota = 0
    for i in range(n + 1):
        vsota = vsota + i ** 2
    return vsota

def vsota_prvih_potenc(n, k = 1):
    vsota = 0
    for i in range(n + 1):
        vsota = vsota + i ** (k)
    return vsota
