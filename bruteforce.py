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


# variables
amount = 500
datas_actions_file = "./data/dataset0_Python+P7.csv"

# extraction des données du fichier csv
# utilisation de pandas
dataframe = pd.read_csv(datas_actions_file)

# Convertir le DataFrame en liste
data_list = dataframe.to_numpy().tolist()
data_list = [action for action in data_list if action[1] > 0]


def itertools_brute_force(
    amount: float,
    actions_list: list,
) -> tuple:
    """
    Algorithme de force brute avec itertools.combinations : Calcule toutes les possibilités
    Complexité : O(2^n)
    """

    # default valies
    actions_selection_final = []
    profit_total_final = 0

    # double boucle for
    for taille_combinaison in range(1, len(actions_list) + 1):
        for comb in combinations(actions_list, taille_combinaison):
            try:
                # blabla
                profit_total = sum([float(action[2]) for action in comb])
                cout_total = sum([float(action[1]) for action in comb])

                # blabla
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

    # action select
    actions_selection = actions_selection if actions_selection else []
    if not actions_list:
        return sum([float(i[2]) for i in actions_selection]), actions_selection

    # ne selectionne pas l'action
    profit_total_1, lst_profit_total_1 = recursive_brute_force(
        amount, actions_list[1:], actions_selection
    )

    # selectionne l'action
    action_current = actions_list[0]

    # verifie si le portefeuille restant permet d'acheter l'action
    if float(action_current[1]) <= amount:
        profit_total_2, lst_profit_total_2 = recursive_brute_force(
            amount - float(action_current[1]),
            actions_list[1:],
            actions_selection + [action_current],
        )
        if profit_total_1 < profit_total_2:
            return profit_total_2, lst_profit_total_2

    # 99% du temps on SAUTE UNE LIGEN ANANT LE RETURN
    return profit_total_1, lst_profit_total_1


# affichage des resultats
def result_display(results: tuple):
    """ """

    # default  values
    profit_total = results[0][0]
    actions_selection = results[0][1]
    execution_time = results[1]
    memory_used = results[2]
    cpu_percent = results[3]

    print("\nListe d'actions: \n")
    index = 1

    # d,zedzzdez
    for action in actions_selection:
        name, price, profit = action
        print(f"{index}\tNom : {name}  \tPrix : {price}  \tProfit : {profit} ")
        index += 1

    # zeddzdz
    total_cost = round(sum([action[1] for action in actions_selection]), 2)

    # zedzzdezdez
    print(f"\nProfit total : {round(profit_total, 2)} \tCout Total : {total_cost}\n")
    print(f"Temps d'execution : {execution_time} ms.")
    print(f"Utilisation mémoire : {memory_used} bytes.")
    print(f"Utilisation CPU : {cpu_percent} %.\n")


def execution_time(function):
    """# calcul du temps d execution et les ressources mémoire et CPU d'une fonction"""

    # Mesurer la mémoire avant l'exécution
    start_memory = psutil.Process().memory_info().rss

    temps_debut = timeit.default_timer()
    resultat = function()
    temps_fin = timeit.default_timer()

    # Mesurer la mémoire après l'exécution
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
    """ """

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
