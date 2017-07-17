import tkinter as tk
import random

vprasanja = [
'Kako je bilo ime prvemu slovenskemu protestantskemu učitelju in prvemu slovničarju slovenskega jezika?', 
'Katerega leta je bila v Kranjski gori v okviru takratnega Slovenskega planinskega društva ustanovljena Gorska reševalna zveza Slovenije?',
'Katerega leta so se v Sloveniji, in sicer v Ljubljani, začele uradne meteorološke meritve, za katere obstajajo zapisi?',
'Kakor vsaka žival ima tudi lisica naravne sovražnike. Katera žival ni to?',
'Kje leži Paradana, svetovno znana kraška udornica z ledeno jamo?',
'Portoroški Hotel Palace, zgrajen v zadnjih letih miru pred razpadom Avstro – Ogrske, je bil drugi takrat največji hotel na Jadranu. Kdaj so ga odprli?',
'Katere vrste parkljarjev je na kočevsko-snežniškem območju največ?',
'Srečno, Kekec Jožeta Galeta je bil …',
'Katerega leta je bil v belokranjskem Gradcu ustanovljen Rdeči križ Slovenije?',
'Kateri slovenski slap je skrivnostno skrit v temačni votlini, ki jo je izdolbel?',
'Koliko let so, z več prekinitvami, ljudje vztrajali v hišah na kolih na Ljubljanskem barju?',
'Pisatelj Cirič Kosmač sode med socialne realiste. Kateri avtor ne sodi mednje?',
'V bližini Preddvora stoji grad Turn, kjer se je rodila pisateljica …',
'Kako dolga je sprehajalna in rekreacijska pot, speljana po trasi žičnate ograje, ki je med drugo svetovno vojno obdajala Ljubljano?',
'Katerega leta je bil katastrofalni potres, ko se je podrla skoraj vsa srednjeveška Ljubljana?',
'Kateri kraj je znan po konjereji? ',
'Kdaj so območje Slovenije poselili Kelti?',
'Katero delo je napisal Srečko Kosovel?',
'Katero delo je napisal France Bevk?',
'Kako se imenuje kraška jama zahodno od Divače, ki velja za tretjo najdaljšo jamo v Sloveniji?',
'Kako se imenuje cerkev, ki je zgrajena na skrajnem zahodnem robu Piranskega polotoka?',
'Prvi zabeleženi čarovniški proces na Slovenskem je potekal leta 1427 v Celju – proti komu?',
'Solkanski most je najdaljši kamniti železniški most na svetu. Kako dolg je njegov kamniti lok?', 
'Kolikšna je največja globina Bohinjskega jezera?', 
'V katero obdobje uvrščamo Ivana Cankarja?',
'Kdo je napisal Šivilja in škarjice?',
'Cerkniško jezero je eden najzanimivejših ekosistemov v Sloveniji. Koliko vrst ptic gnezdi na jezeru?',
'Koliko krakov imajo zvezde v slovenskem grbu?',
'Kateri vrh ne spada v skupino Karavank?', 
'Kolikšen delež volivcev se  je leta 1990 na plebiscitu o neodvisnosti izrekel za samostojno Slovenijo?', 
'Kakšen ples je štajeriš, ki je razširjen po vsem slovenskem ozemlju, razen v Reziji?',
'Katerega leta je v Ljubljani začelo delovati prvo telefonsko omrežje?', 
'Kako imenujemo turistično prireditev, povezano s splavarjenjem v Ljubnem ob Savinji?', # 33
'Koliko je dolga reka Drava v Sloveniji?',
'V kateri vasi v Goriških brdih vsako leto prirejajo festival Dnevi poezije in vina?',
'Katerega leta je začel izhajati osrednji slovenski dnevnik Delo?',
'Katero delo je napisal Oton Zupančič?',
'Leta 1821 je bil v Ljubljani kongres Svete Alianse. Katera država ni bila del te politične zveze?',
'Kdaj so v Ljubljani zgradili prvi vodovod?',
'V katero obdobje uvrščamo Primoža Trubarja?',
'Koliko je en bokal vina?',
'V katero obdobje uvrščamo Cirila Kosmača?',
'Katera vrsta industrije zaposluje večino prebivalcev Medvod?', 
'Katerega leta je začela (poskusno) oddajati program televizija na Slovenskem?',
'V katero obdobje uvrščamo Dragotina Ketteja?',
'Kolikšno površino obsega Kras?',
'Kaj je praha?',
'Kateri avtor je bil sodobnik Prežihovega Voranca?',
'Koliko let je bila Izola pod Benečani?', 
'Vladimir Šubic je zasnoval ljubljanski nebotičnik in tudi prvi stanovanjski blok v Ljubljani. Kako se imenuje?'
]

