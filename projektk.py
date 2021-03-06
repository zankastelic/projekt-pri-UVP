import random
import tkinter as tk

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
'Kako imenujemo turistično prireditev, povezano s splavarjenjem v Ljubnem ob Savinji?', 
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
'B: Flosarski bal',
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
'C: Savinjski bal',
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
'D: Splavarsko popoldne',
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
polovicke = ['b','d','d','c','a','d','b','c','d','b','b','d','d','a','a','a','b','b','b','c','c','c','a','a','b','a','d','a','b','a','b','a','d','b','d',
             'a','b','a','c','a','a','c','b','c','b','a','c','d','d','d'] 

nagrada = [100 , 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]


def polovicka(x):
    pravilen = resitve[x]
    skoraj = polovicke[x]
    if pravilen == 'a':
        if skoraj == 'b':
            polovicca = input(odgovori1[x] + '\n' +
                              odgovori2[x] + '\n')
        if skoraj == 'c':
            polovicca = input(odgovori1[x] + '\n' +
                              odgovori3[x] + '\n')
        if skoraj == 'd':
            polovicca = input(odgovori1[x] + '\n' +
                              odgovori4[x] + '\n')
    if pravilen == 'b':
        if skoraj == 'a':
            polovicca = input(odgovori1[x] + '\n' +
                              odgovori2[x] + '\n')
        if skoraj == 'c':
            polovicca = input(odgovori2[x] + '\n' +
                              odgovori3[x] + '\n')
        if skoraj == 'd':
            polovicca = input(odgovori2[x] + '\n' +
                              odgovori4[x] + '\n')     
    if pravilen == 'c':
        if skoraj == 'a':
            polovicca = input(odgovori1[x] + '\n' +
                              odgovori3[x] + '\n')
        if skoraj == 'b':
            polovicca = input(odgovori2[x] + '\n' +
                              odgovori3[x] + '\n')
        if skoraj == 'd':
            polovicca = input(odgovori3[x] + '\n' +
                              odgovori4[x] + '\n')
    if pravilen == 'd':
        if skoraj == 'a':
            polovicca = input(odgovori1[x] + '\n' +
                              odgovori4[x] + '\n')
        if skoraj == 'b':
            polovicca = input(odgovori2[x] + '\n' +
                              odgovori4[x] + '\n')
        if skoraj == 'c':
            polovicca = input(odgovori3[x] + '\n' +
                              odgovori4[x] + '\n')
    return polovicca



'''def polovicka1(x):
    pravilen_odgovor = resitve[x]
    if pravilen_odgovor == 'a':
        polovica = input(odgovori1[x] + '\n' +
                         random.choice([odgovori2[x],odgovori3[x],
                                        odgovori4[x]]) + '\n')

    if pravilen_odgovor == 'b':
        polovica = input(odgovori2[x] + '\n' +
                         random.choice([odgovori1[x],odgovori3[x],
                                        odgovori4[x]]) + '\n')
    if pravilen_odgovor == 'c':
        polovica = input(odgovori3[x] + '\n' +
                         random.choice([odgovori1[x],odgovori2[x],
                                        odgovori4[x]]) + '\n')

    if pravilen_odgovor == 'd':
        polovica = input(odgovori4[x] + '\n' +
                         random.choice([odgovori1[x],odgovori2[x],
                                        odgovori3[x]]) + '\n')'''

def glas_ljudstva(x, y):
    pravilen_odgovor = resitve[x]
    moznost_zgresitve = y * 0.05
    if pravilen_odgovor == 'a':
        ostalo = moznost_zgresitve
        b = round(random.uniform(0, moznost_zgresitve), 2)
        c = round(random.uniform(0, moznost_zgresitve - b), 2)
        d = round((moznost_zgresitve - b - c), 2) 
        vsota_je_sto = [round((1 - moznost_zgresitve), 2)  * 100,b * 100 ,c * 100 ,d * 100]
    if pravilen_odgovor == 'b':
        ostalo = moznost_zgresitve
        a = round(random.uniform(0, moznost_zgresitve), 2)
        c = round(random.uniform(0, moznost_zgresitve - a), 2)
        d = round((moznost_zgresitve - a - c), 2) 
        vsota_je_sto = [a  * 100,round((1 - moznost_zgresitve), 2) * 100 ,c * 100 ,d * 100]
    if pravilen_odgovor == 'c':
        ostalo = moznost_zgresitve
        a = round(random.uniform(0, moznost_zgresitve), 2)
        b = round(random.uniform(0, moznost_zgresitve - a), 2)
        d = round((moznost_zgresitve - a - b), 2)  
        vsota_je_sto = [a  * 100,b * 100 ,round((1 - moznost_zgresitve), 2) * 100 ,d * 100]
    if pravilen_odgovor == 'd':
        ostalo = moznost_zgresitve
        a = round(random.uniform(0, moznost_zgresitve), 2)
        b = round(random.uniform(0, moznost_zgresitve - a), 2)
        c = round((moznost_zgresitve - a - b), 2) 
        vsota_je_sto = [a  * 100,b * 100 ,c * 100 ,round((1 - moznost_zgresitve), 2)* 100]

    ljudstvo = input(odgovori1[x] + ' ' + str(vsota_je_sto[0]) + '%' + '\n' +
                     odgovori2[x] + ' ' + str(vsota_je_sto[1]) + '%' + '\n' +
                     odgovori3[x] + ' ' + str(vsota_je_sto[2]) + '%' + '\n' +
                     odgovori4[x] + ' ' + str(vsota_je_sto[3])  + '%' + '\n')
    return ljudstvo

