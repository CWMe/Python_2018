import pandas as pd
import numpy as np
from datetime import datetime
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout, Activation
from keras import optimizers
import matplotlib.pyplot as plt


# Parse the time from a string so we can merge on dates.
def parse(x):
    return datetime.strptime(x, '%m/%d/%Y')


def normalize(x ):
    mean = x.mean()
    rg = x.max() - x.min()
    return (x - mean) / rg


# Set the seed so that we have a reproducible output.
np.random.seed(113017)

# Read in the CSV file for the S&P 500 (data source: yahoo)
spxData = pd.read_csv("SPX.csv", parse_dates=["Date"], date_parser=parse)

mu = spxData["Adj Close"].mean()
r = spxData["Adj Close"].max() - spxData["Adj Close"].min()

spxData["Adj Close"] = normalize(spxData["Adj Close"])

# We want to predict 10 days
spxData["next10DaysPrice"] = spxData["Adj Close"].shift(-10)

# To do this we'll compute some indicators to use as input data that we think will
# help our chances of predicting the market.

# Compute the 200 day moving average
spxData["200sma"] = spxData["Adj Close"].rolling(window=200).mean()

# Compute the 50 day moving average
spxData["50sma"] = spxData["Adj Close"].rolling(window=50).mean()

# Remove columns with na values as they break training.
spxData.dropna(inplace=True)

# These are the columns we are interested in for training
input_cols = ["Adj Close", "200sma", "50sma" ]

# Now build the Training / Test data sets by splitting off this month.
# The last 20 rows of the dataframe represent Nov, 2017. We'll use that to test with and the
# rest will be used for training
spxTestData = spxData[-20:]
spxData = spxData[0:-20]

# Convert them into NumPy arrays for processing
train_input_data_ = np.asarray(spxData[input_cols])
train_output_data = np.asarray(spxData["next10DaysPrice"])

test_input_data = np.asarray(spxTestData[input_cols])
test_output_data = np.asarray(spxTestData["next10DaysPrice"])

# We build a sequential NN 
model = Sequential()
model.add(Dense(units=20, input_shape=(len(input_cols),), kernel_initializer="uniform", activation="tanh"))
# If we over fit, can regularize by dropping some samples
model.add(Dropout(0.1))
model.add(Dense(units=300, kernel_initializer="uniform", activation="tanh"))
model.add(Dense(units=1, kernel_initializer="uniform", activation="tanh"))

# Stochastic gradient descent optimizer with some sensible defaults.
sgd = optimizers.SGD(lr=0.01, momentum=0.9)
model.compile(loss='mean_squared_error',
              optimizer=sgd)

# Uncomment this to view the model summary
# model.summary()

# Train the model.
hist = model.fit(train_input_data_, train_output_data, epochs=15)

results = model.evaluate(test_input_data, test_output_data)
print()
print("Model evaluation results (loss): " + str(results))

results = model.predict(test_input_data)

idx = 0
expected = []
predicted = []
for res in results:
    e = (res[0] * r) + mu
    p = (test_output_data[idx] * r) + mu
    print ("Expected:", e, "Actual:", p)

    expected.append(e)
    predicted.append(p)
    idx += 1

# Plots
plt.plot(hist.history['loss'])
plt.show()

plt.plot(train_output_data)
plt.plot(model.predict(train_input_data_), ".")
plt.show()

plt.plot(expected)
plt.plot(predicted)
plt.show()


# Save

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# Alternatively to save the entire model to a
# single file.
# model.save("whole_model.h5")
