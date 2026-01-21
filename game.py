import random

#Initializam Resursele
buget = 35
energie = 50
apa = 45

#Tinem cont de ziua in care ne aflam stabilind progresul orasului
zi = 1

while(buget > 0 or energie > 0 or apa > 0):

    #Afisam situatia actuala a orasului
    print("==============================")
    print("Ziua " + str(zi))
    print("------------------------------")
    print("Bugetul:  " + str(buget))
    print("Energia:  " + str(energie))
    print("Apa:      " + str(apa) + '\n')

    #Userul decide ce optiune strategica se potriveste pentru orasul sau
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

    #Stabilim cate resurse se folosesc zilnic pentru orasul nostru
    cons_zilnic_energie = 10
    cons_zilnic_apa = 8

    if(optiune == 1):

        # pretul unei centrale electrice
        scadere_bani = 12

        #Verificam daca mai avem bani pentru a face o investitie
        if(buget - scadere_bani <= 0):
            buget = 0
            print("Buget insuficient pentru aceasta investitie\nBuget: " + str(buget))
            break

        #Dupa investitie bugetul scade cu 12 u.m., aceasta fiind suma platita pentru centrala electrica
        buget = buget - scadere_bani

        #Energia creste pentru inca 3-5 zile dupa instalarea unei centrale electrice
        crestere_energie = random.randrange(3, 6) * cons_zilnic_energie
        energie = energie + crestere_energie

        
        
    elif(optiune == 2):
        #Pretul de investitie pentru apa
        scadere_bani = 9

        #Verificam daca o investitie poate fi realizata
        if(buget - scadere_bani <= 0):
            buget = 0
            print(
"""
\n
Bugetul orașului a fost complet epuizat.
Lipsa fondurilor a dus la imposibilitatea continuării
investițiilor esențiale pentru energie și apă.

Orașul a ajuns într-un punct fără întoarcere,
iar administrația este nevoită să își înceteze activitatea.

Buget final: """ + str(buget) + '\n'
)
            break

        #Cresterea apei creste aproximativ de 3-5 * consum zilnic
        crestere_apa = random.randrange(3,6) * cons_zilnic_apa
        apa = apa + crestere_apa

        #Scadem din buget costul unei investitii in apa
        buget = buget - scadere_bani

    else:
        #Daca nu faci nimic, nu risti, nu iei o alegere sub tensiune, atunci atat apa, cat si energia vor scadea
        apa = apa - cons_zilnic_apa
        energie = energie - cons_zilnic_energie

    zi = zi + 1
