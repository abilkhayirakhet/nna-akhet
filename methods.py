from csv import reader
from random import randint

# Load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

def convertCharToInteger(values):
    intvalues = []
    for index in range(0, values.__len__()):
        chararray = []
        for char in values[index]:
            chararray.append(ord(char))
        intvalues.append(chararray)
    return intvalues

def getLinesForWriting(data):

    lines = []

    for line in data:
        lineString = ''
        for numbers in line:
            lineString += str(numbers) + ','
        lines.append(lineString[:-1])
    return lines

def getDigitalCsvFile(lines):
    randnumber = randint(1, 100)
    filename = str(randnumber) + '_mushrooms' + '.csv'
    with open(filename, 'a') as the_file:
        the_file.write(get_data_set_headers("mushrooms.csv") + '\n')
        for line in lines:
            the_file.write(line + '\n')
    return filename

def get_data_set_headers(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    headers = getLinesForWriting(dataset[:1])
    return headers[0]

def write_bold(input_string):
    bold = "\033[1m"
    boldReset = "\033[0;0m"
    return bold + input_string + boldReset

