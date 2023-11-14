# Linguaggio di Markdown
Quida ai caratteri speciali e alle convenzioni utilizzate per una corretta formattazione del testo nel file Readme.MD. 
Viene anche utilizzata nei commenti delle classi e funzioni (la docstring) per automatizzare la documentazione mediante Sphinx
<br>

## Indice:
1. [Titoli](#Titoli)
2. [Escape \\](#Escape)
3. [Salto riga](#Salto-riga)
4. [Riga orizzontale](#Riga-orizzontale)
5. [Grassetto](#Grasseto)
6. [Corsivo](#Corsivo)
7. [Barrato](#Barrato)
8. [Link esterni](#Link-esterni)
9. [Elenchi](#Elenchi)
6. [Checklist](#Checklist)
7. [Codice Sorgente](#Codice-Sorgente)
8. [Immagini](#Immagini)
9. [Citazioni](#Citazioni)
10. [Emoji](#Emoji)
***


## Titoli
Per impostare i titoli si utilizza il # eguito da uno spazio. Se si mettono 2 ## avremo un titolo di 2° livello e così via fino al livello 5. Di seguito gli esempi:
# Titolo 1
## Titolo 2
### Titolo 3
#### Titolo 4
##### Titolo 5

<br>

## Escape
Il carattere di escape è il backslash \\. Viene utilizzato per disattivare le funzionalità di alcuni caratteri speciali e inserirli nel testo come gli altri normali caratteri.
Solo i seguenti caratteri possono essere inibiti tramite escape: 
\` (alt-96),  \*,  \_,  \{},  \[],  \(),  \#,  \+,  \-,  \.,  \!.

<br>

## Salto riga
Solo mettendo una riga vuota, si ha un salto di riga. un altro metodo è quello di utilizzare \<br\> simile all'HTML per inserire una interruzione di riga. Mettendone più di uno, si ottengono righe vuote.

<br>

## Riga orizzontale
Utilizzando 3 asterischi \*\*\* si possono inserire righe orizzontali di separazione

<br>

## Grassetto
Per fare il grassetto si utilizza un doppio asterico \** o un doppio underscore \__ all'inizio e alla fine della parte da mettere in grassetto. **Testo** __in grassetto__

<br>

## Corsivo
Per scrivere in corsivo si utilizza un asterisco \* o un underscore \_ all'inizio e alla fine della parte da mettere in corsivo. _Testo_ *in corsivo*.

<br>

## Barrato
Per inserire del testo barrato, si utilizza la doppia tilde \~~ all'inizio e alla fine della parte da barrare. ~~Testo barrato~~

<br>

## Link esterni
Per fare riferimento a documentazione o altre risorse su link esterni, basta inserirne l'URL e il sistema riconosce autonomamente il collegamento. https://github.com/ConoscereLinux/DeskApp

<br>

## Elenchi
Gli elenchi possono essere fatti sia con i numeri (elenchi numerati) che con punti (elenchi puntati).
Si utilizzano numeri seguiti da un punto (in sequenza) o punti. Ogni elemento dell'elenco deve essere su una nuova riga. Per effettuare dei sotto-punti basta far precedere il numero o il punto da un tabulatore. Punti e numeri possono anche essere utilizzati nello stesso elenco:

<br>

1. Uno  (con "1." ad inizio riga)
2. Due  (con "2." ad inizio riga)
3. Tre  (con "3." ad inizio riga

* con \* ad inizio riga
* ancora inizia con un solo \*
* ultima con asterisco

- con \- ad inizio riga
- ancora \- ad inizio riga
  - questa con 2 spazi prima del trattino
  - questa con 2 spazi prima del trattino

<br>

## Checklist
Si può inserire una checklist mediante un trattino, uno spazio e 2 parentesi quadre separate da uno spazio (non spuntata) o da una "x" (spuntata). <br>
- [ ] elemento non spuntato         \- \[ \]
- [x] elemento spuntato             \- \[x\]
- [x] altro elemento spuntato       \- \[x\]
- [ ] ultimo elemento non spuntato  \- \[ \]

<br>

## Codice Sorgente
per inserire del codice sorgente ed utilizzare la formattazione tipica del linguaggio, si fa esattamente come per la docstring in Python, ma al posto dell'apice o dei doppi apici, si utilizza l'accento grave  \`. Se dopo i primi 3 \` inseriamo il nome di un linguaggio, verranno contestualizzati i colori per evidenziare la sintessi del linguaggio indicato. <br>
Nell'esempio sotto, se si sostituiscono gli apici ad inizio e fine codice con altrettanti accenti gravi, si ottinene il box sottostante:<br>
'''python <br>
import pandas as pd <br>
'''
```python
import pandas as pd
```
Linguaggi disponibili: actionscript3, apache, applescript, asp, brainfuck, c, cfm, clojure, cmake, coffee-script, C++, cs, csharp, css, csv, bash, diff, elixir, erb - HTML + Embedded Ruby, go, haml, http, java, javascript, json, jsx, less, lolcode, make - Makefile, markdown, matlab, nginx, objectivec, pascal, PHP, Perl, python, profile - python profiler output, rust, salt, Shell scripting (BASH, ZSH, ASH...), sql, scss, sql, svg, swift, rb, jruby, ruby - Ruby, smalltalk, vim, viml - Vim Script, volt, vhdl, vue, xml, yaml

Per inserire del codice "in line" si utilizza un singolo accento grave. In questa frase la parola `ALT` è inserita fra singoli accenti gravi.

<br>

## Immagini
Per inserire una immagine, basta anteporre all'URL fra parentesi \!\[logo\] . Per esempio per il logo di Python:

\!\[Logo\]https://www.python.org/static/community_logos/python-logo-master-v3-TM.png

![logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

<br>

## Citazioni
Per le citazioni si utilizza il simbolo di maggiore \> ad inizio riga
>Tanto va la gatta al lardo che ci lascia <br>
>lo zampino

<br>

## Emoji :smile:
E' anche possibile inserire le emoji. devono essere scritte fra due duepunti: per esempio :test:. Se al posto di _test_ si utilizza _smile_, si ottienne :smile:, oppure _thumbsup_ per avere :thumbsup: <br>
Un elenco delle emoji è disponibile a questi link: <br>
https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md
https://www.webfx.com/tools/emoji-cheat-sheet/