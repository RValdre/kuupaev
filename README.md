# Kasutusjuhend:

1.Variant: Alla laadida Kuupaev.exe fail ning selle käivitamisel avaneb command line, kus küsitakse aastat. Kui sisestatakse aasta normaalsel kujul (2023 etc.) siis tagastab programm tagasi sobilikud kuupäevad ning loob samase kohta CSV faili palgamaksepäevade ja raamatupidaja meeldetuletus kuupäevadega.

2.Variant Samuti alla laadida .py fail ning alla laadida vajalikud moodulid (python, pip, workalendar) see järel käivitada käsuviip õiges kataloogis ning sisestada käsuviibale "python Kuupaev.py". See käivitab pythoni scripti ja küsib nagu eelnevalt mainitud kasutajalt aasta. Teine viis on käsule koheselt aasta väärtuse sisestamine "python Kuupaev.py --year 2023". käivitub script kohe ilma, et küsiks kasutajalt uuesti aastat.
