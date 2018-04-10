import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from wheel.signatures.djbec import l

HEADERS = [
    "class",
    "cap-shape",
    "cap-surface",
    "cap-color",
    "bruises",
    "odor",
    "gill-attachment",
    "gill-spacing",
    "gill-size",
    "gill-color",
    "stalk-shape",
    "stalk-root",
    "stalk-surface-above-ring",
    "stalk-surface-below-ring",
    "stalk-color-above-ring",
    "stalk-color-below-ring",
    "veil-type",
    "veil-color",
    "ring-number",
    "ring-type",
    "spore-print-color",
    "population",
    "habitat"
]

dataset = pd.read_csv("mushrooms.csv")
train_x, test_x, train_y, test_y = train_test_split(dataset[HEADERS[1:]], dataset[HEADERS[0]], test_size=42)
clf = MLPClassifier()
clf.fit(train_x, train_y)
print("Training Accuracy  :", clf.score(train_x, train_y))
print("Test Accuracy      :", clf.score(test_x, test_y))
