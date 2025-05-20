# test_todo.py

import todo

def test_ajouter():
    liste = []
    resultat = todo.ajouter(liste, "Lire un livre")
    assert len(resultat) == 1
    assert resultat[0]["description"] == "Lire un livre"
    assert resultat[0]["faite"] is False

def test_marquer_faite():
    liste = [{"description": "Lire un livre", "faite": False}]
    resultat = todo.marquer_faite(liste, 0)
    assert resultat[0]["faite"] is True

def test_modifier():
    liste = [{"description": "Ancienne tâche", "faite": False}]
    resultat = todo.modifier(liste, 0, "Nouvelle tâche")
    assert resultat[0]["description"] == "Nouvelle tâche"

def test_supprimer():
    liste = [{"description": "Tâche à supprimer", "faite": False}]
    resultat = todo.supprimer(liste, 0)
    assert len(resultat) == 0
