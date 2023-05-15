# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:13:27 2021

@author: lu6mo
"""
import matplotlib.pyplot as plt
import numpy as np

# Application des filtres sur toutes les courbes de l'oscilloscope
def ECG(nom):
    if nom=='Asystolie':
        txt='asystolie.txt'
    elif nom=='Fibrillation ventriculaire': 
        txt='Fibrillation-ventriculaire.txt'
    elif nom=='Tachycardie ventriculaire':
        txt='tachycardie-ventriculaire.txt'
    elif nom=='Oscillorepos':
        txt='axeducoeur.txt'
    elif nom=='Oscilloeffort1':
        txt='Amandine1.txt'
    elif nom=='Oscilloeffort2':
        txt='Amandine2.txt'
    elif nom=='Oscilloeffort3':
        txt='Amandine4.txt'
    elif nom=='Oscilloeffort4':
        txt='Amandine5.txt'
    elif nom=='Oscilloeffort5':
        txt='Amandine7.txt'        
    if nom=='Asystolie' or nom=='Fibrillation ventriculaire' or nom=='Tachycardie ventriculaire':
        with open(txt,'r') as f:
            ligne = f.readlines()
            f.close()
        list1, list2 ,lignes = [], [], []
        for k in range (len(ligne)):
            lst = ligne[k].split(',')
            list1.append(float(lst[0]))    
            # Créé une liste de valeurs temporelles   
            list2.append(float(lst[1]))       
            # Créé une liste de valeurs d'amplitudes 
            lignes.append([list1[k],list2[k]]) 
            # Crée des listes de listes associant le temps avec l'amplitude 
        return lignes  
    else:
        with open(txt,'r') as f:
            lignes = f.readlines()
        list1, list2 ,liste = [], [], []
        for k in range (len(lignes)):
            lst = lignes[k].split(',')
            list1.append(float(lst[0])+1)     
            list2.append(float(lst[1]))       
            liste.append([list1[k],list2[k]]) 
        fourier= np.fft.fft(np.array(list2))
        # On créé la transformé de fourier de notre signal 
        filtre =np.concatenate((np.zeros(2),np.ones(93),np.zeros(10),np.ones(105),
                                np.zeros(1581),np.ones(105),np.zeros(10),np.ones(93),np.zeros(1)))
        # On créé un filtre symétrique
        transffourier= np.multiply(fourier,filtre)
        # Qu'on applique sur la transofrmée de Fourier
        signal = np.fft.ifft(transffourier)
        # On retransforme notre signal en amplitude en fonction du temps 
        lignes=[]
        for i in range (len(list1)): 
            lignes.append([list1[i],np.real(signal)[i]])
        return lignes
    

################# ANALYSE ET DONNEES DES COURBES ##############

# Déterminerl'emplacement des pics et la période pour obtenir le nombre de 
# battements par minute       
def périodebpm(nom):
    lignes=ECG(nom)
    n1=len(lignes)
    maxi=lignes[0][1]
    lpics=[]
    periodes=0
    for i in range (n1):
        if lignes[i][1]>6e-4:
        #Lors d'un pic
            if lignes[i][1]>maxi:
            #On détermine le maximum
                maxi=lignes[i][1]
            elif lignes[i][1]<maxi and lignes[i-1][1]==maxi: 
            #Lorsque le maximum est atteint, on met le temps et son maximum 
            # associé dans une liste lpics pour plus tard 
                a=[lignes[i-1][0],i-1,lignes[i-1][1]]
                lpics.append(a)
        else :  
        #Lorsqu'on est en dehors d'un pic, le repasse le maximum à 0
        # pour ne pas comparer les maximums des pics entre eux 
            maxi=0
    longlpics=len(lpics)
    if lpics==[]:
        return 0,[]
    else : 
        for k in range (1,longlpics):
            periodes+=lpics[k][0]-lpics[k-1][0]
            # On détermine le temps entre chaque pic et on additionne toutes
            # les valeurs ensemble 
        T=periodes/(longlpics-1)
        # On divise par le nombre d'intervalles pour faire la moyenne 
        # C'est notre période 
        bpm=60//T
        # On divise 1 minute par notre période pour obtenir le nombre de bpm
        return bpm,lpics



# Déterminer la taille du complexe QRS 
def tailleQRS(nom):
    bpm,lpics=périodebpm(nom)
    # On récupère les valeurs obtenues précédemment pour faciliter le calcul
    lignes=ECG(nom)
    lQ=[]
    lS=[]
    lQRS=[]
    n=len(lpics)
    for i in range (1,n-1):
        mini1=lpics[i][2]
        #Pour chaque pic, on définit un minimum qui se trouve au niveau du 
        # maximum actuel (càd au niveau d'un pic)
        fin=0
        k=lpics[i][1]-1
        # On démarre au point juste avant le pic
        while fin==0 and k!=0:
            if mini1<=lignes[k][1] and mini1<=lignes[k-1][1]:
                # On cherche le moment où la courbe remonte, on met 2 
                # conditions pour si les courbes ne sont pas parfaites et
                # possèdent un point décalé des autres
                fin+=1
                # Permet de sortir de la boucle while
                maxim=lignes[k][1]
                imini=k
                # Quand la courbe atteint son point minimum, on stock l'indice
                # et la valeur de ce point
            elif mini1>lignes[k][1]: 
                #On cherche le minimum juste avant le pic R
                mini1=lignes[k][1]
                k-=1
            else :
                k-=1        
        k=imini-1
        # On redémarre au point minimum avant le pic
        while fin==1 and k!=0:
            if maxim>=lignes[k][1] and maxim>=lignes[k-1][1]:
                a=[lignes[k][0],lignes[k][1]]
                lQ.append(a)
                # Dès que la courbe remonte, on stocke les coordonnées de ce
                # point Q dans lQ
                fin+=1   
            elif maxim<lignes[k][1]: 
                maxim=lignes[k][1]
                k-=1
                # On cherche le maximum précédent le minimum trouvé
            elif maxim>=lignes[k][1] and lignes[k+1][1]==maxim:
                a=[lignes[k][0],lignes[k][1]]
                lQ.append(a)
                # Dès que la courbe remonte, on stock les coordonnées de ce
                # point Q dans lQ
                fin+=1   
            else : 
                k-=1
        mini2=lpics[i][2]
        k=lpics[i][1]+1
        # On démarre au point juste après le pic 
        while fin==2 and k!=2000:
            if mini2<=lignes[k][1] and mini2<=lignes[k+1][1]:
                # Dès que la courbe remonte, on stocke les coordonnées de ce
                # point S dans lS
                maxi=lignes[k][1]
                imaxi=k
                fin+=1
            elif mini2>lignes[k][1]:
                mini2=lignes[k][1]
                k+=1
            else : 
                k+=1      
        k=imaxi+1
        # On démarre au point minimum après le pic
        while fin==3 and k!=2000:
            if maxi>=lignes[k][1] and maxi>=lignes[k+1][1]:
                b=[lignes[k][0],lignes[k][1]]
                lS.append(b)
                fin+=1
            elif maxi>=lignes[k][1]:
                b=[lignes[k][0],lignes[k][1]]
                lS.append(b)
                fin+=1
            elif maxi<lignes[k][1]: 
                maxi=lignes[k][1]
                k+=1
            else : 
                fin+=1
    for i in range (len(lS)):
        lQRS.append(lS[i][0]-lQ[i][0])
    if lQRS ==[]:
        return 0
    else: 
        QRS=sum(lQRS)/len(lQRS)
        return QRS



# Détection en fonction du nombre de bpm et de la taille du QRS de la 
# situation rencontrée : choquable ou non.

def défibrillateur(nom):
    print(nom,':')
    bpm,lpics=périodebpm(nom)
    print('bpm=',bpm)
    QRS=tailleQRS(nom)
    print('Taille QRS=',QRS,'\n')
    if bpm==0 and QRS==0: # cas d'une asystolie
        return False
    elif 50<bpm<180 and 0.07<QRS<0.1: # cas d'un patient en bonne santé
        return False 
    elif bpm>=180: # cas d'une tachycardie ou fibrillation ventriculaire
        return True 
    elif QRS>=0.1: # cas d'un QRS large
        return True 
    else : 
        return False


défibrillateur('Asystolie')
défibrillateur('Fibrillation ventriculaire')
défibrillateur('Tachycardie ventriculaire')
défibrillateur('Oscillorepos')
défibrillateur('Oscilloeffort1')
défibrillateur('Oscilloeffort2')
défibrillateur('Oscilloeffort3')
défibrillateur('Oscilloeffort4')
défibrillateur('Oscilloeffort5')



"""
#################### GRAPHIQUES ECG #####################

# plt.figtext(0.5, 0.2,"Fréquence cardiaque : "+ sbpm + "\n" + "Taille QRS :"+ 
            # sQRS,fontsize=18, color='orange',horizontalalignment='center',
            # verticalalignment='baseline')
# plt.figtext(0.2, 0.6,choc,fontsize=24, color='r',fontweight="bold",
            # horizontalalignment='center',verticalalignment='baseline')
"""