odgovori1 = [
'A: Adam Bohorič',
'A: Leta 1901',
'A: Leta 1810',
'A: Medved', 
'A: Na Pokljuki', 
'A: Leta 1904', 
'A: Alpskih kozorogov', 
'A: prvi slovenski barvni film', 
'A: Leta 1934',
'A: Kozjak', 
'A: 500 let', 
'A: Ivan Minatti', 
'A: Josipina Turnograjska', 
'A: 12 kilometrov', 
'A: Leta 1490',
'A: Gornja Radgona',
'A: Okoli leta 300 pr. n. št.',
'A: Godba pomladi',
'A: Balada o trobenti in oblaku', 
'A: Kačna jama', 
'A: Cerkev Marije Zdravja',
'A: Agati Schwarzkobler', 
'A: 65 metrov',
'A: 20 metrov',
'A: V moderno', 
'A: Boris A. Novak', 
'A: Več kot 50 vrst', 
'A: Pet', 
'A: Jalovec', 
'A: 68 odstotkov',
'A: Maturantski ples', 
'A: Leta 1850', 
'A: Dan flosarjev', # 33
'A: Okoli 20 kilometrov', 
'A: V Bukovici', 
'A: Leta 1848', 
'A: Moja mati', 
'A: Avstrija', 
'A: V času rimske Emone', 
'A: V moderno', 
'A: Približno 0,5 litra', 
'A: V moderno', 
'A: Kemična industrija',
'A: Leta 1949', 
'A: V moderno', 
'A: Okoli 200 km2', 
'A: Neposejana njiva', 
'A: France Bevk', 
'A: 150 let', 
'A: Delavski dom' 
]

odgovori2 = [
'B: Jurij Dalmatin',
'B: Leta 1912',
'B: Leta 1850',
'B: Planinski orel', 
'B: Na Snežniku', 
'B: Leta 1910',
'B: Gamsov', 
'B: prvi slovenskicelovečerni film', 
'B: Leta 1944',
'B: Peričnik', 
'B: 1000 let', 
'B: Mile Klopčič', 
'B: Luiza Pesjak', 
'B: 25 kilometrov', 
'B: Leta 1511',
'B: Lenart',
'B: Okoli leta 200 pr. n. št.',
'B: Samo en cvet',
'B: Hlapci', 
'B: Križna jama', 
'B: Cerkev Marijinega vnebovzetja', 
'B: Katri Mantl', 
'B: 85 metrov',
'B: 35 metrov',
'B: V protestantizem', 
'B: Dragotin Kete', 
'B: Več kot 100 vrst', 
'B: Šest', 
'B: Stol', 
'B: 79 odstotkov',
'B: Otroški ples', 
'B: Leta 1897', 
'B: Flosarski bal', # 33
'B: Okoli 82 kilometrov', 
'B: V Medani', 
'B: Leta 1919', 
'B: Povodni mož', 
'B: Prusija', 
'B: V srednjem veku', 
'B: V protestantizem', 
'B: Približno 0,7 litra',
'B: V realizem', 
'B: Lesna industrija',
'B: Leta 1957', 
'B: V razsvetljenstvo', 
'B: Okoli 350 km2',
'B: Poljedeljsko orodje', 
'B: Ivan Cankar', 
'B: 450 let', 
'B: Dom borcev', 

]

