
taches = []

def ajouter(taches, description):
    taches.append({"description": description, "faite": False})
    return taches

def voir(taches):
    resultats = []
    for i, tache in enumerate(taches):
        statut = "✅" if tache["faite"] else "❌"
        resultats.append(f"{i + 1}. {statut} {tache['description']}")
    return resultats

def marquer_faite(taches, index):
    if 0 <= index < len(taches):
        taches[index]["faite"] = True
    return taches

def modifier(taches, index, nouvelle_description):
    if 0 <= index < len(taches):
        taches[index]["description"] = nouvelle_description
    return taches

def supprimer(taches, index):
    if 0 <= index < len(taches):
        del taches[index]
    return taches

def afficher_menu():
    print("\n=== MENU ===")
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Marquer une tâche comme faite")
    print("4. Modifier une tâche")
    print("5. Supprimer une tâche")
    print("6. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-6) : ")

        if choix == "1":
            desc = input("Entrez la description de la tâche : ")
            ajouter(taches, desc)
            print("✅ Tâche ajoutée.")

        elif choix == "2":
            if not taches:
                print("❌ Aucune tâche.")
            else:
                print("\n📋 Liste des tâches :")
                for ligne in voir(taches):
                    print(ligne)

        elif choix == "3":
            index = int(input("Numéro de la tâche à marquer comme faite : ")) - 1
            marquer_faite(taches, index)
            print("👍 Tâche marquée comme faite.")

        elif choix == "4":
            index = int(input("Numéro de la tâche à modifier : ")) - 1
            desc = input("Nouvelle description : ")
            modifier(taches, index, desc)
            print("✏️ Tâche modifiée.")

        elif choix == "5":
            index = int(input("Numéro de la tâche à supprimer : ")) - 1
            supprimer(taches, index)
            print("🗑️ Tâche supprimée.")

        elif choix == "6":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
