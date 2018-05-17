# Data prep and generation
import numpy as np
import random

# ML Framework
from keras import Sequential, optimizers
from keras.layers import Dense

# For plotting graphs
import matplotlib.pyplot as plt

# Set a random seed for reproducability
np.random.seed(180517)

######
# 
# This method builds a neural network for the given input shape.
#
def build_model(num_features, num_outputs=1):

    model = Sequential()
    ## Input & hidden layer
    model.add(Dense(3*num_features, input_shape=(num_features,)))
    ## Add the output layer
    model.add(Dense(num_outputs))

    ############################################
    # YOUR CODE GOES HERE
    #############################################

    return model

######
# 
# This method trains neural network for the given data set
#
def train(input_data, output_data, model, num_epocs=50):
    sgd = optimizers.SGD(lr=0.01)
    model.compile(loss='mean_squared_error', optimizer=sgd)
    return model.fit(input_data, output_data, epochs=num_epocs)

######
# 
# Splits a data set up into training and testing (validation) data sets
# based on a percentage.
#
def split_dataset(data_set, percent=0.75):
    data_pivot = int(len(data_set) * percent)
    return data_set[:data_pivot], data_set[data_pivot:]


if __name__=="__main__":
    ## Constants
    num_samples = 1000
    num_features = 20

    ## Data generation
    features = np.random.rand(num_samples, num_features)    
    output = np.max(features, axis=1)

    train_in, test_in = split_dataset(features)
    train_out, test_out = split_dataset(output)

    model = build_model(num_features)
    hist = train(train_in, train_out, model)

    ## Show the overall loss metric calculated on the test data
    results = model.evaluate(test_in, test_out)
    print ("Overall Loss: ", results)

    ## This will plot the loss over epochs
    plt.title('Training loss')
    plt.plot(hist.history['loss'])
    plt.show()

    ## This will plot the data we predict against the known values
    predictions = model.predict(test_in)
    plt.plot(range(num_samples), output,'black')
    plt.plot(range(num_samples-len(predictions), num_samples), predictions, 'green')
    plt.plot(range(num_samples-len(predictions), num_samples), np.reshape(predictions, len(predictions), 1) - test_out, 'maroon')
    plt.show()