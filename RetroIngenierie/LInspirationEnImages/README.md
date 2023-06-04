# L'inspiration en images
  
## Énoncé  
  
Un quart d'heure plus tôt dans la soirée, vous étiez en train de parler avec Sabine de vos méthodes créatives, de vos exercices de style dans vos mediums respectifs. Elle mentionna au fil de la conversation son atelier de peinture se situant dans les combles rustiques du café littéraire, vous suggérant que vous pourriez toujours prendre de l'inspiration en observant ses peintures, son processus de création, sa manière de capturer la beauté insaisissable.

Une fois la conversation et le café terminés, vous vous aventurez dans l'atelier de peinture de Sabine, votre lampe torche à la main. Au milieu de cette mer de tableaux, vous repérez une peinture étrange, criblée d'inscriptions. 

Et au pied du chevalet a chu une note, sur laquelle il est marqué : 'Ma clé est la couleur du fond de la toile'. Vous remarquez également d'autres inscriptions incompréhensibles au verso de la note. Sans doute un message chiffré ?

Vous vous mettez en quête de la clé.
  
***  
  
Note : Le déchiffrage du message n'est pas nécessaire à la complétion du challenge.  
  
**Format** : 404CTF{vec4(r,g,b,a)} où `r`,`g`,`b` et `a` sont des flottants précis au dixième.

Auteur : `Jauttaro Coudjau#0911`
  
### Format
404CTF{vec4(*0.0*,*0.0*,*0.0*,*0.0*)}  
  
## Résolution  

- identification du framework utilisé pour le programme (glfw)  
- documentation sur le fonctionnement d'openGL, trouver le fait que glClearColor(float r, float g, float b, float a) permet d'initialiser la couleur de fond  
- un peu de reverse statique (par exemple avec `radare 2`) permet de retrouver l'appel à glClearColor, avec les variables d'entrée juste à côté (représentation hexa des floats)  
- il ne reste plus qu'a flag :)  
  
## Description des fichiers  
  
### Dans la racine :  
`vue_sur_un_étrange_tableau` : exécutable compilé avec `g++ tableau.cpp glad.c -ldl -lglfw -o vue_sur_un_étrange_tableau` après avoir copié les deux dossiers de `source/include` dans `/usr/include`.  
### Dans le dossier `source` :  
`include/` et `glad.c` : fichiers de la librairie GLAD, qui permet de créer un contexte openGL.  
`texToCode.cpp` et `texToCode` : binaire permettant de transformer une image en array C, ici `bg.jpg` est "transformée" en `bg.jpg.cpp`  
`test_404_2D.cpp` : fichier source de l'application, shaders intégrés dedans.  
### Dans le dossier `message` :  
`message.txt` le message à trouver  
`chiffré.txt` le contenu de `message.txt` chiffré avec openssl : `openssl enc -aes-256-cbc -md sha512 -pbkdf2 -iter 250000 -nosalt -in message.txt -out chiffré.txt`, dont la base64 est donnée dans `verso.txt`  
