def get_name():
    sujet = input("Quel est le sujet ? ")
    titre1 = input("Quel est le titre 1 ? ")
    #api image ici en fonction du titre 1
    texte1 = input("Quel est le texte 1 ? ")
    titre2 = input("Quel est le titre 2 ? ")
    #api image ici en fonction du titre 1
    texte2 = input("Quel est le texte 2 ? ")
    titre3 = input("Quel est le titre 3 ? ")
    #api image ici en fonction du titre 1
    texte3 = input("Quel est le texte 3 ? ")
    titre4 = input("Quel est le titre 4 ? ")
    #api image ici en fonction du titre 1
    texte4 = input("Quel est le texte 4 ? ")
    titre5 = input("Quel est le titre 5 ? ")
    #api image ici en fonction du titre 1
    texte5 = input("Quel est le texte 5 ? ")
    return sujet, titre1, texte1, titre2, texte2, titre3, texte3, titre4, texte4, titre5, texte5

def get_info():
    sujet = input("Quel est le sujet ? ")
    
    titre1 = input("Quel est le titre 1 ? ")
    #api image ici en fonction du titre 1
    texte1 = input("Quel est le texte 1 ? ")
    
    titre2 = input("Quel est le titre 2 ? ")
    texte2 = input("Quel est le texte 2 ? ")
    
    titre3 = input("Quel est le titre 3 ? ")
    texte3 = input("Quel est le texte 3 ? ")
    
    titre4 = input("Quel est le titre 4 ? ")
    texte4 = input("Quel est le texte 4 ? ")
    
    titre5 = input("Quel est le titre 5 ? ")
    texte5 = input("Quel est le texte 5 ? ")

    page_info = {'sujet': sujet, 'titre1': titre1, 'titre2': titre2, 'titre3': titre3, 'titre4': titre4, 'titre5': titre5, 'texte1': texte1, 'texte2': texte2, 'texte3': texte3, 'texte4': texte4, 'texte5': texte5,}
    return page_info

    

