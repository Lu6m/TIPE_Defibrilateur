# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:29:25 2022

@author: lu6mo
"""

# Afin de pouvoir utiliser les valeurs récupérées dans les fichiers de points,
# il a fallu les récupérer et les transformer en listes au format de python

# Les étapes ci-dessous ont déjà été effectuées sur chaque fichier de données 
def modiftachy():
    f=open('tachycardie-ventriculaire - Copie2.txt',"w")
    with open('tachycardie-ventriculaire - Copie.txt','r') as r:
        lignes = r.readlines()
    lig = []
    for k in lignes:
        s = ''
        for c in k:
            if c!=' ':
                s = s+c
                # On met dans s à la suite les uns les autres, tous les 
                # caractères sauf les espaces 
        s = s.replace(',','.')
        s = s.replace(';','\n')
        lst = s.split('\n')
        # On sépare tous les termes au niveau des \n (changement de ligne)
        L = []
        for el in lst:
            if el!='' and el!='\n':
                L.append(float(el))
        lig.append(L)
    lignes = []
    for L in lig:
        if len(L)!=0:
            lignes.append(L)
    for i in range (len(lignes)):
        lignes[i][0]=lignes[i][0]+0.39095106186518924
        lignes[i][1]=lignes[i][1]*10**(-3)
        f.write(str(lignes[i][0])+";"+str(lignes[i][1])+'\n')
        
def modifasyst():
    f=open('asystolie - nv.txt',"w")
    with open('asystolie.txt','r') as r:
        lignes = r.readlines()
    lig = []
    for k in lignes:
        s = ''
        for c in k:
            if c!=' ':
                s = s+c
                # On met dans s à la suite les uns les autres, tous les 
                # caractères sauf les espaces 
        s = s.replace(',','.')
        s = s.replace(';','\n')
        lst = s.split('\n')
        # On sépare tous les termes au niveau des \n (changement de ligne)
        L = []
        for el in lst:
            if el!='' and el!='\n':
                L.append(float(el))
        lig.append(L)
    lignes = []
    for L in lig:
        if len(L)!=0:
            lignes.append(L)
    for i in range (len(lignes)):
        lignes[i][0]=lignes[i][0]+0.3857308677845832
        lignes[i][1]=lignes[i][1]*10**(-3)
        f.write(str(lignes[i][0])+";"+str(lignes[i][1])+'\n')
    
    
def modiffibril():
    f=open('Fibrillation-ventriculaire - nv.txt',"w")
    with open('Fibrillation-ventriculaire.txt','r') as r:
        lignes = r.readlines()
    lig = []
    for k in lignes:
        s = ''
        for c in k:
            if c!=' ':
                s = s+c
                # On met dans s à la suite les uns les autres, tous les 
                # caractères sauf les espaces 
        s = s.replace(',','.')
        s = s.replace(';','\n')
        lst = s.split('\n')
        # On sépare tous les termes au niveau des \n (changement de ligne)
        L = []
        for el in lst:
            if el!='' and el!='\n':
                L.append(float(el))
        lig.append(L)
    lignes = []
    for L in lig:
        if len(L)!=0:
            lignes.append(L)
    for i in range (len(lignes)):
        lignes[i][0]=lignes[i][0]+0.15909191095437514 
        lignes[i][1]=lignes[i][1]*10**(-3)
        f.write(str(lignes[i][0])+";"+str(lignes[i][1])+'\n')

    
def modif():
    f=open('Fibrillation-ventriculaire - Copie2.txt',"w")
    with open('Fibrillation-ventriculaire - Copie.txt','r') as r:
        lignes = r.readlines()
    lig = []
    for k in lignes:
        s = ''
        for c in k:
            if c!=' ':
                s = s+c
                # On met dans s à la suite les uns les autres, tous les 
                # caractères sauf les espaces 
        s = s.replace(',','.')
        s = s.replace(';','\n')
        lst = s.split('\n')
        # On sépare tous les termes au niveau des \n (changement de ligne)
        L = []
        for el in lst:
            if el!='' and el!='\n':
                L.append(float(el))
        lig.append(L)
    lignes = []
    for L in lig:
        if len(L)!=0:
            lignes.append(L)
    for i in range (len(lignes)):
        f.write(str(lignes[i][0])+","+str(lignes[i][1])+'\n')
        
        
        
    # f=open('asystolie-Copie.txt',"w")
    # with open('asystolie.txt','r') as r:
    #     lignes = r.readlines()
    # lig = []
    # for k in lignes:
    #     s = ''
    #     for c in k:
    #         if c!=' ':
    #             s = s+c
    #             # On met dans s à la suite les uns les autres, tous les 
    #             # caractères sauf les espaces 
    #     s = s.replace(',','.')
    #     s = s.replace(';','\n')
    #     lst = s.split('\n')
    #     # On sépare tous les termes au niveau des \n (changement de ligne)
    #     L = []
    #     for el in lst:
    #         if el!='' and el!='\n':
    #             L.append(float(el))
    #     lig.append(L)
    # lignes = []
    # for L in lig:
    #     if len(L)!=0:
    #         lignes.append(L)
    # for i in range (len(lignes)):
    #     f.write(str(lignes[i][0])+","+str(lignes[i][1])+'\n')
        
    # f=open('tachycardie-ventriculaire - Copie2.txt',"w")
    # with open('tachycardie-ventriculaire - Copie.txt','r') as r:
    #     lignes = r.readlines()
    # lig = []
    # for k in lignes:
    #     s = ''
    #     for c in k:
    #         if c!=' ':
    #             s = s+c
    #             # On met dans s à la suite les uns les autres, tous les 
    #             # caractères sauf les espaces 
    #     s = s.replace(',','.')
    #     s = s.replace(';','\n')
    #     lst = s.split('\n')
    #     # On sépare tous les termes au niveau des \n (changement de ligne)
    #     L = []
    #     for el in lst:
    #         if el!='' and el!='\n':
    #             L.append(float(el))
    #     lig.append(L)
    # lignes = []
    # for L in lig:
    #     if len(L)!=0:
    #         lignes.append(L)
    # for i in range (len(lignes)):
    #     f.write(str(lignes[i][0])+","+str(lignes[i][1])+'\n')