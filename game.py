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

    optiune = (input(f"""Ce decizie iei astăzi?

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
f"""==============================
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

def pauza():
    input("\n Apasa ENTER ca sa continui...")

def AI_Predictor(buget, energie, apa):
    
    #Logica: „Dacă aleg X azi, cât de riscant e pe termen scurt?”
    valori = ['1', '2', '3']
    
    scor_riscuri = {
        "Mic": 0,
        "Mediu": 1,
        "Mare": 2,
        "Critic": 3,
        "IMPOSIBIL": 4
    }
    riscuri = {}

    BEST_CASE_VALUE = 100
    BEST_CASE_SCENARIO = ""

    for decizie in valori:

        buget0 = buget
        apa0 = apa
        energie0 = energie

        buget_sim = buget0
        apa_sim = apa0
        energie_sim = energie0

        if(decizie == '1' and (buget_sim < cost_energie)):
            riscul = "IMPOSIBIL"
            riscuri[decizie] = riscul
            continue
        elif(decizie == '2' and (buget_sim < cost_apa)):
            riscul = "IMPOSIBIL"
            riscuri[decizie] = riscul
            continue

        if(decizie == '1'):
            energie_sim = energie_sim + (4 * cons_zilnic_energie)
            buget_sim = buget_sim - cost_energie
        elif(decizie == '2'):
            apa_sim = apa_sim + (4 * cons_zilnic_apa)
            buget_sim = buget_sim - cost_apa
        else:
            pass

        energie_sim = energie_sim - 3 * cons_zilnic_energie
        apa_sim = apa_sim - 3 * cons_zilnic_apa

        #Stabilim ce fel de risc avem
        riscul = ""
        if(energie_sim <= 0 or apa_sim <= 0 or buget_sim <= 0):
            riscul = "Critic"
        else:
            zE = energie_sim // cons_zilnic_energie
            zA = apa_sim // cons_zilnic_apa
            zMin = min(zE, zA)
            
            if(zMin <= 1):
                riscul = 'Mare'
            elif(zMin <= 3):
                riscul = "Mediu"
            else:
                riscul = "Mic"
        
        riscuri[decizie] = riscul
        
        
        if(scor_riscuri[riscuri[decizie]] < BEST_CASE_VALUE): 
            BEST_CASE_VALUE = scor_riscuri[riscuri[decizie]]
            BEST_CASE_SCENARIO = decizie

    return riscuri, BEST_CASE_SCENARIO
#Initializam Resursele
buget = 35
energie = 50
apa = 45

#Tinem cont de ziua in care ne aflam stabilind progresul orasului
zi = 1

while(energie > 0 and apa > 0 and buget > 0):

    
    riscuri, best = AI_Predictor(buget, energie, apa)
    print("\n🤖 ====== AI Predictor (forecast 3 zile) ======")
    print(f"Optiunea 1: {riscuri.get('1')}")
    print(f"Optiunea 2: {riscuri.get('2')}")
    print(f"Optiunea 3: {riscuri.get('3')}")

    if best != "":
        print(f"✅ AI recomanda: Optiunea {best} (risc minim)")

    else:
        print("⚠️ AI: Nicio optiune valida (buget prea mic pentru investitii)")

    #Afisam situatia actuala a orasului
    #Userul decide ce optiune strategica se potriveste pentru orasul sau
    optiune = status_decision(zi, buget, energie, apa)
    if(optiune == "1"):

        if not efect(buget, cost_energie):
            continue

        #Dupa investitie bugetul scade cu 12 u.m., aceasta fiind suma platita pentru centrala electrica
        buget = buget - cost_energie

        #Energia creste pentru inca 3-5 zile dupa instalarea unei centrale electrice
        crestere_energie = efectul_investitiei(cons_zilnic_energie)
        energie = energie + crestere_energie

        print(f"\n-{cost_energie}: Buget")
        print(f"+{crestere_energie}: Energie")
    elif(optiune == "2"):

        if not efect(buget, cost_apa):
            continue

        #Cresterea apei creste aproximativ de 3-5 * consum zilnic
        crestere_apa = efectul_investitiei(cons_zilnic_apa)
        apa = apa + crestere_apa

        #Scadem din buget costul unei investitii in apa
        buget = buget - cost_apa

        print(f"\n-{cost_apa}: Buget")
        print(f"+{crestere_apa}: Apa")

    elif (optiune == "3"):
        #Nu faci nimic
        print("\nAi ales să nu iei nicio măsură azi.")

    else:
        print("\nAlege 1, 2 sau 3.\n")
        continue

    #Orasul pierde din resurse la finalul zilei

    print("\n==========Consumabile===========\n")
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

    #Vrem ca userul sa aiba timp sa citeasca update-urile fara sa sara la ziua urmatoare
    pauza()

    #Trecem la ziua urmatoare
    zi = zi + 1

if(buget <= 0 or energie <= 0 or apa <= 0):
    game_over(zi,buget,energie,apa)