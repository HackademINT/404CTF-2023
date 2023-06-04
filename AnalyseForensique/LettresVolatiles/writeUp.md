# Lettre Volatiles
## Énoncé et contexte

Le titre de l'énoncé annonce un peu la couleur : **ceci est un challenge volatility**.
L'énoncé décrit le fichier du challenge. Il s'agit du système de fichiers de Célimène, qui aime avoir ses petits secrets.
On s'attend à trouver un dump mémoire dans le système de fichier, car on parle d'une capture de mémoire.

## Énumération du système de fichier
Comme on nous indique que les données que l'ont cherche sont des données utilisateur.

On cherche ainsi des répertoires bien connus comme notamment Images, Téléchargements, Documents,...

Dans Images on trouve le magnifique logo, et un png magifique d'un drapeau. Juste un drapeau. Bon il va faloir chercher plus loin et utiliser l'énoncé.

### Trouver le secret
On trouve s3cr37.zip dans le dossier /documents/perso
qui requiert un mot de passe 
### Trouver le dump mémoire
On trouve un dossier jumpbag qui après des recherche sur internet, on apprend sert à dump la ram. On y trouve un fichier .raw

### Trouver le mot de passe dans le dump
`vol2 -f <image.raw> imageinfo`
`vol2 -f <image.raw> --profile Win7SP1 clipboard`

Toute tentative d'analyser la mémoire liée à firefox mènera à des dead ends, au mieux des private jokes.

### Ouverture du zip
unzip ne supporte pas l'aes, attention
`7z x s3cr37.zip`

On trouve maintenant une lettre d'amour compromettante de Célimène, avec le flag en bas.
