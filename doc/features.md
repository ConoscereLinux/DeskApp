# Specifiche DeskApp

Questo programma partendo da una cartella base, specificata, raccoglierà i file di un tipo specificato in una lista, e ne crea un indice, consultabile.

## Funzionalità

- Parser comandi da command line
- Gestione Log organica e centralizzata
- Interfaccia grafica con Qt tramite PySide6
- Inizialmente un percorso base di ricerca (la funzione verrà espansa)
- Filtri sui tipi di file o nome del file (gestito tramite RegEx)
- Indicizazzione du database (inizialmente SQLite)
- Raccolta di metadati sui file, tramite funzioni specializzate

## Funzionalità II

- Filtri sui tipi di file tramite Mime Type (se non posso basarmi sull'estensione devo guardare il contenuto)
- Upgrade del database a PostgreSQL
