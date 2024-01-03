from itertools import combinations
import pandas as pd


# variables
amount = 500
datas_actions_file = './data/dataset0_Python+P7.csv'

# extraction des données du fichier csv
# utilisation de pandas
dataframe = pd.read_csv(datas_actions_file)

# Convertir le DataFrame en liste
data_list = dataframe.to_numpy().tolist()


def recursive_brute_force(amount: float, actions_list: list, actions_selection: list = None):
    """
    Algorithme de force brute avec récursivité : Calcule toutes les possibilités
    Complexité : O(2^n)
    """
    actions_selection = actions_selection if actions_selection else []

    if not actions_list:
        return sum([float(i[2]) for i in actions_selection]), actions_selection

    # ne selectionne pas l'action
    profit_total_1, lst_profit_total_1 = recursive_brute_force(amount, actions_list[1:], actions_selection)
    # selectionne l'action
    action_current = actions_list[0]
    # verifie si le portefeuille restant permet d'acheter l'action
    if float(action_current[1]) <= amount:
        profit_total_2, lst_profit_total_2 = recursive_brute_force(
            amount - float(action_current[1]),
            actions_list[1:],
            actions_selection + [action_current]
            )
        if profit_total_1 < profit_total_2:
            return profit_total_2, lst_profit_total_2
    return profit_total_1, lst_profit_total_1


def itertools_brute_force(amount: float, actions_list: list):
    """
    Algorithme de force brute avec itertools.combinations : Calcule toutes les possibilités
    Complexité : O(2^n)
    """
    actions_selection_final = []
    profit_total_final = 0

    for taille_combinaison in range(1, len(actions_list) + 1):
        for comb in combinations(actions_list, taille_combinaison):
            profit_total = sum([float(i[2]) for i in comb])
            cout_total = sum([float(i[1]) for i in comb])
            if profit_total > profit_total_final and cout_total <= amount:
                actions_selection_final = comb
                profit_total_final = profit_total

    return profit_total_final, actions_selection_final


def result_display(profit_total: float, actions_selection: list):
    print("\nListe d'actions: \n")
    for action in actions_selection:
        name, price, profit = action
        print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
    print(f"\nProfit total : {round(profit_total, 2)} \tCout Total : {sum([float(i[1]) for i in actions_selection])}\n")


# méthode récursive
#result_display(*recursive_brute_force(amount, data_list))

# méthode itertools.combinations
result_display(*itertools_brute_force(amount, data_list))
