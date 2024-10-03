# TIPE project by Amandine BATIER and Lucie MOREAU - 2021/2022
## English

The automatic external defibrillator (AED) project is part of the 2021-2022 Health Prevention theme, for the TIPE (Travail d'Initiative Personnelle Encadré or Supervised Personal Initiative Work) mandatory in french preparatory classes (CPGE). The purpose of the TIPE is to put students in a situation of responsibility or research, to introduce them to scientific approaches and give them a foretaste of their future profession as engineers or researchers. The subject is then free to choose, as long as it remains within the imposed theme. We worked on the functioning of the AED, the recovery of data from the victim, the creation of the ECG and its analysis.

Given the lack of information we were able to find on this subject, we started off by analyzing the components from the loaned AEDs provided by the Défibril company, and then decided to model this same AED.

<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/d%C3%A9fibrillateur_ouvert.png" width="300">
</p>

To do this, we began by recovering a noisy signal from the heart by connecting the AED's electrodes to one of our school's oscilloscopes *(slides 19 and 21 of our presentation)*.
<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/image_oscillo.png" width="300">
</p>

We then digitally filtered this signal for further processing *(slide 28)*: the filters applied were selected to have resulting signals closely resembling a classic electrocardiogram *(as illustrated on slide 18)*.

<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/PDRSTU.png" height="200">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/filtrage_oscillo.png" height="200">
</p>

Following this, we created a fairly simple python code to analyze the properties of each ECG (number of beats per minute, size of QRS complex...) and determine each time whether the signal was to be shocked or not *(slide 32 to 38)*. We then implemented this python code in a Matlab Simulink model, which follows the principle of the AED state diagram *(slide 12)*. The model takes into account the conditions of passage from one stage to the next by, among other things, calculating the victim's impedance *(slide 15)*. Our model's console then allows us to check that the actions take place one after the other and in the intended scenarios *(slide 42)*.

With more time and knowledge, further work regarding the impedance and its use in the case of a AED could have been pursued.


## Français

Le projet du Défibrillateur Automatique Externe (DAE) est rentré dans le thème Santé Prévention de l'année 2021-2022, pour les TIPE (Travail d’Initiative Personnelle Encadré) en classe prépa CPGE. Le principe du TIPE est de mettre les étudiants en situation de responsabilité ou de recherche, pour les initier aux démarches scientifiques et leur donner un avant-gout de leur futur métier d’ingénieur ou de chercheur. Le sujet est alors libre de choix, tant qu’il reste dans le thème imposé. Nous avons travaillé sur le fonctionnement du DAE, sur la partie récupération des données de la victime, création de l’ECG, et analyse de celui-ci.

Compte tenu du manque d’informations que nous avons pu trouver sur ce sujet, nous avons analysé les composants en ouvrant les DAE prêtés par l’entreprise Défibril puis nous avons décidé de faire une modélisation de ce même DAE.

<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/d%C3%A9fibrillateur_ouvert.png" width="300">
</p>

Pour cela nous avons commencé par récupérer un signal bruité provenant du cœur simplement à partir des électrodes du DAE branchées à un oscillateur *(diapo 19 et 21)*.
<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/image_oscillo.png" width="300">
</p>

Nous avons ensuite filtré numériquement ce signal pour pouvoir l’exploiter *(diapo 28)* : les filtres appliqués ont été choisis par nous même pour se
rapprocher le plus possible d’un modèle classique d’électrocardiogramme *(comme illustré diapo 18)*.

<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/PDRSTU.png" height="200">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/filtrage_oscillo.png" height="200">
</p>


Suite à cela, nous avons créé un code python assez simple pour analyser les propriétés de chaque ECG (nombre de battements par minutes, taille du complexe QRS…) et déterminer à chaque fois si le signal était choquable ou non *(diapo 32 à 38)*.

Nous avons ensuite implémenté ce code python dans un modèle Matlab Simulink, qui suit le principe du diagramme d’état du DAE *(diapo 12)*.

<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/diagramme_etat.png" width="500">
</p>

Il prend en compte les conditions de passage d’une étape à l’autre par, entre autres, le calcul de l’impédance de la victime *(diapo 15)*.

<p align="center">
<img src="https://github.com/Lu6m/TIPE_Defibrilateur/blob/main/imagesReadme/impedance.png" width="500">
</p>

La console de notre modèle nous permet ensuite de vérifier que les actions ont bien lieu les unes après les autres dans les cas souhaités *(diapo 42)*.
