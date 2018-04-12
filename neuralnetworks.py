import pandas as panda
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

dataset = panda.read_csv("mushrooms.csv")
datasetHeaders = []
convertedToIntegerValues = []

for column in dataset:
    datasetHeaders.append(dataset[column].name)

for valueArr in dataset.values:
    for value in valueArr:
        #print(ord(value))
        convertedToIntegerValues.append(ord(value))

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