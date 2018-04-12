import pandas as panda
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

from methods import load_csv
from methods import convertCharToInteger
from methods import getLinesForWriting
from methods import getDigitalCsvFile

load_csv("mushrooms.csv")

dataset = load_csv('mushrooms.csv')
values = dataset[1:]
data = convertCharToInteger(values)
lines = getLinesForWriting(data)

converted_file = getDigitalCsvFile(lines)

dataset = panda.read_csv(converted_file)
datasetHeaders = []

for column in dataset:
    datasetHeaders.append(dataset[column].name)


train_x, test_x, train_y, test_y = train_test_split(dataset[datasetHeaders[1:-1]], dataset[datasetHeaders[-1]])

# for i in range(10):
#clf = MLPClassifier(activation="identity",learning_rate="invscaling")
#clf = MLPClassifier(activation="logistic")
#clf = MLPClassifier(activation="tanh")
clf = MLPClassifier(hidden_layer_sizes=(13,13),activation="relu", max_iter=300)

clf.fit(train_x, train_y)

print(converted_file)

print("Training Accuracy  :", clf.score(train_x, train_y))

print("Test Accuracy      :", clf.score(test_x, test_y))
