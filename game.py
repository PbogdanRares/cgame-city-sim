import random

#Consum si Costuri pentru investitii, respectiv exploatarea resurselor
cons_zilnic_apa = 8
cons_zilnic_energie = 10
cost_apa = 9
cost_energie = 12

#Salarii si Taxe ce ne ajuta la venitul saptamanal(Ideal era lunar, dar dura prea mult pana la salariu, facand jocul imposibil de jucat)
BONUS_SAPTAMANAL_BAZA = 8
PRAG_TAXE_ENERGIE = 20
PRAG_TAXE_APA = 20

#Tot codul repetitiv ce poate fi automatizat vine aici

#Contine alegerile posibile pentru user si returneaza alegerea acestuia
def status_decision(zi, buget, energie, apa):
    print("\n\n")
    print("==============================")
    print("Ziua " + str(zi))
    print("------------------------------")
    print("Bugetul:  " + str(buget))
    print("Energia:  " + str(energie))
    print("Apa:      " + str(apa) + '\n' + '\n')

    optiune = int(input(f"""Ce decizie iei astăzi?

    [1] Construiești o centrală electrică (Cost: -{cost_energie} buget)
        + Energie (impact 3–5 zile echivalent)
        Consum zilnic: -{cons_zilnic_energie} energie, -{cons_zilnic_apa} apă

    [2] Repari rețeaua de apă (Cost: -{cost_apa} buget)
        + Apă (impact 3–5 zile echivalent)
        Consum zilnic: -{cons_zilnic_energie} energie, -{cons_zilnic_apa} apă

    [3] Nu iei nicio măsură (Cost: 0)
        Doar consumul zilnic se aplică

    Introdu opțiunea (1 / 2 / 3): """))
    return optiune


#Observam daca user-ul are banii necesari pentru o noua investitie
def efect(buget, scaderea):
    
    #Verificam daca mai avem bani pentru a face o investitie
    if(buget - scaderea < 0):
        print(
    """
    \n \n
    Bugetul orașului a fost complet epuizat.
    Lipsa fondurilor a dus la imposibilitatea continuării
    investițiilor esențiale pentru energie și apă.

    Orașul a ajuns într-un punct fără întoarcere,
    iar administrația este nevoită să își înceteze activitatea.

    Va rugam sa alegeti alta optiune. Multumim!

    Buget final: """ + str(buget) + '\n' + '\n'
    )
        return False
    return True
    
#Generam un numar ce reprezinta impactul investitiei asupra orasului(influenteaza cresterea apei/energiei)
def efectul_investitiei(consum):
    return random.randrange(3, 6) * consum
        
#Mesajul dupa ce ai ramas fara resurse
def game_over(zi, buget, energie, apa):
    print(
        f""" \n
==============================
        GAME OVER
==============================

Resursele orașului au fost complet epuizate.

Fără energie și apă, infrastructura s-a prăbușit,
iar viața urbană nu mai poate continua.

Deciziile luate de-a lungul zilelor au dus
orașul într-un punct fără întoarcere.

Ziua finală: {zi}
Buget final: {buget}
Energie finală: {energie}
Apă finală: {apa}

Administrația orașului își încheie mandatul.\n"""
    )


#Initializam Resursele
buget = 35
energie = 50
apa = 45

#Tinem cont de ziua in care ne aflam stabilind progresul orasului
zi = 1

while(energie > 0 and apa > 0 and buget > 0):

    #Afisam situatia actuala a orasului
    #Userul decide ce optiune strategica se potriveste pentru orasul sau
    optiune = status_decision(zi, buget, energie, apa)

    if(optiune == 1):

        if not efect(buget, cost_energie):
            continue

        #Dupa investitie bugetul scade cu 12 u.m., aceasta fiind suma platita pentru centrala electrica
        buget = buget - cost_energie

        #Energia creste pentru inca 3-5 zile dupa instalarea unei centrale electrice
        crestere_energie = efectul_investitiei(cons_zilnic_energie)
        energie = energie + crestere_energie

        print(f"\n-{cost_energie}: Buget")
        print(f"+{crestere_energie}: Energie")
    elif(optiune == 2):

        if not efect(buget, cost_apa):
            continue

        #Cresterea apei creste aproximativ de 3-5 * consum zilnic
        crestere_apa = efectul_investitiei(cons_zilnic_apa)
        apa = apa + crestere_apa

        #Scadem din buget costul unei investitii in apa
        buget = buget - cost_apa

        print(f"\n-{cost_apa}: Buget")
        print(f"+{crestere_apa}: Apa")

    elif (optiune == 3):
        #Nu faci nimic
        print("\nAi ales să nu iei nicio măsură azi.")

    else:
        print("\nAlege 1, 2 sau 3.\n")
        continue

    #Orasul pierde din resurse la finalul zilei

    print("\n==========Consumabile===========")
    print(f"-{cons_zilnic_energie}: Energie")
    print(f"-{cons_zilnic_apa}: Apa")
    energie -= cons_zilnic_energie
    apa -= cons_zilnic_apa

    #Daca e sfarsit de saptamana atunci primim un venit care variaza si nu este constant
    #prag_taxe_energie/apa inseamna ca o unitate monetara are loc daca ex: energia = 20 si pragul e 20 => +1 u.m
    if(zi % 7 == 0):
        taxe = max(0, energie) // PRAG_TAXE_ENERGIE + max(0, apa) // PRAG_TAXE_APA
        bonus = BONUS_SAPTAMANAL_BAZA + taxe
        buget += bonus
        print("\n🏦 ====== Bonus saptamanal ======")
        print(f"+{bonus}: Buget (baza {BONUS_SAPTAMANAL_BAZA} + taxe {taxe})")

    zi = zi + 1

if(buget <= 0 or energie <= 0 or apa <= 0):
    game_over(zi,buget,energie,apa)