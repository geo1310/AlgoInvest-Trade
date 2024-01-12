import timeit
import psutil


# calcul du temps d execution et les ressources mémoire et CPU d'une fonction
def execution_time(function):
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
    cpu_percent = psutil.cpu_percent(interval=1)  # Utilisation CPU au cours de la dernière seconde

    return resultat, time_execution, memory_used, cpu_percent
