import sqlite3
import os

nomeDB = "libretto.sqlite"
opDB = ("ins", "del", "upd", "info", "ext")  # Lasciare il comando (ext) sempre alla fine della tupla
upDB = ("vot", "cfu")


# Definiamo oggetto esame
class Esame:
    """Gestisce un esame universitario con -> Nome esame, voto e cfu"""

    def __init__(self, nomes: str = "", vot: int = 0, cfu: int = 0):
        self.nom_es = nomes
        self.vot_es = vot
        self.cfu_es = cfu

    def __str__(self):
        return f"Nome Esame: {self.nom_es}, Voto Esame: {self.vot_es}, Cfu Esame: {self.cfu_es}"


cwd = os.getcwd()  # Directory corrente
percorso_file = f"{cwd}/{nomeDB}"  # percorso file per raggiungere la posizione dove dovrà essere il nostro DB

# Controllo se il DB esiste
if os.path.exists(percorso_file):
    connection = sqlite3.connect(nomeDB)
    cur = connection.cursor()
else:
    # Solo se il DB non esiste e lo devo creare
    connection = sqlite3.connect(nomeDB)
    cur = connection.cursor()
    cur.execute("CREATE TABLE Libretto (Esame TEXT,Voto INTEGER,Cfu INTEGER)")

# Funzionamento automatico del DB
controllo = ""

while 1:
    print(f" KEY per operazioni su DB: [ext] -> Esci / [ins] -> Inserisci nel DB / [del] -> Rimuovi dal DB / "
          f"[upd]-> Modifica nel DB / [info] -> Seleziona dal DB")

    controllo = input("Dammi KEY:\t")

    if controllo == opDB[len(opDB) - 1]:  # Procedura per uscire
        connection.close()
        break
    elif controllo == opDB[0]:  # Procedura per inserimento nel DB
        nomeEs = input("Esamee da inserire nel DB:\t")
        voto = int(input("Voto da inserire nel DB:\t"))
        cfues = int(input("Cfu da inserire nel DB:\t"))
        cur.execute("INSERT INTO Libretto (Esame,Voto,Cfu) VALUES (?,?,?)", (nomeEs, voto, cfues))
        connection.commit()
        continue
    elif controllo == opDB[1]:  # Procedura per cancellare nel DB
        nomeEsDel = input("Esame da eliminare nel DB:\t")
        cur.execute("DELETE from Libretto WHERE Esame=(?)", (nomeEsDel,))
        connection.commit()
        continue

    elif controllo == opDB[2]:
        print("KEY per modificare esame nel DB: [vot] -> Modifica Vot / [cfu] -> Modifica Cfu")
        contr2 = input("Dammi KEY:\t")
        esUp = input("Dammi Esame da modificare:\t")
        if contr2 == upDB[0]:
            votUp = int(input("Dammi voto nuovo:\t"))
            cur.execute("UPDATE Libretto SET Voto=(?) WHERE Esame=(?)", (votUp, esUp))
            connection.commit()
        else:
            cfuUp = int(input("Dammi cfu nuovi:\t"))
            cur.execute("UPDATE Libretto SET Cfu=(?) WHERE Esame=(?)", (cfuUp, esUp))
            connection.commit()
        continue
    elif controllo == opDB[3]:
        cur.execute("SELECT Esame,Voto,Cfu FROM Libretto")
        esami = list()
        totvot = 0
        totvotpon = 0
        totcfu = 0
        med = 0
        medpon = 0
        for row in cur:
            esami.append(Esame(row[0], row[1], row[2]))

        for i in range(len(esami)):
            es = Esame()
            es = esami[i]
            totvot += es.vot_es
            totvotpon += es.vot_es * es.cfu_es
            totcfu += es.cfu_es
        med = round(totvot / len(esami), 2)
        medpon = round(totvotpon / totcfu, 2)
        proiezione = round((medpon * 11) / 3)
        print(f"Media: {med}\tMedia Ponderata: {medpon}\tProiezione di Laurea: {proiezione}")

        continue
    else:
        continue
