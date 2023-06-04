# Le petit chat [Moyen]

## Introduction ## 
Ce challenge CTF est basé sur l'attaque très connue : l'adversarial attack par descente de gradient rapide sur les 
images. Le but est de modifier légèrement une image afin qu'un humain ne perçoive pas de différence mais qu'une IA 
se trompe totalement dans sa classification. C'est une attaque reproduisible si l'on possède le modèle et que le modèle 
n'est pas protégé contre ce type d'attaque. Si le modèle n'est pas connu, on peut commencer par faire une extraction 
de modèle. Cette attaque est la version facile des attaques possibles sur images. Plus d'informations sur : 
[ML Safety](https://www.mlsafety.org/).

## Énoncé du chall (va être modifié) ##
Mon chat ne peut pas rentrer au club de littérature car les animaux sont interdits. Malheureusement, une IA veille à 
l'application de cette règle à l'entrée. Pouvez-vous *légèrement* modifier mon chat pour qu'il soit reconnu comme une 
théière ? 

*Pour valider le challenge il faudra upload son image de chat modifié sur internet et récupérer son URL. Enfin, il vous 
suffira de vous connecter via netcat et d'entrer l'URL du chat modifié. Voici un site possible : https://imgtr.ee/

Mais attention ! Ne ~~Modifiez~~ pas trop le petit chat ! Sinon son maître ne pourra plus le reconnaître.*

Ébloui par les reflets du soleil sur l'imposante vitrine du café littéraire, vous plissez les yeux et marquez un temps d'arrêt pour vérifier que vous êtes bien au bon endroit. Oui, c'est bien ici : Café Littéraire. Vous vous apprêtez à rentrer dans le bâtiment quand une boule dorée attire votre attention. Tiens, ce n'est pas une boule, mais un petit chat orange, le regard absorbé par la vitrine luisante. Vous vous étonnez de remarquer des lunettes de soleil surplombant ses magnifiques moustaches blanches, même lui s'est équipé en cette douce après-midi d'été. Intéressé, vous vous approchez discrètement, ayant senti votre mouvement, le chat se retourna. 
<< Vous ne seriez pas Hackademicien par hazard. Dit-il, d'un air effrayé.
- Heu, non pourquoi ?
Soulagé, le petit chat se retourna completement, se leva de tout son long sur ses deux pattes arrières, frotta ses griffes sur son pelage et vous tendit la patte.
- Je suis le Chat botté ! Ravi de faire votre connaissance ! 
N'étant pas plus surpis de voir un chat qui parle qu'un chat avec des lunettes languissant devant un café littéraire, vous décidez de tendre votre main à votre tour. 
- Mon maître, Monsieur le Marquis de Carabas m'attend dans ce café, malheureusement je ne peux pas le rejoindre, les chiens sont interdits. 
- Et alors ? Vous êtes un chat, vous devriez pouvoir entrer.
- Justement, je suis sensé pouvoir rentrer, mais l'intelligence artificielle qui garde l'entrée se mélange les neurones ! Voila qu'elle confond les chiens et les chats.
- C'est dérangeant effectivement.
- À cause de ce disfonctionnement, je me retrouve dehors, dit-il, en levant ses lunettes et en vous regardant intensément avec ses gros yeux noirs et son aura envoûtante.  
- Vous allez m'aider n'est-ce pas ? 
Ne sachant que répondre face à cette claire injustice, vous décidez seulement d'acquicer de la tête. Satisfait, le chat s'approcha et vous proposa à voix basse : 
- Vous vous y conaissez dans l'art du camouflage ? Oui ? Excellent, c'est exactement ce qu'il me faut. J'ai entendu dire que les thé était très apprécié dans cet endroit, pouvez-vous m'aider à me faire passer pour une théière ? Cela me permettrai de rejoindre mon maître ! >> 
Ne pouvant plus faire demi-tour, vous prenez une profonde respiration pour vous concentrer sur votre objectif : Transformer ce petit chat roux en théière ! 




## Prérequis pour pouvoir résoudre le challenge ##
- Connaissances de base sur les IA, il faut savoir ouvrir et modifier une image pour qu'elle soit modifiable par le 
modèle, il faut savoir faire une descente de gradient avec les outils de tensorflow.
- Il faut upload une image et récupérer son URL, des sites seront proposés.


## Infra ##
- Le joueur se connecte via netcat et envoie l'url de son image de chat modifié pour que le script de vérification
    puisse directement chercher l'image sur internet. Un petit modèle doit tourner (ResNetV2 qui est un modèle mobile).

## Solution ##
Un script de solution est proposé : ```solution.py```. J'utilise l'outil ART 
([Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)) de Trusted AI
car le code est plus propre et plus efficace. 

Le fichier `requirements.txt` ne contient que les modules nécessaires au vérificateur.

