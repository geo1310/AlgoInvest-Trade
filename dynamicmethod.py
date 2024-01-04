import pandas as pd

# variables
amount = 500
datas_actions_file = './data/dataset0_Python+P7.csv'

# extraction des données du fichier csv
dataframe = pd.read_csv(datas_actions_file)

# Converti le DataFrame en liste
data_list = dataframe.to_numpy().tolist()
data_list = [action for action in data_list if action[1] > 0]


def dynamic_method(amount: float, actions_list: list):
    """
    Algorithme de programmation dynamique : Création d'une matrice amount * nombre d'actions
    Complexité : O(n*capacite)
    """
    # creation de la matrice
    matrice = [[0 for _ in range(0, amount + 1)] for _ in range(len(actions_list) + 1)]
    # remplissage de la matrice
    for i in range(1, len(actions_list) + 1):
        for w in range(1, amount + 1):
            if actions_list[i-1][1] <= w:
                matrice[i][w] = max(actions_list[i-1][2] + matrice[i-1][w-int(actions_list[i-1][1])], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # recuperation des actions selectionnes en parcourant la matrice à l'envers
    amount_selection = amount
    nb_actions = len(actions_list)
    actions_list_selection = []

    while amount_selection >= 0 and nb_actions >= 0:
        current_action = actions_list[nb_actions - 1]
        if matrice[nb_actions][amount_selection] == matrice[nb_actions-1][amount_selection-int(current_action[1])] + current_action[2]:
            actions_list_selection.append(current_action)
            amount_selection -= int(current_action[1])

        nb_actions -= 1

    return matrice[-1][-1], actions_list_selection


def result_display(profit_total: float, actions_selection: list):
    print("\nListe d'actions: \n")
    for action in actions_selection:
        name, price, profit = action
        print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
    print(f"\nProfit total : {round(profit_total, 2)} \tCout Total : {sum([float(i[1]) for i in actions_selection])}\n")


# méthode dynamique
result_display(*dynamic_method(amount, data_list))
