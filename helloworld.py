import random




##2 personnnes de donnne rendezed vous entre 12 et 13 sans préciser la minute

somme = 0
numberSimulation = int(input("Merci de donner le nombre de simulation  :"))
for i in range(1, numberSimulation):
    arrive1 = random.randint(0, 59)
    arrive2 = random.randint(0, 59)
    attente = abs(arrive1 - arrive2)
    somme = somme + attente

moyenne = somme / numberSimulation
print("Estimation de la moyenne est  {}".format(moyenne))


print("start methode de jugement")
## Methode du jugement majoritaire
nbElecteur = 8
nbCandidats = 3
nbMention = 7
vote=[[0]*nbCandidats]*nbElecteur
resultat=[[0]*nbMention]*nbElecteur
for e in range (1,nbElecteur):
    for c in range (1,nbCandidats):
        vote[e][c] = random.randint(1, nbMention)

for c in range (1,nbCandidats):
    for m in range (1,nbMention) :
        resultat[c][m]=0
    for e in range (1, nbCandidats):
        m=vote[e][c]
        resultat[c][m]+=1

print(" Vainqueur = {}".format(resultat))


















