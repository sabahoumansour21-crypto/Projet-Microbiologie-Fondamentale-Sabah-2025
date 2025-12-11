
#Pandas OUMANSOUR SABAH M1 (Microbiologie Fondamentale)
#for biologie Master Tlemcen...11/12/2025
#Chef du projet: OUMANSOUR SABAH
#Membres de l'équipe:
#Yaiche rania imane
#Youbi Imene 
#PROJET D'ANALYSE DE SÉQUENCES ADN
import pands as pd 
#données: séquence adn, langeur, pourcentage de GC
Data=[
"séquence":[" ATGCGTACGTA "," GCTAGCTAGGCC "," ATGCGTACGTA ","TACGATCGTA"," ATGAAAGGCTT", "CGTACGTAGC"," TTAACCGGAT "] 
" longueur ":[12,12,10,11,10,10]
" pourcentage "[50,66.67,58.33,40,45.45,60,50]
#création d'un data frame(tableau pands) 
df=pd. Data frame (data) 
Print (" ****************création et affichage *****************") 
#affichage du tableau 
print ("tableau des séquence Adn; ") 
Print (df) 
#opération sur les tableaux 
Print (" **************opération ***************") 
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
#5)ajouté une nouvelle colonne avec des calcul 
Print (" *************ajouté d'une nouvelle colonne **************") 
#ajouté une nouvelle colonne "catégorise pourcentages GC") 
df.[" catégorie pour GC"]=df.["pourcentage GC"]. Apply lambda x: "Riche" if x> 55else("moyen "if45<=x<=55" faible")] 
Print (df, "\n" "\n") 
#6) Ajouter une colonne comptant les 'G'
df["Nombre de G"] = df["Séquence"].str.count("G")
print("===== Nombre de G ajoutés =====")
print(df, "\n" "\n")
#7) Calculer l'écart type du Pourcentage GC et de la Longueur des Séquence
print("*******Calcul de l'écart type*******") 
écart_type_GC = df["Pourcentage GC"].std()
écart_type_Longueur = df["Longueur"].std()
print(f"écart type du Pourcentagede GC : {écart_type_GC:.3f}%") 
#8) Sauvegarde et chargement des données avec panda
#Sauvegarder le DataFrame dans un fichier CSV
df.to_csv("tableau_Séquence.csv", index=False)
