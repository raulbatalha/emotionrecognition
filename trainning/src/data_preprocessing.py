import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def prepare_data(folder_path, picture_size=48, batch_size=128):
    datagen_train = ImageDataGenerator()
    datagen_val = ImageDataGenerator()

    train_set = datagen_train.flow_from_directory(os.path.join(folder_path, "train"),
                                                  target_size=(picture_size, picture_size),
                                                  color_mode="grayscale",
                                                  batch_size=batch_size,
                                                  class_mode='categorical',
                                                  shuffle=True)

    test_set = datagen_val.flow_from_directory(os.path.join(folder_path, "validation"),
                                               target_size=(picture_size, picture_size),
                                               color_mode="grayscale",
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)
    
    return train_set, test_set
