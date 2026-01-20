# CGame – Simulare de gestionare a unui oraș

## Descriere generală
Acest proiect reprezintă o **simulare în consolă** care modelează procesul de luare a deciziilor într-un oraș cu **resurse limitate**.  
Utilizatorul joacă rolul unui administrator care trebuie să gestioneze eficient resursele orașului pentru a preveni intrarea acestuia în criză.

Proiectul a fost realizat pentru concursul **CGame – Poveste și Provocare**, având ca scop evidențierea modului în care **algoritmii pot fi aplicați în situații reale**.

---

## Problema abordată
În viața reală, orice sistem (oraș, familie, companie) funcționează cu resurse limitate.  
Deciziile luate într-un moment influențează evoluția sistemului pe termen scurt și lung.

Această simulare urmărește:
- să evidențieze relația **cauză–efect** dintre decizii și resurse
- să demonstreze importanța **prioritizării** și a **planificării**
- să ilustreze utilizarea unui algoritm simplu pentru modelarea unui sistem real

---

## Cum funcționează simularea
Orașul este caracterizat prin mai multe resurse:
- ⚡ Energie
- 💧 Apă
- 💰 Buget

Jocul este structurat pe **zile**. În fiecare zi:
1. Se afișează starea curentă a orașului
2. Utilizatorul alege o acțiune
3. Resursele sunt actualizate în funcție de decizie
4. Se aplică un consum zilnic al resurselor

Simularea continuă atât timp cât toate resursele au valori pozitive.  
Atunci când una dintre resurse ajunge la zero, orașul intră în criză, iar jocul se încheie.

---

## Algoritmul utilizat
Proiectul se bazează pe un algoritm iterativ, implementat printr-o **buclă `while`**, care rulează atâta timp cât sistemul rămâne funcțional.

Structura logică a algoritmului este:
- inițializarea resurselor
- repetarea ciclului zilnic:
  - afișare stare
  - luare decizie
  - actualizare resurse
  - verificare condiții de oprire

Această abordare permite modelarea unui sistem dinamic într-un mod clar și ușor de înțeles.

---

## Tehnologii utilizate
- **Python 3**
- Aplicație rulată în **consolă**
- Controlul versiunilor realizat cu **Git**

---

## Dezvoltarea proiectului
Proiectul a fost realizat **incremental**, pornind de la un **MVP (Minimum Viable Product)**, care include mecanica de bază a simulării.  
Ulterior, funcționalitățile pot fi extinse în mod controlat, în funcție de timp și complexitate.

Această metodă de dezvoltare asigură stabilitate și claritate logică.

---

## Concluzie
Deși algoritmul utilizat este simplu, acesta demonstrează modul în care programarea poate fi folosită pentru a simula situații reale și pentru a sprijini procesul decizional.

Proiectul pune accent pe **logică, claritate și aplicabilitate**, nu pe complexitate inutilă.
