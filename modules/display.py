def result_display(results: tuple):
    profit_total = results[0][0]
    actions_selection = results[0][1]
    execution_time = results[1]
    memory_used = results[2]
    cpu_percent = results[3]

    print("\nListe d'actions: \n")
    index = 1
    for action in actions_selection:
        name, price, profit = action
        print(f"{index}\tNom : {name}  \tPrix : {price}  \tProfit : {profit} ")
        index += 1
    total_cost = round(sum([action[1] for action in actions_selection]), 2)
    print(
        f"\nProfit total : {round(profit_total, 2)} \tCout Total : {total_cost}\n"
    )
    print(f"Temps d'execution : {execution_time} ms.")
    print(f"Utilisation mémoire : {memory_used} bytes.")
    print(f"Utilisation CPU : {cpu_percent} %.\n")
