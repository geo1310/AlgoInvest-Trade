from itertools import combinations

# Votre liste
ma_liste = [1, 2, 3, 4, 5]

# Générer toutes les combinaisons possibles
combinaisons = []
for taille_combinaison in range(1, len(ma_liste) + 1):
    combinaisons.extend(combinations(ma_liste, taille_combinaison))

# Afficher les combinaisons
for comb in combinaisons:
    print(comb)