odgovori3 = [
'C: Primož Trubar',
'C: Leta 1938',
'C: Leta 1880', 
'C: Ris', 
'C: V Kočevskem rogu', 
'C: Leta 1914', 
'C: Jelenjadi', 
'C: prvi slovenski mladinski celovečerni film', 
'C: Leta 1954', 
'C: Rinka', 
'C: 2500 let', 
'C: Miško Kranjec', 
'C: Veronika Simoniti', 
'C: 34 kilometrov', 
'C: Leta 1643',
'C: Ljutomer',
'C: Okoli leta 100 pr. n. št.', 
'C: Zdravljica',
'C: Kaplan Martin Čedermac', 
'C: Potočka zijalka', 
'C: Cerkev svetega Jurija', 
'C: Uršuli Kolar', 
'C: 99 metrov',
'C: 45 metrov',
'C: V realizem', 
'C: Kajetan Kovič', 
'C: Več kot 250 vrst', 
'C: Sedem', 
'C: Struška', 
'C: 89 odstotkov',
'C: Pogrebni ples', 
'C: Leta 1915', 
'C: Savinjski bal', # 33
'C: Okoli 140 kilometrov', 
'C: V Šmartnem', 
'C: Leta 1945', 
'C: Soči', 
'C: Rusija', 
'C: V 18. stoletju', 
'C: V razsvetljenstvo', 
'C: Približno 1,5 litra',
'C: V romantiko', 
'C: Papirna industrija',
'C: Leta 1965',
'C: V realizem', 
'C: Okoli 400 km2',
'C: Vrsta gnojila', 
'C: Ivan Tavčar', 
'C: 500 let', 
'C: Meksika', 
]

odgovori4 = [
'D: Sebastijan Krelj',
'D: Leta 1965',
'D: Leta 1914',
'D: Volk', 
'D: V Trnovskem gozdu', 
'D: Leta 1918',
'D: Muflonov', 
'D: prvi slovenski zvočni film', 
'D: Leta 1964', 
'D: Savica', 
'D: 5000 let', 
'D: Tone Seliškar', 
'D: Zofka Kveder', 
'D: 41 kilometrov', 
'D: Leta 1895',
'D: Veržej', 
'D: Okoli leta 10 n. št.', 
'D: Z vlakom',
'D: Solzice', 
'D: Sveta jama', 
'D: Cerkev svete Trojice', 
'D: Veroniki Deseniški', 
'D: 105 metrov',
'D: 60 metrov',
'D: V romantiko', 
'D: Svetlana Makarovič', 
'D: Več kot 300 vrst', 
'D: Osem', 
'D: Trupejevo poldne', 
'D: 95 odstotkov',
'D: Snubitveni ples', 
'D: Leta 1930', 
'D: Splavarsko popoldne', # 33
'D: Okoli 500 kilometrov', 
'D: V Vilenici', 
'D: Leta 1959', 
'D: Z vlakom', 
'D: Velika Britanija', 
'D: Pred 1000 leti', 
'D: V romantiko', 
'D: Približno 2 litra',
'D: V socialni realizem', 
'D: Tekstilna industrija',
'D: Leta 1973', 
'D: V romatinko', 
'D: Okoli 500 km2',
'D: Vrsta kmetijskega posestva', 
'D: Josip Jurčič', 
'D: 700 let', 
'D: Vila Šubic' 
]
resitve = ['a','b','b','a','d','b','c','a','b','a','c','a','a','c','b','c','a','a','c','a','a','d','b','c','a','b','b','b','a','c','d','b','b',
           'c','b','d','d', 'd', 'a', 'b','c', 'd','a', 'b','a','d','a','a','c', 'c']
nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
polovicke = ['b','d','d','c','a','d','b','c','d','b','b','d','d','a','a','a','b','b','b','c','c','c','a','a','b','a','d','a','b','a','b','a','d','b','d',
             'a','b','a','c','a','a','c','b','c','b','a','c','d','d','d']

okno = tk.Tk()



def odgovor_ni_pravilen():
    odg_ni_pravilen = tk.Tk()
    zgori = tk.Frame(odg_ni_pravilen)
    zgori.pack()
    spodi = tk.Frame(odg_ni_pravilen)
    spodi.pack()
    zal = tk.Label(zgori, text='Žal je Vaš odgovor napačen.')
    zal.pack()
    ponovno = tk.Button(spodi, text='Poskusi ponovno!', command = lambda:novo_in_naslednje_vprasanje())
    ponovno.pack()
    odg_ni_pravilen.mainloop()



def gumb_preveri_odgovor_a(x, y):
    odgovor_pravilen = resitve[x]
    if odgovor_pravilen == 'a':  
        okno_za_a = tk.Tk()
        zg = tk.Frame(okno_za_a)
        zg.pack()
        sp = tk.Frame(okno_za_a)
        sp.pack()
        zaploskajmo = tk.Label(zg, text='Odgovor je pravilen, zaslužili ste {} €!'.format(nagrada[y]))
        zaploskajmo.pack()
        gumb_za_naprej_in_naslednje_vprasanje = tk.Button(sp, text='Naslednje vprašanje', command = lambda:novo_in_naslednje_vprasanje())
        gumb_za_naprej_in_naslednje_vprasanje.pack()
        okno_za_a.mainloop()
    else:
        odgovor_ni_pravilen()
                    
