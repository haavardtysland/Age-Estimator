import tensorflow as tf
from tensorflow import keras
from PIL import Image
import os
import numpy as np
from tensorflow.keras import layers

IMAGE_SIZE = (200,200)

x = []
y = []

folder = './face_age'
set = os.listdir(folder)
num_classes = 0

for i in set:
    num_classes += 1
    for file in os.listdir(f"{folder}/{i}"):
        if file[-4:]=='.png':
            image=keras.preprocessing.image.load_img(f"{folder}/{i}/{file}", grayscale=False, color_mode='rgb', target_size=(150,150))
            x_arr = keras.preprocessing.image.img_to_array(image)
            y.append(int(i[-3:]))
            x.append(x_arr)
print(f"Det er {num_classes} klasser")
print(len(x))
print(len(y))

x = np.asarray(x)
y = np.asarray(y)
x = x.astype('float32')
x /= 255.0
print('Min: %.3f, Max: %.3f' % (x.min(), x.max()))

print(x.shape)
print(y.shape)


def build_model():
    model = keras.Sequential()
    model.add(layers.Conv2D(filters=32,kernel_size=(3,3),activation="relu",input_shape=(150, 150, 3)))
    model.add(layers.MaxPooling2D(pool_size=2, strides=2, padding='valid'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Flatten())
    model.add(layers.Dense(num_classes,activation="linear"))
    return model

model = build_model()
model.summary()

epochs = 50
batch_size = 128

model = build_model()

model.compile(optimizer="adam",loss="mean_absolute_error",metrics=['mean_absolute_error'])

model_history = model.fit(
            x,
            y,
            batch_size= batch_size,
            epochs = epochs,
            verbose=True)