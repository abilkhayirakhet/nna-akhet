from csv import reader
from csv import writer


# Load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset


dataset = load_csv('mushrooms.csv')
values = dataset[1:]


def convertCharToInteger(values):
    intvalues = []
    for index in range(0, values.__len__()):
        chararray = []
        for char in values[index]:
            chararray.append(ord(char))
        intvalues.append(chararray)
    return intvalues


print(convertCharToInteger(values))
