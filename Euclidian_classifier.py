"""
Class for the euclidian classifier

Parameter description:
training_set: The part of the dataset designed for training of the algorithm
test_set: The part of the dataset designed for testing of the algorithm
label_position: boolean that indicates if the label is at the beginning of the dataset (False) or at the end (True), by default it is True
"""

from Math_tools import Math_tools

class Euclidian_classifier():

    def euclidian_algorithm(self, training_set, test_set, label_position=True):
        
        # Establish the index corresponding to the class label
        pattern_length = len(training_set[0])
        
        label_index = pattern_length-1 if label_position else 0

        
        # Separate the patterns from their class labels
        training_set_by_classes = {}

        training_set_length = len(training_set)

        for i in range(training_set_length):

            class_label = training_set[i].pop(label_index)

            if(class_label not in training_set_by_classes.keys()):

                training_set_by_classes[class_label] = []

            training_set_by_classes[class_label].append(training_set[i])
        

        # Train the classifier: Calculate the centroid for each class label
        centroids = {}

        for class_label in training_set_by_classes.keys():

            centroids[class_label] = Math_tools.compute_vector_centroid(training_set_by_classes[class_label])      
        

        # Classify the patterns in test set
        for i in range(len(test_set)): test_set[i].pop(label_index) # Eliminate class_labels from test_set

        for i in range(len(test_set)):

            distances = {}

            for class_label in centroids.keys():
                
                distances[Math_tools.compute_euclidian_distance(test_set[i], centroids[class_label])] = class_label

            test_set[i].append(distances[min(distances.keys())])
            
        
        return test_set

