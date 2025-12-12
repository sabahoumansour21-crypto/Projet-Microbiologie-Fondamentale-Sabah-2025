#Pandas OUMANSOUR SABAH M1 (Microbiologie Fondamentale)
#for biologie Master Tlemcen...12/12/2025
#Chef du projet: OUMANSOUR SABAH
#Membres de l'équipe:
#Yaiche rania imane
#Youbi Imene 
#PROJET D'ANALYSE DE SÉQUENCES ADN
import pandas as pd 

# Données : Séquences ADN, Longueur, Pourcentage de GC
data = {
    "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur": [11, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

#1) Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)
print("**************** Creation et affichage *****************")
# Affichage du tableau
print("Tableau des séquences ADN :", "\n" "\n")
print(df, "\n" "\n")
# Opérations sur les tableaux:
print("************** Operations ***************")

#2) Sélectionner la colonne "Longueur"
Longueur = df[["Longueur"]]
print(Longueur, "\n" "\n")

#3)Filtrer les séquences avec Longueur supérieur à 10
print("************* Filtrage avec la Longueur *************")
# Filtrer les séquences avec Longueur supérieur à 10
filtered_df = df[df["Longueur"] > 10]
print(filtered_df, "\n" "\n")

#4)Calculer la moyenne du pourcentage de GC
print("************* Calcul de la moyenne *************")
# Calculer la moyenne du pourcentage de GC
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%")
print( "\n" "\n")

#5)Ajouter une nouvelle colonne avec des calculs
print("************* Ajout d'une nouvelle colonne *************")
# Ajouter une nouvelle colonne "catégorisée Pourcentage GC"
df["Catégorie Pourcentage GC"] = df["Pourcentage GC"].apply(lambda x:"Riche" if x > 55 else ("Moyen" if 45<=x<=55 else "faible"))
print(df, "\n" "\n")

#6) Ajouter une colonne comptant les 'G'
df["Nombre de G"] = df["Séquence"].str.count("G")
print("===== Nombre de G ajoutés =====")
print(df, "\n" "\n")

#7) Calculer l'écart type du Pourcentage GC et de la Longueur des Séquence
print("*******Calcul de l'écart type*******") 
écart_type_GC = df["Pourcentage GC"].std()
écart_type_Longueur = df["Longueur"].std()
print(f"écart type du Pourcentagede GC : {écart_type_GC:.3f}%")
print(f"écart type du Longueur: {écart_type_Longueur:.3f}%")
print( "\n" "\n")

#8)Sauvegarde et chargement des données avec panda
#Sauvegarder le DataFrame dans un fichier CSV
df.to_csv("tableau_Séquence.csv", index=False)


