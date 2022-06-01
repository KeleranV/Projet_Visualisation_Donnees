#Parser pour le projet, permet de donner un semblant d'uniformité aux noms des jeux

import pandas as pd

steam = pd.read_csv('steam.csv')
vgsales = pd.read_csv('vgsales.csv')

#lettres de l'alphabet, minuscules et majuscules
#permettra de faire des tests pour retirer les caractères
dictionary = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_/'

#récupération des noms des jeux
namesSteam = steam.loc[:, "name"]
nameVG = vgsales.loc[:, "Name"]

#print(namesSteam[:5])
print(namesSteam[0])
print(type(namesSteam[0]))

#tri des caractères, si non dans de dico, on le retire, puis on mets le nom en minuscules, pour être sûr
for i in range(len(namesSteam)):
    for char in namesSteam[i]:
        if char not in dictionary: namesSteam[i] = namesSteam[i].replace(char, "")
    namesSteam[i] = namesSteam[i].lower()
print(namesSteam[0])