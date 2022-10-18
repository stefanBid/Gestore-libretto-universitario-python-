`version: 1.0`
# Gestore libretto universitario (Python)

## Introduzione
Questo progetto riguarda la creazione di un applicativo privo di interfaccia utente per la gestione del proprio libretto universitario.

## Implementazione

L'applicativo permette di eseguire le seguenti operazioni:
- Creare il libretto;
- Registrare un esame a libretto (nome, cfu, voto)
- Rimuovere un esame dal libretto
- Aggiornare (nome, cfu, voto) di un esame
- Selezionare esami in base a dei crieri di ricerca
- Fornire informazioni relative alla media, media ponderata e proiezione di laurea


## Info utili 
Per gestire i dati si è utilizzato [DB Browser per sqlite](https://sqlitebrowser.org/).
Il DB viene creato automaticamente alla prima esecuzione dell'aplicativo, lo stesso verrà consultato le volte successive in cui l'applicativo verrà rieseguito

Puoi importare un file il file `gestoreDB.py` nel tuo progetto e scaricare automaticamente tutte le librerie richieste, per una semplicità di tilizzo ti consiglio l'IDE [PyCharm](https://www.jetbrains.com/pycharm/)


---
Fanne buon uso :)
