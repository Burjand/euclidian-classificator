from Euclidian_classifier import Euclidian_classifier
from Validation_method import Validation_method
from Performance_measure import Performance_measure
import copy
import csv

if __name__ == "__main__":

    #Dataset
    # Training and Test sets
    training_set_file_path = "D:\\Data\\Knowledge\\Academic\\Master\\CIC\\1er Semestre\\Clasificación inteligente de patrones\\Tareas\\Tarea 4\\mnist_train.csv"
    test_set_file_path = "D:\\Data\\Knowledge\\Academic\\Master\\CIC\\1er Semestre\\Clasificación inteligente de patrones\\Tareas\\Tarea 4\\mnist_test.csv"
    file_delimiter = ','

    csv_file = open(training_set_file_path, newline='')
    training_set = list(csv.reader(csv_file, delimiter = file_delimiter))[1:]

    csv_file = open(test_set_file_path, newline='')
    test_set = list(csv.reader(csv_file, delimiter = file_delimiter))[1:]

    # Convert values from str to float
    for i in range(len(training_set)): training_set[i] = list(map(float, training_set[i]))

    for i in range(len(test_set)): test_set[i] = list(map(float, test_set[i]))


    # Algorithm
    euclidian_classifier = Euclidian_classifier()
    classified_test_set = euclidian_classifier.euclidian_algorithm(copy.deepcopy(training_set), copy.deepcopy(test_set), False)


    # Performance measure
    performance_measure = Performance_measure()    
    accuracy = performance_measure.measure_accuracy(test_set, classified_test_set)

    print(accuracy)