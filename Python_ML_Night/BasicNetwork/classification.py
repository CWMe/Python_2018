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



    ############################################
    # YOUR CODE GOES HERE
    #############################################

    return model

######
# 
# This method trains neural network for the given data set
#
def train(input_data, output_data, model, num_epocs=150):
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model.fit(input_data, output_data, epochs=num_epocs)

######
# 
# Splits a data set up into training and testing (validation) data sets
# based on a percentage.
#
def split_dataset(data_set, percent=0.75):
    data_pivot = int(len(data_set) * percent)
    return data_set[:data_pivot], data_set[data_pivot:]

def encode(index, num_categories):
    encoding = np.zeros(num_categories)
    if index >= num_categories:
        index = num_categories - 1
    encoding[index] = 1
    return encoding

if __name__=="__main__":
    ## Constants
    categories = [ "none", "one", "two", "3+"]
    num_samples = 1000
    num_features = len(categories)

    ## Data generation
    features = np.random.rand(num_samples, num_features)

    ## Count number of entries > 0.5
    output = []
    for i in np.sum(np.round(features), axis=1):
        output.append(encode(int(i), len(categories)))
    output = np.asarray(output)

    train_in, test_in = split_dataset(features)
    train_out, test_out = split_dataset(output)

    model = Sequential()
    
    ## Input & hidden layer
    model.add(Dense(3*num_features, input_shape=(num_features,), activation="relu"))
    ## model.add(Dense(10*num_features, activation="relu"))
    ## Add the output layer
    model.add(Dense(len(categories),activation="softmax"))
    hist = train(train_in, train_out, model)

    ## Show the overall loss metric calculated on the test data
    results = model.evaluate(test_in, test_out)
    print (model.metrics_names)
    print ("Overall Loss: ", results)

    ## This will plot the loss over epochs
    plt.title('Training Results')
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['acc'])
    plt.show()

    ## some test cases
    tests = [[0.75, 0.3, 0.3, 0.5], np.zeros(4), np.ones(4), [0.2, 0.5, 0.5, 0.5], [0.49, 0.48, 0.7, 0.52]]
    for test in tests:
        result = model.predict(np.asarray([test]))
        print (test, "=", categories[np.argmax(result)])
