def odrezi_stevko(n):
    if n < 10:
        return 0
    else:
        return n % 10 + 10 * odrezi_stevko(n // 10)
    
