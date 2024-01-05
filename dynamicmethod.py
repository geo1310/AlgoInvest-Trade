import pandas as pd
import timeit

# variables
amount = 500
datas_actions_file = "./data/dataset1_Python+P7.csv"

# extraction des données du fichier csv
dataframe = pd.read_csv(datas_actions_file)

# Converti le DataFrame en liste
data_list = dataframe.to_numpy().tolist()
# suppression des actions <= 0
data_list = [action for action in data_list if action[1] > 0]


# calcul du temps d execution d'une fonction
def execution_time(function):
    temps_debut = timeit.default_timer()
    resultat = function()
    temps_fin = timeit.default_timer()
    # durée d execution en millisecondes
    time_execution = round(((temps_fin - temps_debut) * 1000), 6)

    return resultat, time_execution


def dynamic_method(amount: float, actions_list: list):
    """
    Algorithme de programmation dynamique : Création d'une matrice amount * nombre d'actions
    Complexité : O(n*capacite)
    """
    # creation de la matrice
    matrice = [[0 for _ in range(0, amount + 1)] for _ in range(len(actions_list) + 1)]
    # remplissage de la matrice
    for actions_index, current_action in enumerate(actions_list, start=1):
        for amount_range in range(1, amount + 1):
            if actions_list[actions_index - 1][1] <= amount_range:
                matrice[actions_index][amount_range] = max(
                    actions_list[actions_index - 1][2]
                    + matrice[actions_index - 1][
                        amount_range - int(actions_list[actions_index - 1][1])
                    ],
                    matrice[actions_index - 1][amount_range],
                )
            else:
                matrice[actions_index][amount_range] = matrice[actions_index - 1][
                    amount_range
                ]

    # recuperation des actions selectionnees en parcourant la matrice à l'envers
    amount_selection = amount
    nb_actions = len(actions_list)
    actions_list_selection = []

    while amount_selection >= 0 and nb_actions >= 0:
        current_action = actions_list[nb_actions - 1]
        if (
            matrice[nb_actions][amount_selection]
            == matrice[nb_actions - 1][amount_selection - int(current_action[1])]
            + current_action[2]
        ):
            actions_list_selection.append(current_action)
            amount_selection -= int(current_action[1])

        nb_actions -= 1

    return matrice[-1][-1], actions_list_selection


# affichage des resultats
def result_display(results: tuple):
    profit_total = results[0][0]
    actions_selection = results[0][1]
    execution_time = results[1]

    print("\nListe d'actions: \n")
    for action in actions_selection:
        name, price, profit = action
        print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
    print(
        f"\nProfit total : {round(profit_total, 2)} \tCout Total : {sum([float(i[1]) for i in actions_selection])}\n"
    )
    print(f"\nTemps d'execution : {execution_time} ms.\n")


# méthode dynamique
result_display(execution_time(lambda: dynamic_method(amount, data_list)))
