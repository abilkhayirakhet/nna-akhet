import pandas as panda
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

dataset = panda.read_csv("mushrooms.csv")
datasetHeaders = []
convertedToIntegerValues = []
newValues = []

for column in dataset:
    datasetHeaders.append(dataset[column].name)

for valueArr in dataset.values:

    for value in valueArr:
        #newValues.append([valueArr, ord(value)]) #convertedToIntegerValues.append(ord(value))
        newValues[value] = ord(value)

print(newValues)
exit()

     #   newValues = [valueArr, ord(value)]
print(newValues)
exit()




df2 = panda.DataFrame(convertedToIntegerValues,columns=datasetHeaders)
print(df2)
exit()

ds2 = panda.DataFrame.from_records(
    datasetHeaders,
    convertedToIntegerValues,
    index=None,
    exclude=None,
    columns=None,
    coerce_float=False,
    #nrows=None
)

#print(convertedToIntegerValues)

#print(convertedToIntegerValues.r((-1,3)))
#print(dataset.values)


train_x, test_x, train_y, test_y = train_test_split(dataset[datasetHeaders[1:-1]], dataset[datasetHeaders[-1]])
print(train_x)
exit()

#scaler = StandardScaler()

#scaler.fit(train_x)

#train_x = scaler.transform(train_x)

#test_x = scaler.transform(test_x)

# min = None

# for i in range(10):
clf = MLPClassifier(activation="identity",learning_rate="invscaling")
# clf = MLPClassifier(activation="logistic")
# clf = MLPClassifier(activation="tanh")
# clf = MLPClassifier(hidden_layer_sizes=(13,13),activation="relu", max_iter=300)

clf.fit(train_x, train_y)

print("Training Accuracy  :", clf.score(train_x, train_y))

print("Test Accuracy      :", clf.score(test_x, test_y))

print()