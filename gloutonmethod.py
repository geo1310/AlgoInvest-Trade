import pandas as pd

# variables
amount = 500
datas_actions_file = './data/dataset1_Python+P7.csv'

# extraction des données du fichier csv
# utilisation de pandas
dataframe = pd.read_csv(datas_actions_file)

# Convertir le DataFrame en liste
data_list = dataframe.to_numpy().tolist()


class Action:
    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit
        self.rapport = round((profit / price), 2)

    def __lt__(self, other):
        return self.rapport < other.rapport


def glouton_method(amount: float, actions_list: list):
    tableau_trie = []
    for action in actions_list:
        if action[1] > 0:
            tableau_trie.append(Action(*action))

    # Trier les actions par leur rapport
    tableau_trie.sort(reverse=True)
    for action in tableau_trie:
        print(f"{action.name} - {action.rapport}")

    profit_total = 0
    actions_selection = []

    for action in tableau_trie:
        action_price = action.price
        action_profit = action.profit
        if amount - action_price >= 0:
            amount -= action_price
            profit_total += action_profit
            actions_selection.append(action)

    return profit_total, actions_selection


def result_display(profit_total: float, actions_selection: list):
    cout_total = 0
    print("\nListe d'actions: \n")
    for action in actions_selection:
        name = action.name
        price = action.price
        cout_total += price
        profit = action.profit
        print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
    print(f"\nProfit total : {round(profit_total, 2)} \tCout Total : {round(cout_total, 2)}\n")


# méthode itertools.combinations
result_display(*glouton_method(amount, data_list))
