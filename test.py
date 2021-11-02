import tensorflow as tf
from tensorflow import keras
image_size = (180, 180)
batch_size = 32

train_ds = keras.preprocessing.image_dataset_from_directory(
    "face_age",
    validation_split=0.2,
    subset="training",
    seed=1337,
    shuffle=True,
    image_size=image_size,
    batch_size=batch_size,
)

x = 'kjor';