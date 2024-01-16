"""
Alogorithme de Force Brute :
Toutes les combinaisons d'actions sont calculées afin de faire ressortir la meilleure.

Dans ce script on peut régler deux variables

* `amount` : la valeur du portefeuille
* `datas_actions_file` : le fichier csv contenant la liste des actions à analysées
( les fichiers csv doivent etre placés dans le dossier data du projet)

Ce script execute deux fonctions :

1. `itertools_brute_force(amount: float, actions_list: list)`

    Calcule toutes les combinaisons possibles en utilisant la fonction `combinations` du module `itertools`,
    qui génère toutes les combinaisons possibles d'une séquence avec une longueur donnée.

2. `recursive_brute_force(amount: float, actions_list: list, actions_selection: list = None)`

    Calcule toutes les combinaisons possibles en utilisant la récursivité

Aprés lancement du script la console affiche le résultat pour les deux fonctions, le temps d'execution
de chaque fonction ainsi que l'utilisation de la memoire et la charge CPU.

"""


from itertools import combinations

import timeit
import psutil

import pandas as pd


# default values
amount = 500
datas_actions_file = "./data/dataset0_Python+P7.csv"


def csv_to_list(file_path):
    """
    extraction des données du fichier csv, conversion en liste
    transforme le benefice (%) de chaque action en profit reel
    """

    # creation d u dataframe avec pandas
    dataframe = pd.read_csv(file_path)

    # Converti le DataFrame en liste
    data_list = dataframe.values.tolist()

    # convertit le pourcentage en profit reel et supprime les actions avec un prix <= 0
    data_list = [
        [action[0], action[1], round((action[2]*action[1]/100), 2)]
        for action in data_list
        if action[1] > 0
    ]

    return data_list


def itertools_brute_force(
    amount: float,
    actions_list: list,
) -> tuple:
    """
    Algorithme de force brute avec itertools.combinations : Calcule toutes les possibilités
    Complexité : O(2^n)
    """

    # default values
    actions_selection_final = []
    profit_total_final = 0

    # double boucle for pour toutes les tailles de combinaisons et toutes les combinaisons
    for taille_combinaison in range(1, len(actions_list) + 1):
        for comb in combinations(actions_list, taille_combinaison):
            try:
                # enregiste le resultat de la combinaison actuelle
                profit_total = sum([action[2] for action in comb])
                cout_total = sum([action[1] for action in comb])

                # verifie si la combinaison actuelle est meilleure et si oui la mémorise
                if profit_total > profit_total_final and cout_total <= amount:
                    actions_selection_final = comb
                    profit_total_final = profit_total

            except Exception as error:
                print(error)

    return profit_total_final, actions_selection_final


def recursive_brute_force(
    amount: float,
    actions_list: list,
    actions_selection: list = None,
) -> tuple:
    """
    Algorithme de force brute avec récursivité : Calcule toutes les possibilités
    Complexité : O(2^n)
    """

    # initialise la leste des actions selectionnees
    actions_selection = actions_selection if actions_selection else []

    # verifie si la liste des actions est vide
    if not actions_list:
        # si oui renvoie la somme des profits et la liste des actions selectionnees
        return sum([i[2] for i in actions_selection]), actions_selection

    # appel recursif sans l action actuelle
    profit_total_1, lst_profit_total_1 = recursive_brute_force(
        amount, actions_list[1:], actions_selection
    )

    # selectionne l'action
    action_current = actions_list[0]

    # verifie si le portefeuille restant permet d'acheter l'action
    if action_current[1] <= amount:
        # appel recursif avec l action actuelle
        profit_total_2, lst_profit_total_2 = recursive_brute_force(
            amount - float(action_current[1]),
            actions_list[1:],
            actions_selection + [action_current],
        )  

        # compare les profits obtenus et retourne le meilleur
        if profit_total_1 < profit_total_2:
            return profit_total_2, lst_profit_total_2

    return profit_total_1, lst_profit_total_1


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
    """execution des méthodes force brute avec itertools.combinations et ensuite avec la récursivité"""

    data_list = csv_to_list(datas_actions_file)

    # méthode itertools.combinations
    print("\nUtilisation de itertools.combinations :")
    print("----------------------------------------")
    result_display(execution_time(lambda: itertools_brute_force(amount, data_list)))

    # méthode avec récursivité
    print("\nUtilisation de la récursivité :")
    print("-------------------------------")
    result_display(execution_time(lambda: recursive_brute_force(amount, data_list)))


if __name__ == "__main__":
    main()