def gumb_preveri_odgovor_b(x, y):
    odgovor_pravilen = resitve[x]
    if odgovor_pravilen == 'b':  
        okno_za_b = tk.Tk()
        zg = tk.Frame(okno_za_b)
        zg.pack()
        sp = tk.Frame(okno_za_b)
        sp.pack()
        zaploskajmo = tk.Label(zg, text='Odgovor je pravilen, zaslužili ste {} €!'.format(nagrada[y]))
        zaploskajmo.pack()
        gumb_za_naprej_in_naslednje_vprasanje = tk.Button(sp, text='Naslednje vprašanje',command = lambda:novo_in_naslednje_vprasanje())
        gumb_za_naprej_in_naslednje_vprasanje.pack()
        okno_za_b.mainloop()
    else:
        odgovor_ni_pravilen()

def gumb_preveri_odgovor_c(x, y):
    odgovor_pravilen = resitve[x]
    if odgovor_pravilen == 'c':  
        okno_za_c = tk.Tk()
        zg = tk.Frame(okno_za_c)
        zg.pack()
        sp = tk.Frame(okno_za_c)
        sp.pack()
        zaploskajmo = tk.Label(zg, text='Odgovor je pravilen, zaslužili ste {} €!'.format(nagrada[y]))
        zaploskajmo.pack()
        gumb_za_naprej_in_naslednje_vprasanje = tk.Button(sp, text='Naslednje vprašanje', command = lambda:novo_in_naslednje_vprasanje())
        gumb_za_naprej_in_naslednje_vprasanje.pack()
        okno_za_c.mainloop()
    else:
        odgovor_ni_pravilen()

def gumb_preveri_odgovor_d(x, y):
    odgovor_pravilen = resitve[x]
    if odgovor_pravilen == 'd':  
        okno_za_d = tk.Tk()
        zg = tk.Frame(okno_za_d)
        zg.pack()
        sp = tk.Frame(okno_za_d)
        sp.pack()
        zaploskajmo = tk.Label(zg, text='Odgovor je pravilen, zaslužili ste {} €!'.format(nagrada[y]))
        zaploskajmo.pack()
        gumb_za_naprej_in_naslednje_vprasanje = tk.Button(sp, text='Naslednje vprašanje', command = lambda:novo_in_naslednje_vprasanje())
        gumb_za_naprej_in_naslednje_vprasanje.pack()
        okno_za_d.mainloop()
    else:
        odgovor_ni_pravilen()

def izhod(stanje):
    izhodno_okno = tk.Tk()
    izhodho_sporocilo =tk.Label(izhodno_okno, text='Četitamo zadeli ste {} €!'.format(stanje))
    izhodho_sporocilo.pack()
    izhodho_sporocilo.mainloop()

