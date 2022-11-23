# DeskApp

**DeskApp** è una utility per gestire, rinominare e indicizzare file.

# Ambiente di sviluppo

Per poter lavorare al progetto, occorre preparare un ambiente di sviuluppo, e per farlo utilizzeremo una *virtualenv* usando Miniconda.

## Miniconda

Per installare miniconda, seguire la guida di riferimento:
[Installation - conda 22.9.0 documentation](https://conda.io/projects/conda/en/stable/user-guide/install/index.html)

Qui, invece, la pagina per il download deigli installer:
[Miniconda - conda documentation](https://docs.conda.io/en/latest/miniconda.html)

Per creare la *virtualenv* con Miniconda, da riga di comando:

```bash
conda create --name DeskApp python=3.10
```

Poi per attivare la *virtualenv* utilizzare il comando:

```bash
conda activate DeskApp
```

> In seguito per disattivare la *virtualenv* digitare:
> 
> ```bash
> conda deactivate
> ```

## Requisiti

Per installare tutte le librerie di Python richieste useremo direttamente *pip*. Entare nella cartella ```src``` e digitare il seguente comando:

```bash
pip install -r requirements.txt
```

> Il file ```requirements.txt``` può essere creato, dopo aver installato manualmente i pacchetti necessari, usando il seguente comando dall'interno della cartella ```src```:
> 
> ```bash
> pip freeze > requirements.txt
> ```
