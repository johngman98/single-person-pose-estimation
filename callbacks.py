import tensorflow as tf
def make_checkpoint_callback(checkpoint_filepath):
  return tf.keras.callbacks.ModelCheckpoint(filepath = checkpoint_filepath,
                                            save_weights_only = True,
                                            monitor = 'val_loss',
                                            mode = 'min', # since monitor val_loss, overwrite when its mean
                                            save_best_only=True,
                                            verbose = True)

# Callback for printing the LR at the end of each epoch.
class PrintLR(tf.keras.callbacks.Callback):
    """Callback for printing the LR at the beginning of each epoch"""

    def on_epoch_begin(self, epoch, logs=None):
        print('\nLearning rate for epoch {} is {}'.format(epoch + 1, self.model.optimizer.lr.numpy()))