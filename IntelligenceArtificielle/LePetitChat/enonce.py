# Python 3.11.3
import numpy as np
import tensorflow as tf
from urllib import request
from PIL import Image
from TresTresSecret import drapeau


def main(file):
    je_merite_le_drapeau = True
    chat_modifie = Image.open(file)

    # Modèle utilisé : ResNet50 de TensorFlow
    model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')

    # Mise du chat dans le réseau
    image_raw = tf.io.read_file(file)
    image = tf.image.decode_image(image_raw)

    # Prétraitement de l'image : on utilise directement la fonction de ResNet50
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = image[None, ...]

    # Prédiction de l'image
    image_probs = model.predict(image)
    _, image_class, class_confidence = tf.keras.applications.resnet50.decode_predictions(image_probs, top=1)[0][0]

    # On vérifie que c'est bien une théière
    if image_class != 'teapot':
        je_merite_le_drapeau = False

    # On cherche le vrai chat
    chat = Image.open('chat.jpg')
    taille = chat.size

    # On utilise la norme L2
    def distance(a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    # On vérifie enfin si le chat n'a pas été trop ~modifié~~
    eps = 70
    for x in range(taille[0]):
        for y in range(taille[1]):
            if distance(chat.getpixel((x, y)), chat_modifie.getpixel((x, y))) > eps:
                je_merite_le_drapeau = False

    if je_merite_le_drapeau:
        print(f'Je mérite le drapeau. Le voici : {drapeau}')
    else:
        print('Je ne mérite pas le drapeau')


try:
    url = input('URL du chat > ')
    file = request.urlretrieve(url)[0]
    main(file)
except Exception as e:
    print(f'Je n\'ai pas récupéré ton chat ! {str(e)}')
