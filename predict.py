import argparse
import os
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the VGG16 model
model = load_model('model_vgg16.h5')

# load and preprocess the image
img = image.load_img(args["image"], target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
img_data = preprocess_input(x)

# predict the class of the input image
predictions = model.predict(img_data)[0]
class_names = ["COVID", "NOT COVID", "NORMAL", "PNEUMONIA"]
print("Predictions:")
for i in range(len(class_names)):
    print(f"{class_names[i]}: {predictions[i]}")
