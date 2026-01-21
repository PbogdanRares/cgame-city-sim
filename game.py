import random

#Tot codul repetitiv ce poate fi automatizat vine aici

#Contine alegerile posibile pentru user si returneaza alegerea acestuia
def status_decision(zi, buget, energie, apa):
    print("==============================")
    print("Ziua " + str(zi))
    print("------------------------------")
    print("Bugetul:  " + str(buget))
    print("Energia:  " + str(energie))
    print("Apa:      " + str(apa) + '\n')

    optiune = int(input(
    """Ce decizie iei astăzi?

    [1] Construiești o centrală electrică
        + Energie
        - Buget

    [2] Repari rețeaua de apă
        + Apă
        - Buget

    [3] Nu iei nicio măsură
        - Energie
        - Apă

    Introdu opțiunea (1 / 2 / 3): """
        ))
    return optiune


#Observam daca user-ul are banii necesari pentru o noua investitie
def efect(buget, scaderea):
    
    #Verificam daca mai avem bani pentru a face o investitie
    if(buget - scaderea < 0):
        print(
    """
    \n
    Bugetul orașului a fost complet epuizat.
    Lipsa fondurilor a dus la imposibilitatea continuării
    investițiilor esențiale pentru energie și apă.

    Orașul a ajuns într-un punct fără întoarcere,
    iar administrația este nevoită să își înceteze activitatea.

    Va rugam sa alegeti alta optiune. Multumim!

    Buget final: """ + str(buget) + '\n'
    )
        return False
    return True
    
#Generam un numar ce reprezinta impactul investitiei asupra orasului(influenteaza cresterea apei/energiei)
def efectul_investitiei(consum):
    return random.randrange(3, 6) * consum
        
#Mesajul dupa ce ai ramas fara resurse
def game_over(buget, energie, apa):
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

Ziua finală:
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

    #Stabilim cate resurse se folosesc zilnic pentru orasul nostru
    cons_zilnic_energie = 10
    cons_zilnic_apa = 8

    if(optiune == 1):

        # pretul unei centrale electrice
        scadere_bani = 12

        if(efect(buget, scadere_bani)== False):
            continue


        #Dupa investitie bugetul scade cu 12 u.m., aceasta fiind suma platita pentru centrala electrica
        buget = buget - scadere_bani

        #Energia creste pentru inca 3-5 zile dupa instalarea unei centrale electrice
        crestere_energie = efectul_investitiei(cons_zilnic_energie)
        energie = energie + crestere_energie
        
    elif(optiune == 2):
        #Pretul de investitie pentru apa
        scadere_bani = 9

        if(efect(buget, scadere_bani) == False):
            continue

        #Cresterea apei creste aproximativ de 3-5 * consum zilnic
        crestere_apa = efectul_investitiei(cons_zilnic_apa)
        apa = apa + crestere_apa

        #Scadem din buget costul unei investitii in apa
        buget = buget - scadere_bani

    elif (optiune == 3):
        #Nu faci nimic
        pass

    else:
        print("Alege 1, 2 sau 3.")
        continue
    
    #Orasul pierde din resurse la finalul zilei
    energie -= cons_zilnic_energie
    apa -= cons_zilnic_apa

    zi = zi + 1

if(buget <= 0 or energie <= 0 or apa <= 0):
    game_over(buget,energie,apa)