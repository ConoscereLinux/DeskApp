# DeskApp
Utility per gestire, rinominare e indicizzare file

# Installazione

Ecco la procedura per preparare l'ambiente di sviluppo.

Intanto dobbiamo installare miniconda:
https://conda.io/projects/conda/en/stable/user-guide/install/download.html

Questo è il link alla pagina iniziale di MiniConda
https://docs.conda.io/en/latest/miniconda.html


# VirtualEnv
Per creare una VirtualEnv su Linux con MiniConda da riga di comando:
conda create --name DeskApp python=3.10

Poi per attivare/disattivare la VirtualEnv utilizzare i comandi:
conda activate DeskApp
conda deactivate

Nella VirtualEnv installiamo Pyside con il comando:
pip install PySide6

per creare la documentazione:
pip freeze > requirement.txt

per creare un ambiente di sviluppo standard, cioè come memorizzato nel file di documentazione:

pip install -r requirements.txt
