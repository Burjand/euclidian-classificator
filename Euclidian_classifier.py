from Math_tools import Math_tools

class Euclidian_classifier():

    def euclidian_algorithm(self, training_set, test_set):        
        # Calculate training set centroid for each class
        training_set_class_1 = []
        training_set_class_2 = []

        pattern_length = len(training_set[0])

        for pattern in training_set:

            if (pattern[pattern_length-1] == 1):
                
                training_set_class_1.append(pattern[:-1])

            else:

                training_set_class_2.append(pattern[:-1])


        centroid_class_1 = Math_tools.compute_vector_centroid(training_set_class_1)
        centroid_class_2 = Math_tools.compute_vector_centroid(training_set_class_2)
        
        #Classify the patterns in test set
        for i in range(len(test_set)):

            x1 = test_set[i][0]
            y1 = test_set[i][1]

            centroid_1_x2 = centroid_class_1[0]
            centroid_1_y2 = centroid_class_1[1]

            centroid_2_x2 = centroid_class_2[0]
            centroid_2_y2 = centroid_class_2[1]


            distance_to_centroid_1 = Math_tools.compute_euclidian_distance(x1, y1, centroid_1_x2, centroid_1_y2)

            distance_to_centroid_2 = Math_tools.compute_euclidian_distance(x1, y1, centroid_2_x2, centroid_2_y2)
            

            if ( distance_to_centroid_1 < distance_to_centroid_2 ):

                test_set[i][2] = 1.0

            else:

                test_set[i][2] = 2.0

        
        return test_set

