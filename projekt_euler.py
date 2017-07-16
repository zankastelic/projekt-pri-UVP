def vsota(stevilado):
    veckratniki = []
    for x in range(1, stevilado):
        if x % 15 == 0:
            veckratniki.append(x)
        elif x % 3 == 0:
            veckratniki.append(x)
        elif x % 5 == 0:
            veckratniki.append(x)
    return sum(veckratniki)

def najvecja_vsota(niz):
    najvecja_vsota_do_sedaj = 0
    stevilo = ''
    for x in niz:
        stevilo += x
        if len(stevilo) == 10:
            a = int(stevilo)
            b = vsota_stevk(a)
            if b > najvecja_vsota_do_sedaj:
                najvecja_vsota_do_sedaj = b
    return najvecja_vsota_do_sedaj

def vsota_stevk(n):
    vsota = 0
    while n > 0:
        vsota += n % 10
        n //= 10
    return vsota


def vsota_potenc(x):
    vsota = 0
    for x in range(x + 1):
        vsota += x ** 2
    return vsota

def vsota_stevil_do(x):
    vsota = 0
    for x in range(x + 1):
        vsota += x
    return vsota

def iscemo(x):
    return vsota_stevil_do(x) ** 2 - vsota_potenc(x)


def produkt_stevk(stevilo): #tuki je število niz
    produkt = 1
    for x in stevilo:
        x = int(x)
        produkt *= x
    return produkt

def najvecji_produkt(niz):
    dolzina_niza = len(niz)
    nov = ''
    produkt = 0
    najvecji_niz = ''
    for x in range(dolzina_niza - 13):
        nov = niz[x:x+13]
        b = produkt_stevk(nov)
        if produkt < b:
            produkt == b
            najvecji_niz = nov
    return najvecji_niz
        

def palindrom(dokok): #ni najbolj učinkovita
    najvecji = 0
    for i in range(100, dokok):
        for j in range(100, dokok):
            if str(i * j) == str(i * j)[::-1]:
                if najvecji < (i * j):
                    najvecji = i * j 
    return najvecji 


def lcm(x, y):
   if x > y:
       večji = x
   else:
       večji = y

   while True: 
       if((večji % x == 0) and (večji % y == 0)):
           lcm = večji
           break
       večji += 1

   return lcm

def je_prastevilo(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def prastevila(n):
    while True:
        n += 1
        if je_prastevilo(n):
            yield n

g = prastevila(1)
[next(g) for i in range(10001)] #problem 7
#kdaj da kdaj ne?

import math	
def je_prastevilo(n):
    if n == 2:
        return True 
    for a in range(2,round(math.sqrt(n)) + 1): 
        if n % a == 0: 
            return False
    return True
	
def prastevila_do(n):
    seznam_prastevil = []
    for x in range(2, n + 1):
        a = je_prastevilo(x)
        if a:
            seznam_prastevil.append(x)
        
    return seznam_prastevil


def problem10(dokoliko):
    return sum(prastevila_do(dokoliko))

def nova_vsota(zadnjestevilo):
    vsota = 0
    for x in range(1, zadnjestevilo + 1):
        vsota += x ** x
    return vsota

def problem48(zadnja):
    return nova_vsota(zadnja) % 10 ** 10




