# Compte Rendu de Projet-TIPE de BATIER Amandine et MOREAU Lucie

Le projet du DAE est rentré dans le thème Santé Prévention de cette année 2021-2022, pour les TIPE (Travail
d’Initiative Personnelle Encadré) en CPGE. Le principe du TIPE est de mettre les étudiants en situation de
responsabilité ou de recherche, pour les initier aux démarches scientifiques et leur donner un avant-gout de leur
futur métier d’ingénieur ou de chercheur. Le sujet est alors libre de choix, tant qu’il reste dans le thème imposé.
Nous avons travaillé sur le fonctionnement du DAE, sur la partie récupération des données de la victime,
création de l’ECG, et analyse de celui-ci.

Compte tenu du manque d’informations que nous avons pu trouver sur ce sujet, nous avons analysé les
composants en ouvrant les DAE prêtés par l’entreprise Défibril *(diapo 8)*, puis nous avons décidé de faire une
modélisation du DAE.

Pour cela nous avons commencé par récupérer un signal bruité provenant du cœur simplement à partir des
électrodes du DAE branchées à un oscillateur *(diapo 19 et 21)*. Nous avons ensuite filtré numériquement ce
signal pour pouvoir l’exploiter *(diapo 28)* : les filtres appliqués ont été choisis par nous même pour se
rapprocher le plus possible d’un modèle classique d’électrocardiogramme *(comme illustré diapo 18)*.
Suite à cela, nous avons créé un code python assez simple pour analyser les propriétés de chaque ECG (nombre
de battements par minutes, taille du complexe QRS…) et déterminer à chaque fois si le signal était choquable ou
non *(diapo 32 à 38)*.

Nous avons ensuite implémenté ce code python dans un modèle Matlab Simulink, qui suit le principe du
diagramme d’état du DAE *(diapo 12)*. Il prend en compte les conditions de passage d’une étape à l’autre par,
entre autres, le calcul de l’impédance de la victime *(diapo 15)*.

La console de notre modèle nous permet ensuite de vérifier que les actions ont bien lieu les unes après les
autres dans les cas souhaités *(diapo 42)*.
