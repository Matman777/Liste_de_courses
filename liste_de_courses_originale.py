# 1. Ajouter un élément à la liste de courses
# 2. Retirer un élément à la liste de courses
# 3. Afficher les éléments de la liste de courses
# 4. Vider la liste de courses
# 5. Quiter le programme

# Demander à l'utilisateur de choisir une de ces actions en entrant un nombre de 1 à 5

# Si autre chose qu'un nombre de 1 à 5 est entré, le programme doit continuer à afficher les choix.

#Pour boucler sur un itérable et récupérer en même temps l'indice de l'itération, on peut utiliser la fonction enumerate:
# for i, element in enumerate("Python"):
    #print(i, element)
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n


# Pour sorir d'un script en lignes de commandes, on utilise le module sys et la fonction exit:
#  import sys
#  sys.exit()     Ca mettra fin au script éxécuté.



import sys

add = (": Ajouter un élément à la liste")
rmv = (": Retirer un élément de la liste")
consult = (": Afficher les éléments de la liste")
rmv_all = (": Vider la liste")
bye = (": Quiter")
lst_user = [add, rmv, consult, rmv_all, bye]
final_lst = []


while True:
    
    print("__________________________________________")
    print("Choisissez parmi les 5 options suivantes :")
    print(" ")

    for i, element in enumerate(lst_user, 1):
        print(i, element)
    user_choice = input("--> Votre choix : ")

    if user_choice == "5":
        print("A bientôt !")
        sys.exit()
    
    elif user_choice == "1":
        a = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        final_lst.append(a.capitalize())
        print(f"L'élément {a.capitalize()} a bien été ajouté à la liste.")
   
    elif user_choice == "2":
        b = input("Quel élément voulez-vous retirer? ").capitalize()
        if b in final_lst:
            final_lst.remove(b)
            print(f"L'élément {b} a bien été supprimé de la liste.")
        elif b not in final_lst:
            print(f"L'élément {b} n'est pas dans la liste.")
   
    elif user_choice == "3":
        if final_lst == []:
            print("Votre liste ne contient aucun élément.")
        else:
            print(f"Voici le contenu de votre liste : ")
        for i, element in enumerate(final_lst,1):
            print(f"{i}. {element.capitalize()}")
            
        
    elif user_choice == "4":
        final_lst.clear()
        print("La liste a été vidée de son contenu.")
