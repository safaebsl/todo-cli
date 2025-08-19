def ajouter_tache(tache):
    with open("todo.txt", "a") as f:
        f.write(tache + "\n")
    print(f"Tâche ajoutée : {tache}")
def lister_taches():
    try:
        with open("todo.txt", "r") as f:
            taches = f.readlines()
        if not taches:
            print("Aucune tâche pour l’instant ✅")
        else:
            for i, tache in enumerate(taches, 1):
                print(f"{i}. {tache.strip()}")
    except FileNotFoundError:
        print("Pas encore de tâches.")
def marquer_tache_faite(num):
    with open("todo.txt", "r") as f:
        taches = f.readlines()
    if 0 < num <= len(taches):
        taches[num-1] = "[X] " + taches[num-1]
        with open("todo.txt", "w") as f:
            f.writelines(taches)
        print(f"Tâche {num} marquée comme faite ✅")
    else:
        print("Numéro de tâche invalide.")
