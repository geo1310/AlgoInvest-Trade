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
data_list = [action for action in data_list if action[1] > 0]


def itertools_brute_force(amount: float, actions_list: list):
    """
    Algorithme de force brute avec itertools.combinations : Calcule toutes les possibilités
    Complexité : O(2^n)
    """
    actions_selection_final = []
    profit_total_final = 0

    for taille_combinaison in range(1, len(actions_list) + 1):
        for comb in combinations(actions_list, taille_combinaison):
            try:
                profit_total = sum([float(action[2]) for action in comb])
                cout_total = sum([float(action[1]) for action in comb])
                if profit_total > profit_total_final and cout_total <= amount:
                    actions_selection_final = comb
                    profit_total_final = profit_total
            except Exception as error:
                print(error)

    return profit_total_final, actions_selection_final


def result_display(profit_total: float, actions_selection: list):
    print("\nListe d'actions: \n")
    for action in actions_selection:
        name, price, profit = action
        print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
    print(f"\nProfit total : {round(profit_total, 2)} \tCout Total : {sum([float(i[1]) for i in actions_selection])}\n")


# méthode itertools.combinations
result_display(*itertools_brute_force(amount, data_list))
