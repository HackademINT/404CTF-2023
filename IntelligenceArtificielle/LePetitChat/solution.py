# ART Notebook slightly modified for the purpose of the challenge
# https://github.com/Trusted-AI/adversarial-robustness-toolbox/blob/main/notebooks/attack_defence_imagenet.ipynb

import warnings
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
from art.estimators.classification import KerasClassifier
from art.attacks.evasion import ProjectedGradientDescent
from art.utils import to_categorical
from art.preprocessing.preprocessing import Preprocessor

warnings.filterwarnings('ignore')
if tf.executing_eagerly():
    tf.compat.v1.disable_eager_execution()


im = tf.keras.preprocessing.image.load_img('images/chat_mis_a_jour.jpg')
im = tf.keras.preprocessing.image.img_to_array(im)

# This loads the pretrained ResNet50 model:
model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')


class ResNet50Preprocessor(Preprocessor):
    def __call__(self, x, y=None):
        return tf.keras.applications.resnet50.preprocess_input(x.copy()), y

    def estimate_gradient(self, x: np.ndarray, grad: np.ndarray) -> np.ndarray:
        return grad[..., ::-1]


# Create the ART preprocessor and classifier wrapper:
preprocessor = ResNet50Preprocessor()
classifier = KerasClassifier(clip_values=(0, 255), model=model, preprocessing=preprocessor)


# Same as for the original model, we expand the dimension of the inputs.
x_art = np.expand_dims(im, axis=0)

# Create the attacker:
adv = ProjectedGradientDescent(classifier, targeted=True, max_iter=100, eps_step=1, eps=10)
target_label = 849
x_art_adv = adv.generate(x_art, y=to_categorical([target_label]))

mpimg.imsave('images/mechant_chat.jpg', x_art_adv[0]/255)