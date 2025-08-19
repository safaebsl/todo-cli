def ajouter_tache(tache):
    with open("todo.txt", "a") as f:
        f.write(tache + "\n")
    print(f"Tâche ajoutée : {tache}")
