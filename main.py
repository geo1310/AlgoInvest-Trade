from itertools import combinations


def recursive_brute_force(amount: int, actions_list: list, actions_selection: list = None):
    """
    Algorithme de force brute avec récursivité : Calcule toutes les possibilités
    Complexité : O(2^n)
    """
    actions_selection = actions_selection if actions_selection else []

    if not actions_list:
        return sum([i[2] for i in actions_selection]), actions_selection

    # ne selectionne pas l'action
    profit_total_1, lst_profit_total_1 = recursive_brute_force(amount, actions_list[1:], actions_selection)
    # selectionne l'action
    action_current = actions_list[0]
    # verifie si le portefeuille restant permet d'acheter l'action
    if action_current[1] <= amount:
        profit_total_2, lst_profit_total_2 = recursive_brute_force(
            amount - action_current[1],
            actions_list[1:],
            actions_selection + [action_current]
            )
        if profit_total_1 < profit_total_2:
            return profit_total_2, lst_profit_total_2
    return profit_total_1, lst_profit_total_1


def itertools_brute_force(amount: int, actions_list: list):
    """
    Algorithme de force brute avec itertools.combinations : Calcule toutes les possibilités
    Complexité : O(2^n)
    """
    actions_selection_final = []
    profit_total_final = 0

    for taille_combinaison in range(1, len(actions_list) + 1):
        combinaisons = list(combinations(actions_list, taille_combinaison))
        for comb in combinaisons:
            profit_total = sum([i[2] for i in comb])
            cout_total = sum([i[1] for i in comb])
            if profit_total > profit_total_final and cout_total <= amount:
                actions_selection_final = comb
                profit_total_final = profit_total

    return profit_total_final, actions_selection_final


# variables
actions_list = [

    ('Action-1', 20, 1),
    ('Action-2', 30, 3),
    ('Action-3', 50, 7.5),
    ('Action-4', 70, 14),
    ('Action-5', 60, 10.2),
    ('Action-6', 80, 20),
    ('Action-7', 22, 1.54),
    ('Action-8', 26, 2.86),
    ('Action-9', 48, 6.24),
    ('Action-10', 34, 9.18),
    ('Action-11', 42, 7.14),
    ('Action-12', 110, 9.9),
    ('Action-13', 38, 8.74),
    ('Action-14', 14, 0.14),
    ('Action-15', 18, 0.54),
    ('Action-16', 8, 0.64),
    ('Action-17', 4, 0.48),
    ('Action-18', 10, 1.4),
    ('Action-19', 24, 5.04),
    ('Action-20', 114, 20.52)
]

amount = 500

# méthode récursive
profit_total, actions_selection = recursive_brute_force(amount, actions_list)

print("\nListe d'actions: \n")
for action in actions_selection:
    name, price, profit = action
    print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
print(f"\nProfit total : {profit_total} \tCout Total : {sum([i[1] for i in actions_selection])}\n")

# méthode itertools.combinations
profit_total, actions_selection = itertools_brute_force(amount, actions_list)

print("\nListe d'actions: \n")
for action in actions_selection:
    name, price, profit = action
    print(f"Nom : {name}  \tPrix : {price}  \tProfit : {profit} ")
print(f"\nProfit total : {profit_total} \tCout Total : {sum([i[1] for i in actions_selection])}\n")
