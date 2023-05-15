import matplotlib.pyplot as plt
import numpy as np

# Ce code a pour but de tracer les courbes une fois filtrés
# il y a plusieurs types de courbes, celles appelées amandine récupérées
# directement sur l'oscilloscope, et les autres, retracés à partir de points 
# récupérés sur des courbes préexistantes (car impossible à avoir sur oscillo)


################## ECG NORMAL #################

def ECGnorm(txt):
    with open(txt,'r') as f:
        lignes = f.readlines()
        f.close()
    lig = []
    for k in lignes:
        s = ''
        for c in k:
            if c!='\x00' and c!=chr(255) and c!=chr(254) and c!=chr(32):
                s = s+c
        s = s.replace(',','.')        
        # On remplace les virgules par des points pour s'adapter à l'écriture
        # de python
        lst = s.split('\t')
        L = []
        for el in lst:
            if el!='' and el!='\n':
                L.append(float(el))
        lig.append(L)
    lignes = []
    for L in lig:
        if len(L)!=0:
            lignes.append(L)
    return lignes


################## ECG NORMAL PAR EXPERIMENTATION #################

def ECGoscillo(txt):
    with open(txt,'r') as f:
        ligne = f.readlines()
        f.close()
    list1, list2 ,liste = [], [], []
    for k in range (len(ligne)):
        lst = ligne[k].split(',')
        list1.append(float(lst[0])+1)    
        # Créé une liste de valeurs temporelles   
        list2.append(float(lst[1]))       
        # Créé une liste de valeurs d'amplitudes 
        liste.append([list1[k],list2[k]]) 
        # Crée des listes de listes associant le temps avec l'amplitude 
    plt.figure()
    plt.grid()
    fourier= np.fft.fft(np.array(list2))
    # On créé la transformé de fourier de notre signal 
    filtre =np.concatenate((np.zeros(2),np.ones(93),np.zeros(10),np.ones(105),
                            np.zeros(1581),np.ones(105),np.zeros(10),np.ones(93),np.zeros(1)))
    # On créé un filtre symétrique
    transffourier= np.multiply(fourier,filtre)
    # Qu'on applique sur la transofrmée de Fourier 
    signal = np.fft.ifft(transffourier)
    # On retransforme notre signal en amplitude en fonction du temps 
    if txt=='axeducoeur.txt':
        titre='ECG oscilloscope au repos'
    elif txt=='Amandine1.txt':
        titre='ECG oscilloscope après effort'
    elif txt=='Amandine2.txt':
        titre='ECG oscilloscope après effort n°2'
    elif txt=='Amandine4.txt':
        titre='ECG oscilloscope après effort et forte respiration'
    elif txt=='Amandine5.txt':
        titre='ECG oscilloscope après effort n°3'
    elif txt=='Amandine7.txt':
        titre='ECG oscilloscope après effort et forte respiration n°2'
    plt.title (titre,fontsize=40)
    plt.xlabel('Temps (s)',fontsize=30)
    plt.ylabel('Amplitude (V)',fontsize=30)
    for tickLabel in plt.gca().xaxis.get_ticklabels():
        tickLabel.set_fontsize(14)
    for tickLabel in plt.gca().yaxis.get_ticklabels():
        tickLabel.set_fontsize(14)
    plt.plot(list1,np.real(signal),linewidth=4, color='black')

ECGoscillo('axeducoeur.txt')
ECGoscillo('Amandine1.txt')
ECGoscillo('Amandine2.txt')
ECGoscillo('Amandine4.txt')
ECGoscillo('Amandine5.txt')
ECGoscillo('Amandine7.txt')

def ECG(txt):
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

def trace(txt,P):
    if P==1 or P==2 or P==3:
        courbe=ECG(txt)
    else : 
        courbe=ECGnorm(txt)
    n=len(courbe)
    tps=[courbe[i][0] for i in range (n)]
    Lpoints=[courbe[i][1] for i in range (n)]
    plt.figure()
    if P==0: 
        plt.axis([0,10,-4e-4,6e-4])
        plt.title ('ECG Normal',fontsize=40)
    elif P==1: 
        plt.axis([0,4,-0.9e-3,0.9e-3])
        plt.title ('ECG Asystolie',fontsize=40)
    elif P==2: 
        plt.axis([0,2,-1.5e-3,1e-3])
        plt.title ('ECG Fibrillation Ventriculaire',fontsize=40)
    elif P==3: 
        plt.axis([0,2,-0.9e-3,0.9e-3])
        plt.title ('ECG Tachycardie Ventriculaire',fontsize=40)
    for tickLabel in plt.gca().xaxis.get_ticklabels():
        tickLabel.set_fontsize(14)
    for tickLabel in plt.gca().yaxis.get_ticklabels():
        tickLabel.set_fontsize(14)
    plt.xlabel('Temps (s)',fontsize=30)
    plt.ylabel('Amplitude (V)',fontsize=30)
    plt.grid()
    plt.plot (tps,Lpoints, color='black',linewidth=4)

trace('mesuresECG.txt',0)
trace('asystolie.txt',1)
trace('Fibrillation-ventriculaire.txt',2)
trace('tachycardie-ventriculaire.txt',3)
