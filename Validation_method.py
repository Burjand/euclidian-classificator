"""
Class for the validation methods

Fixed partition (This method will be improved in the future for better flexibility in parameters intake)

Description of parameters:
dataset: the dataset for which the validation method will be used
indexes: A list with the indexes to make the partition, it takes 4: a for the training set of class 1, (a,b] for the test set
        of class 1, (b,c] for the training set of class 2 and (c,d] for the test set of class 2.
"""

import csv

class Validation_method():

    def __init__(self, dataset_file_path, file_delimiter):

        # Import dataset from file
        self.csv_file = open(dataset_file_path, newline='')
        self.dataset = list(csv.reader(self.csv_file, delimiter = file_delimiter))



    def fixed_partition(self, indexes: list):

        training_set = []
        test_set = []

        for i in range(indexes[0]):
            
            training_set.append(list(map(float, self.dataset[i])))

        for i in range(indexes[0],indexes[1]):

            test_set.append(list(map(float, self.dataset[i])))

        for i in range(indexes[1],indexes[2]):
            
            training_set.append(list(map(float, self.dataset[i])))

        for i in range(indexes[2],indexes[3]):

            test_set.append(list(map(float, self.dataset[i])))


        return [training_set, test_set]

