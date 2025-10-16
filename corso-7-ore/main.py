# Sono un commento

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
# x = true      NON va bene
print(type(x))