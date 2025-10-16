# #--------------------------------------------------------
# Introduzione

# Metodo per mandare a schermo un messaggio

# messaggio = input("Inserisci un messaggio: ")
# print(messaggio)

if 1 < 5:
    print("fatto if")
    print("sono una seconda indentazione")

x = 6
y = 5

# Non posso dichiarare a priopri una var senza assegnarle contenuto
# z

# Non posso scrivere formati di variabile così
# 2pesopersona
# peso-persona
# peso persona

# Standard dichiarazione var:
peso_persona_amichevole = 45
# Si usa l'underscore piuttosto che il camelCase, ma nulla lo vieta a prescindere

#Multidichiarazione
x, y, z = 32, 45, 100

print(x)
print(y)

# Qua hanno tutte lo stesso valore, si assegna così
a = b = c = 99
print(a, b, c)

# lista
città = ["Roma", "Genova", "Tirana"]
# A ogni var assegna un valore della lista
x, y, z = città
# Notare che x, y, z cambiano di tipo da int a stringhe
print(x, y, z)

x = 8
y = 10
z = x + y
print(z)
# Figata:
z = x + y + x + y
print(z)
print(type(z))

# Il tipo cambia alla riassegnazione di un valore,
# un float diventa stringa, flessibile ma 👀...
f = 5.5
print(type(f))
f = "belandi"
print(type(f))

# Il tipo boolean si scrive in Maiuscolo
x = True      # Va bene
x = False
is_true = True
# x = true      NON va bene
print(type(x))

#--------------------------------------------------------
# Tipi di dati "listosi":
#list
x = ["Roma", "Genova", "Tirana"]
print(type(x))
#tuple
x = ("Roma", "Genova", "Tirana")
print(type(x))
#range
x =  range(6) # Genera varori da 0 a 5 al runtime, anziché scrivere [0, 1, 2, 3, 4, 5]
print(type(x))
#  dict
x = {"nome": "Alessandro", "eta": 29}
print(type(x))
#set
x = {"Roma", "Genova", "Tirana"}
print(type(x))

# Casting
x = "5"
y = 5

# NON funziona come Javascript che si possono sommare stringa e numero
# print (x + y) Da errore!!!
# print (y + x) Anche qua!!

# Per far funzionare faccio
# In un caso:
y = str(5) # castato a stringa
print(x + y) # concatena ed esece 55

y = 5
x = int(x) # qui casta la stringa in int
print(x + y) # ed esce 10

x = float(x)
print(x) # diventa 5.0
print(type(x)) # e ovviamente tipo float

#--------------------------------------------------------
# Stringhe

# Sono entrambe stringhe valide:
x = 'ciao'
y = "ciao"

# per fare stringhe multilinea:
# Con """  """ ne esce un bell'haiku multilinea o... Ungaretti 
x = """oh belandi
che bella 
giornata
raga"""

# Le stringhe vengono sempre tratatte come array:
print(x[0]) # stampa 'o'
# ovviamente anche lo spazio è un carattere della stringa....

print(len(x)) #stampa la lunghezza, ben 35 caratteri...

# ciclare sulle stringhe
for carattere in "dibris":
    print(carattere)

# prendere parti di stringa:
x = "ciao sonoun biscotto"
print(x[:3]) # stampa "cia" con estremo di arrivo non incluso [0, 3)
print(x[4:9]) # stampa " sono", [4, 9)
print(x[-4]) # stampa il quarto carattere partendo dal fondo, quindi 'o'
print(x[-4:]) # stampa "otto", da -4 a -0

# modificare una stringa
print(x.upper())
print(x.lower())
print(x.replace("o", "p")) # si spiega da solo..
x = " hey "
print(x.strip()) # toglie gli spazi davanti e in fondo se ce ne sono

# da errore, va castato il 9
# prova = "Ciao sono Ale e sono nato il " + 9 + " giugno"
prova = "Ciao sono Ale e sono nato il {} giugno"
print(prova.format(9)) # inserisce il 9 al posto di {}
prova = "Ciao sono Ale e sono nato il {} giugno, peso {}kg e sono alto {}cm"
print(prova.format(9, 90, 190))
prova = "Ciao sono Ale e sono nato il {2} giugno, peso {0}kg e sono alto {1}cm" # qui assegno indici
print(prova.format(90, 190, 9)) # e inserisco i valori in ordine di indice
prova = "ciao sono \"figo\"" # escape
prova = 'porca l\'oca' #escape