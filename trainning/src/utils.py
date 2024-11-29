import matplotlib.pyplot as plt

def plot_training_history(history):
    plt.figure(figsize=(20, 10))

    plt.subplot(1, 2, 1)
    plt.title('Training and Validation Loss')
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.legend(loc='upper right')

    plt.subplot(1, 2, 2)
    plt.title('Training and Validation Accuracy')
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.legend(loc='lower right')

    plt.show()
