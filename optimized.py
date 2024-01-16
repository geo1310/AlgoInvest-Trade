"""
Programmation Dynamique :
Une matrice est crée, comprenant d'une part toutes les valeurs possibles du portefeuille de 0 au max
et d'autre part une ligne pour chaque action de la liste en commencant par 0 action.
Le but étant de construire la solution petit à petit pour chaque valeur de Portefeuille et en maximisant
les valeurs d'actions pouvant y etre insérée par rapport à la ligne precedente.
Avec cette méthode on uitlise les calculs deja effectués des lignes precedentes augmentant ainsi les performances.
La derniere case de la matrice representant la solution optimale.

Dans ce script on peut régler deux variables

* `amount` : la valeur du portefeuille
* `datas_actions_file` : le fichier csv contenant la liste des actions à analysées
( les fichiers csv doivent etre placés dans le dossier data du projet)

Ce script execute la fonction :

1. `dynamic_method(amount: float, actions_list: list, type: int)`

La fonction est lancée deux fois avec un type different :

1. Type 1 : on garde la précision des prix d'actions ( 2 décimales )
    amount et toutes les valeurs sont multipliées par 100 afin d'assurer le bon fonctionnement
    de la matrice et de l'indexage ( nombres entiers).

2. Type 2 : on garde l'amount et on arrondi les prix d'actions au nombre entier le plus proche.

Aprés lancement du script la console affiche le résultat pour les deux types de calculs, le temps d'execution
ainsi que la charge mémoire et la charge CPU.

"""


import psutil

import timeit

import pandas as pd


# default values
amount = 500
datas_actions_file = "./data/dataset2_Python+P7.csv"

# extraction des données du fichier csv
dataframe = pd.read_csv(datas_actions_file)

# Converti le DataFrame en liste
data_list = dataframe.to_numpy().tolist()

# convertit le pourcentage en profit reel et supprime les actions avec un prix <= 0
data_list = [[action[0], action[1], round((action[2]*action[1]/100), 2)] for action in data_list if action[1] > 0]


def dynamic_method(
    amount: float,
    actions_list: list,
    type: int,
) -> tuple:
    """
    Algorithme de programmation dynamique : Création d'une matrice amount * nombre d'actions
    Complexité : O(n*capacite)
    """

    # type de precision pour le prix de l'action , 1-> avec 2 décimales, 2-> en arrondissant au premier entier
    if type == 1:
        # on verifie que le prix de l action est superieur a 0 et on multiplie par 100
        actions_list = [
            [action[0], round(action[1] * 100), action[2]]
            for action in actions_list
        ]

        # on multiplie la capacite par 100 pour adapter la taille de la matrice
        amount *= 100

        # valeur du diviseur pour recupérer la valeur reelle du prix des actions
        div_values = 100

    elif type == 2:
        # on verifie que le prix de l action est superieur a zero et on l arrondi a l entier le plus proche
        actions_list = [
            [action[0], round(action[1]), action[2]]
            for action in actions_list
        ]

        # valeur du diviseur pour recupérer la valeur reelle du prix des actions
        div_values = 1

    # creation de la matrice remplie de 0
    matrice = [[0 for _ in range(0, amount + 1)] for _ in range(len(actions_list) + 1)]

    # boucle sur chaque action de la liste
    for actions_index, current_action in enumerate(actions_list, start=1):
        # boucle sur chaque capacite possible
        for amount_range in range(1, amount + 1):
            # verifie si le cout de l'action actuelle est inferieur ou egal a la capacite en cours
            if actions_list[actions_index - 1][1] <= amount_range:
                # si oui choisi la meilleure option possible entre inclure ou exclure l action actuelle
                matrice[actions_index][amount_range] = max(
                    actions_list[actions_index - 1][2]
                    + matrice[actions_index - 1][
                        amount_range - actions_list[actions_index - 1][1]
                    ],
                    matrice[actions_index - 1][amount_range],
                )
            else:
                # si non affecte la case actuelle de la matrice avec la valeur de capacite precedente
                matrice[actions_index][amount_range] = matrice[actions_index - 1][
                    amount_range
                ]

    # recuperation des actions selectionnees en parcourant la matrice à l'envers

    # default values
    amount_selection = amount
    nb_actions = len(actions_list)
    actions_list_selection = []

    # boucle tant que la capacite et le nb dactions est superieur ou egal a zero
    while amount_selection >= 0 and nb_actions >= 0:
        # selectionne l action actuelle
        current_action = actions_list[nb_actions - 1]

        # verifie si la position actuelle est egale à la somme de la position precedente + profit action actuelle
        if (
            matrice[nb_actions][amount_selection]
            == matrice[nb_actions - 1][amount_selection - current_action[1]]
            + current_action[2]
        ):
            # si oui on ajoute l action a la selection
            actions_list_selection.append(current_action)
            # reduit la capacite de la valeur actuelle
            amount_selection -= current_action[1]

        # decremente le nombre d actions disponibles
        nb_actions -= 1

    # on modifie la valeur du prix de l action par rapport au type de calcul choisi 1 ou 2
    actions_list_selection = [
        [action[0], action[1] / div_values, action[2]]
        for action in actions_list_selection
    ]

    # on retourne la derniere case de la matrice et la liste des actions selectionnees
    return matrice[-1][-1], actions_list_selection


# affichage des resultats
def result_display(results: tuple):
    """affichage des resultats"""

    # default  values
    profit_total = results[0][0]
    actions_selection = results[0][1]
    execution_time = results[1]
    memory_used = results[2]
    cpu_percent = results[3]

    print("\nListe d'actions: \n")
    index = 1

    # affiche la liste d'actions selectionnees
    for action in actions_selection:
        name, price, profit = action
        print(f"{index}\tNom : {name}  \tPrix : {price}  \tProfit : {profit} ")
        index += 1

    # calcul le cout total de la liste d'actions selectionnees
    total_cost = round(sum([action[1] for action in actions_selection]), 2)

    # affiche les resultats et les performances
    print(f"\nProfit total : {round(profit_total, 2)} \tCout Total : {total_cost}\n")
    print(f"Temps d'execution : {execution_time} ms.")
    print(f"Utilisation mémoire : {memory_used} bytes.")
    print(f"Utilisation CPU : {cpu_percent} %.\n")


def execution_time(function):
    """calcul du temps d execution et les ressources mémoire et CPU d'une fonction"""

    start_memory = psutil.Process().memory_info().rss
    temps_debut = timeit.default_timer()

    resultat = function()

    temps_fin = timeit.default_timer()
    end_memory = psutil.Process().memory_info().rss
    memory_used = end_memory - start_memory

    # durée d execution en millisecondes
    time_execution = round(((temps_fin - temps_debut) * 1000), 2)

    # Mesurer l'utilisation du CPU
    cpu_percent = psutil.cpu_percent(
        interval=1
    )  # Utilisation CPU au cours de la dernière seconde

    return resultat, time_execution, memory_used, cpu_percent


def main():
    """execution de la méthode dynamique avec deux types de précisions"""

    # type 1 avec 2 decimales
    print("\nMéthode Dynamique Type 1 : Prix de l'action avec deux décimales")
    print(64 * "-")
    result_display(execution_time(lambda: dynamic_method(amount, data_list, 1)))

    # type 2 en arrondissant
    print(
        "\nMéthode Dynamique Type 2 : Prix de l'action Arrondi à l'entier le plus proche"
    )
    print(77 * "-")
    result_display(execution_time(lambda: dynamic_method(amount, data_list, 2)))


if __name__ == "__main__":
    main()