def polovicka(x):
    pravilen = resitve[x]
    skoraj = polovicke[x]
    #if izkoriscena_polovicka == False:
    if pravilen == 'a':
        if skoraj == 'b':
            okno_a_in_b = tk.Tk()
            a = tk.Button(okno_a_in_b, text = odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
            b = tk.Button(okno_a_in_b, text = odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=1)
            okno_a_in_b.mainloop()
        if skoraj == 'c':
            okno_a_in_c = tk.Tk()
            a = tk.Button(okno_a_in_c, text = odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
            c = tk.Button(okno_a_in_c, text = odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=0, column=1)
            okno_a_in_c.mainloop()
        if skoraj == 'd':
            okno_a_in_d = tk.Tk()
            a = tk.Button(okno_a_in_d, text = odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
            d = tk.Button(okno_a_in_d, text = odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=0, column=1)
            okno_a_in_d.mainloop()
        izkoriscena_polovicka = True
    if pravilen == 'b':
        if skoraj == 'a':
            okno_b_in_a = tk.Tk()
            a = tk.Button(okno_b_in_a, text = odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
            b = tk.Button(okno_b_in_a, text = odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=1)
            okno_b_in_a.mainloop()
        if skoraj == 'c':
            okno_b_in_c = tk.Tk()
            b = tk.Button(okno_b_in_c, text = odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=0)
            c = tk.Button(okno_b_in_c, text = odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=0, column=1)
            okno_b_in_c.mainloop()
        if skoraj == 'd':
            okno_b_in_d = tk.Tk()
            b = tk.Button(okno_b_in_d, text = odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=0)
            d = tk.Button(okno_b_in_d, text = odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=0, column=1)
            okno_b_in_d.mainloop()
        izkoriscena_polovicka = True
    if pravilen == 'c':
        if skoraj == 'a':
            okno_c_in_a = tk.Tk()
            a = tk.Button(okno_c_in_a, text = odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
            c = tk.Button(okno_c_in_a, text = odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=0, column=1)
            okno_c_in_a.mainloop()
        if skoraj == 'b':
            okno_c_in_b = tk.Tk()
            b = tk.Button(okno_c_in_a, text = odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=0)
            c = tk.Button(okno_c_in_a, text = odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=0, column=1)
            okno_c_in_b.mainloop()
        if skoraj == 'd':
            okno_c_in_d = tk.Tk()
            c = tk.Button(okno_c_in_d, text = odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=0, column=0)
            d = tk.Button(okno_c_in_d, text = odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=0, column=1)
            okno_c_in_d.mainloop()
        izkoriscena_polovicka = True
    if pravilen == 'd':
        if skoraj == 'a':
            okno_d_in_a = tk.Tk()
            a = tk.Button(okno_d_in_a, text = odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
            d = tk.Button(okno_d_in_a, text = odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=0, column=1)
            okno_d_in_a.mainloop()
        if skoraj == 'b':
            okno_d_in_b = tk.Tk()
            b = tk.Button(okno_d_in_b, text = odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=0)
            d = tk.Button(okno_d_in_b, text = odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=0, column=1)
            okno_d_in_b.mainloop()
        if skoraj == 'c':
            okno_d_in_c = tk.Tk()
            c = tk.Button(okno_d_in_c, text = odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=0, column=0)
            d = tk.Button(okno_d_in_c, text = odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=0, column=1)
            okno_d_in_c.mainloop()
        izkoriscena_polovicka = True
    #else:
        #poraba_polovicka= tk.Tk()
        #polovicka_poraba = tk.Label(poraba_polovicka, text='Žal ste polovičko že porabili')
        #poraba_poraba.pack()
        #poraba_polovicka.mainloop()
        

def glas_ljudstva(x, y):
    #global izkoriscen_glas_ljudstva
    pravilen_odgovor = resitve[x]
    moznost_zgresitve = y * 0.06
    #if izkoriscen_glas_ljudstva == False:
    if pravilen_odgovor == 'a':
        ostalo = moznost_zgresitve
        b = round(random.uniform(0, moznost_zgresitve), 2)
        c = round(random.uniform(0, moznost_zgresitve - b), 2)
        d = round((moznost_zgresitve - b - c), 2) 
        vsota_je_sto = [round((1 - moznost_zgresitve), 2)  * 100,b * 100 ,c * 100 ,d * 100]
        #izkoriscen_glas_ljudstva = True
    if pravilen_odgovor == 'b':
        ostalo = moznost_zgresitve
        a = round(random.uniform(0, moznost_zgresitve), 2)
        c = round(random.uniform(0, moznost_zgresitve - a), 2)
        d = round((moznost_zgresitve - a - c), 2) 
        vsota_je_sto = [a  * 100,round((1 - moznost_zgresitve), 2) * 100 ,c * 100 ,d * 100]
        #izkoriscen_glas_ljudstva = True
    if pravilen_odgovor == 'c':
        ostalo = moznost_zgresitve
        a = round(random.uniform(0, moznost_zgresitve), 2)
        b = round(random.uniform(0, moznost_zgresitve - a), 2)
        d = round((moznost_zgresitve - a - b), 2)  
        vsota_je_sto = [a  * 100,b * 100 ,round((1 - moznost_zgresitve), 2) * 100 ,d * 100]
        #izkoriscen_glas_ljudstva = True
    if pravilen_odgovor == 'd':
        ostalo = moznost_zgresitve
        a = round(random.uniform(0, moznost_zgresitve), 2)
        b = round(random.uniform(0, moznost_zgresitve - a), 2)
        c = round((moznost_zgresitve - a - b), 2) 
        vsota_je_sto = [a  * 100,b * 100 ,c * 100 ,round((1 - moznost_zgresitve), 2)* 100]
        #izkoriscen_glas_ljudstva = True
    #else:
        #poraba_glas = tk.Tk()
        #glas_poraba = tk.Label(poraba_glas, text='Žal ste glas ljudstva že porabili')
        #glas_poraba.pack()
        #poraba_glas.mainloop()

    '''ljudstvo = input(odgovori1[x] + ' ' + str(vsota_je_sto[0]) + '%' + '\n' +
                     odgovori2[x] + ' ' + str(vsota_je_sto[1]) + '%' + '\n' +
                     odgovori3[x] + ' ' + str(vsota_je_sto[2]) + '%' + '\n' +
                     odgovori4[x] + ' ' + str(vsota_je_sto[3]) + '%' + '\n')'''
    oknoglasljudstva = tk.Tk()
    tk.Button(oknoglasljudstva, text=odgovori1[x] + ' ' + str(vsota_je_sto[0]) + '%', command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0)
    tk.Button(oknoglasljudstva, text=odgovori2[x] + ' ' + str(vsota_je_sto[1]) + '%', command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=1)
    tk.Button(oknoglasljudstva, text=odgovori3[x] + ' ' + str(vsota_je_sto[2]) + '%', command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=1, column=0)
    tk.Button(oknoglasljudstva, text=odgovori4[x] + ' ' + str(vsota_je_sto[3]) + '%', command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=1, column=1)
    oknoglasljudstva.mainloop()



def novo_okno(x):
    okno2= tk.Tk()
    prvi=tk.Frame(okno2)
    prvi.pack()
    drugi=tk.Frame(okno2)
    drugi.pack()
    vpr= tk.Label(prvi, text= vprasanja[x])
    vpr.pack()
    tretji=tk.Frame(okno2)
    tretji.pack()
    cetrti=tk.Frame(okno2)
    cetrti.pack()
    tk.Button(drugi, text=odgovori1[x], command = lambda:gumb_preveri_odgovor_a(x, y)).grid(row=0, column=0) 
    tk.Button(drugi, text=odgovori2[x], command = lambda:gumb_preveri_odgovor_b(x, y)).grid(row=0, column=1) 
    tk.Button(drugi, text=odgovori3[x], command = lambda:gumb_preveri_odgovor_c(x, y)).grid(row=1, column=0)
    tk.Button(drugi, text=odgovori4[x], command = lambda:gumb_preveri_odgovor_d(x, y)).grid(row=1, column=1) 
    gumb_za_polovicko = tk.Button(tretji, text='POLOVIČKA', command = lambda: polovicka(x)).grid(row=0, column=0)
    gumb_za_glas_ljudstva = tk.Button(tretji, text='GLAS LJUDSTVA',command = lambda: glas_ljudstva(x, y)).grid(row=0, column=1)
    gumb_za_izhod = tk.Button(cetrti, text='IZHOD', command = lambda: izhod(stanje))
    gumb_za_izhod.pack()
    vprasanja_ze_bla.append(x)
    okno2.mainloop 

def novo_in_naslednje_vprasanje():
    global y 
    y += 1
    if stanje == 1000000:
        zmagovalnookno = tk.Tk()
        cestitka = tk.Label(zmagovalnookno, text='Čestitamo, osvojili ste PRVO nagrado!')
        cestitka.pack()
    x = random.randint(0, len(resitve)-1)
    if x not in vprasanja_ze_bla:
            novo_okno(x)

def zapri_okno():
    novo_in_naslednje_vprasanje()
    okno.destroy()




    
navodila = tk.Label(okno,text='''Dobrodošli v Milijonarju o Sloveniji!
Denarna nagrada znaša 1.000.000€.
Odgovorite tako, da napište kliknete odgovor, za katerega mislite, da je pravilen.
Na voljo imate tudi polovičko in glas ljudstva.
Polovičke in glasu ljusdtva ne morete izkoristiti pri istem vprašanju.''')
navodila.pack()
stanje = 0
y = -1
vprasanja_ze_bla = []
izkoriscena_polovicka = False
izkoriscen_glas_ljudstva = False
gumb1 = tk.Button(okno, text='Začni!', command = zapri_okno)
gumb1.pack()

okno.mainloop() 
