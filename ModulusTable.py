import matplotlib.pyplot as plt
import math as math

def segments(n ,p):
    for i in range (1, p+1):
        angleActuel = (2*math.pi/p)*i #Starting angle
        coorX = math.cos(angleActuel)
        coorY = math.sin(angleActuel)

        angleCible = (2*math.pi/p)*i*n #Reaching Angle
        coorX2 = math.cos(angleCible)
        coorY2 = math.sin(angleCible)

        plt.plot((coorX, coorX2), (coorY, coorY2,), 'black') #Draw segment

#Ask for user input
table = input('Table: ')
modulus = input('Modulus: ')
name = input('Outputfile Name: ')

ax = plt.subplots(num=None, figsize=(8,8), dpi=96, facecolor='w', edgecolor='k') #Window definition, to have a 1:1 ratio, change the 'dpi' if you want a higher quality

plan = plt.gca()
plan.set_xlim((-1, 1)) #x limit
plan.set_ylim((-1, 1)) #y limit
plt.axis('off') #Remove apaprents axis

Cercle = plt.Circle((0, 0), 1, color='black', fill=False) #Create a circle
plan.add_artist(Cercle)

segments(int(table), int(modulus)) #Segments, real thing here

titre = "Table " + table + " modulus " + modulus
plt.text(-1, 1, titre) #Print the title, remove this if you want

plt.savefig(name + '.png')
plt.cla() #Remove the canvas
plt.close() #Close figure for better RAM usage, this is optional, I'll let this option if you want to create a loop to draw a lot of shapes