def izhod(stanje):
    print('Četitamo zadeli ste',stanje,'€!')
    print('Igra se zapira ...')
    
def milijonar():
    stanje = 0
    y = 0
    print('''Dobrodošli v Milijonarju o Sloveniji!''')
    print('''Denarna nagrada znaša 1.000.000€.''')
    print('''Odgovorite tako, da napište črko, za katero mislite, da je odgovor pravilen npr(a).''') 
    print('''Na voljo imate tudi polovičko (če jo želite izkoristiti napišete 'polovička'). ''')
    print('''Prav tako imate na voljo glas ljudstva (če jo želite izkoristiti napišete 'glas ljudstva'). ''')
    print('''Polovičke in glasu ljudstva ne morete izkoristiti pri istem vprašanju.''' + '\n')
    
    vprasanja_ze_bla = []
    izkoriscena_polovicka = False
    izkoriscen_glas_ljudstva = False
    while True:
        x = random.randint(0, len(resitve)-1)
        
        if stanje == 1000000:
            print('Čestitamo, osvojili ste PRVO nagrado!')
            break
        if x not in vprasanja_ze_bla:
            #print("TESTING: odgovor", resitve[x],vprasanja_ze_bla)
            primer = input(izpisi_vprasanje(x))
            primer = preveri(primer,izkoriscena_polovicka,izkoriscen_glas_ljudstva,x)
            if primer == resitve[x]:
                stanje = nagrada[y]
                y += 1 
                print('Bravo prislužili ste si ' + str(stanje) + ' €!')
            elif primer.lower() == 'polovička':
                primer = polovicka(x)
                izkoriscena_polovicka = True
                if primer == resitve[x]:
                    stanje = nagrada[y]
                    y += 1 
                    print('Bravo prislužili ste si ' + str(stanje) + ' €!')
                elif primer == 'glas ljudstva':
                    print('Pri istem vprašanju ne morete izkoristiti obeh možnosti.')
                    primer = polovicka(x)
                    stanje = nagrada[y]
                    y += 1 
                    print('Bravo prislužili ste si ' + str(stanje) + ' €!')
                else:
                    print('Žal je ta odgovor napačen! Hvala za Vaš trud. Več sreče prihodnjič! ')
                    break
            elif primer.lower() == 'glas ljudstva':
                primer = glas_ljudstva(x, y)
                izkoriscen_glas_ljudstva = True
                if primer == resitve[x]:
                    stanje = nagrada[y]
                    y += 1 
                    print('Bravo prislužili ste si ' + str(stanje) + ' €!')
                elif primer == 'polovička':
                    print('Pri istem vprašanju ne morete izkoristiti obeh možnosti.')
                    primer = glas_ljudstva(x, y)
                    stanje = nagrada[y]
                    y += 1 
                    print('Bravo prislužili ste si ' + str(stanje) + ' €!')
                else:
                    print('Žal je ta odgovor napačen! Hvala za Vaš trud. Več sreče prihodnjič! ')
                    break
            elif primer.lower() == 'izhod':
                izhod(stanje) 
                break
            else:
                print('Žal je ta odgovor napačen! Hvala za Vaš trud. Več sreče prihodnjič! ')
                break
            
            vprasanja_ze_bla.append(x)

def izpisi_vprasanje(x):
    return vprasanja[x] + '\n' + odgovori1[x] + '\n' + odgovori2[x] + '\n' + odgovori3[x] + '\n' + odgovori4[x] + '\n'

def preveri(primer, izkoriscena_polovicka, izkoriscen_glas_ljudstva,x):
    porabljeno = True
    while porabljeno:
        porabljeno = False
        if izkoriscena_polovicka and izkoriscen_glas_ljudstva:
            if primer == 'polovička':
                porabljeno = True
                primer = input('polovičko si že porabil \n' + izpisi_vprasanje(x))
            if primer == 'glas ljudstva':
                porabljeno = True
                primer = input('glas ljudstva si že porabil \n' + izpisi_vprasanje(x))
        elif izkoriscena_polovicka:
            if primer == 'polovička':
                porabljeno = True
                primer = input('polovičko si že porabil \n' + izpisi_vprasanje(x))
        elif izkoriscen_glas_ljudstva:
            if primer == 'glas ljudstva':
                porabljeno = True
                primer = input('glas ljudstva si že porabil \n' + izpisi_vprasanje(x))
            
    return primer
            
            
            
milijonar()


    

        
