from Euclidian_classifier import Euclidian_classifier
from Validation_method import Validation_method
from Performance_measure import Performance_measure
import copy

if __name__ == "__main__":

    # Dataset
    dataset_file_path = "D:\\Data\\Knowledge\\Academic\\Master\\CIC\\1er Semestre\\Clasificación inteligente de patrones\\Tareas\\Tarea 4\\08_uci_haberman_65_2_att_27_patt.csv"
    file_delimiter = ','


    # Validation method
    indexes = [10, 14, 23, 27]
    validation_method = Validation_method(dataset_file_path, file_delimiter)
    sets = validation_method.fixed_partition(indexes)

    training_set = sets[0]
    test_set = sets[1]

    print(training_set)
    print(test_set)

    # Algorithm
    euclidian_classifier = Euclidian_classifier()
    classified_test_set = euclidian_classifier.euclidian_algorithm(copy.deepcopy(training_set), copy.deepcopy(test_set))

    print(classified_test_set)

    # Performance measure
    performance_measure = Performance_measure()    
    accuracy = performance_measure.measure_accuracy(test_set, classified_test_set)

    print(accuracy)

