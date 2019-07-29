# -*- coding: utf-8 -*-
"""Implementation of LeNet architecture.
"""
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K


class LeNet:
    """Implementation of LeNet architecture.

    Returns:
        [obj] -- LeNet model
    """
    @staticmethod
    def build(width, height, depth, classes):
        """Build LeNet model

        Arguments:
            width {int} -- The width of the input image.
            height {int} -- The height of the input image.
            depth {int} -- The number of channels (depth) of the image.
            classes {int} -- The number class labels in the classification task.

        Returns:
            [obj] -- LeNet model
        """
        # initialize the model
        model = Sequential()
        input_shape = (height, width, depth)
        # if we are using "channels first", update
        if K.image_data_format() == "channels_first":
            input_shape = (depth, height, width)
        # first set of CONV => RELU => POOL layers
        model.add(Conv2D(20, (5, 5), padding="same", input_shape=input_shape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # second set of CONV => RELU => POOL layers
        model.add(Conv2D(50, (5, 5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))
        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))
        # return the constructed network architecture
        return model
