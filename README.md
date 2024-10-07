# Python-Classroom

Como Crear un Branch (Solo un vez): 

    Escribe en una terminal de Git Bash:

    git clone https://github.com/StevenMZH/Python-Classroom.git
    git checkout -b "Nombre de la Rama"

Como hacer un Commit (Mandar los cambios a Github):

    Escribe en una terminal de Git Bash:

    git add .
    git commit -m "Descripción de los cambios"
    git push origin "Nombre de la Rama"

Como actualizar la Carpeta Clases de tus archivos al que esta en Github: 

    Escribe en una terminal de Git Bash:

    git fetch origin main
    git checkout origin/main -- Clases/
