from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from .model import create_model
from .data_preprocessing import prepare_data

def train_model(folder_path, epochs=48):
    train_set, test_set = prepare_data(folder_path)
    
    model = create_model()

    checkpoint = ModelCheckpoint("../../../models/model.keras", monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, verbose=1, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, verbose=1, min_delta=0.0001)

    callbacks = [checkpoint, early_stopping, reduce_lr]

    history = model.fit(train_set,
                        steps_per_epoch=train_set.n // train_set.batch_size,
                        epochs=epochs,
                        validation_data=test_set,
                        validation_steps=test_set.n // test_set.batch_size,
                        callbacks=callbacks)
    
    return model, history
