import pandas as panda
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


from methods import load_csv
from methods import convertCharToInteger
from methods import getLinesForWriting
from methods import getDigitalCsvFile
from methods import write_bold


training_accuracy = []
testing_accuracy = []

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

scaler = StandardScaler()

scaler.fit(train_x)

train_x = scaler.transform(train_x)

test_x = scaler.transform(test_x)

activations = ['identity', 'logistic', 'tanh', 'relu']
solvers = ['lbfgs', 'sgd', 'adam']
learning_rates = ['constant', 'invscaling', 'adaptive']

print(converted_file)


def classify(activation='relu', solver='adam', learning_rate='constant'):
    clf = MLPClassifier(
        activation=activation,
        solver=solver,
        learning_rate=learning_rate,
    )

    clf.fit(train_x, train_y)

    print(
        "Activation is " + write_bold(activation) +
        " Solver is " + write_bold(solver)+
        " Learning rate is  " + write_bold(learning_rate)
    )

    train_accuracy = clf.score(train_x, train_y)
    test_accuracy = clf.score(test_x, test_y)

    training_accuracy.append({"'" + activation+solver+learning_rate+ "'":train_accuracy})
    testing_accuracy.append({"'" + activation+ solver+ learning_rate + "'": test_accuracy})

    print("Training Accuracy  :", train_accuracy)

    print("Test Accuracy      :", test_accuracy)


for activation in activations:
    for solver in solvers:
        for learning_rate in learning_rates:
            classify(
                activation,
                solver,
                learning_rate,
            )

print(write_bold("Finished"))

print(training_accuracy)
print(testing_accuracy)


