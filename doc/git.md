# Comandi utili con Git

Ecco una lista di comnadi che possono far comodo utilizzando git

## clone

Crea una copia completa del repo.

Sintassi (da eseguire nella cartella in cui si vuole):

```bash
git clone git@github.com:ConoscereLinux/DeskApp.git
```

## fetch

Scarica gli aggiornamenti remoti, relativi a tutto il repo. Non tocca la
cartella di lavoro.

Sintassi:

```bash
git fetch
```

## pull

Scarica gli aggiornamenti dal ramo upstream di GitHub.

Sintassi:

```bash
git pull <nome ramo remoto>
```

## push

Manda gli aggiornamenti verso il ramo upstream di GitHub.

Sintassi:

```bash
git push <nome ramo remoto>
```

## branch

Crea un nuovo branch (ramo) partendo da quello attuale (comportamento default).

Sintassi (esempio):

```bash
git branch feature/<nome funzione>
```

## checkout

Visualizza il nome del ramo in cui ci troviamo o ci consete di cambiare ramo.

Sintassi:

```bash
git chckout
```

Oppure:

```bash
git checkout <nome ramo>
```
