class Performance_measure():

    def measure_accuracy(self, original_test_set, classified_test_set, original_test_set_label_position=True):

        # Establish the index corresponding to the class label
        set_length = len(original_test_set)
        pattern_length = len(original_test_set[0])
        
        label_index = pattern_length-1 if original_test_set_label_position else 0

        successes = 0

        for i in range(set_length):

            if (classified_test_set[i][pattern_length-1] == original_test_set[i][label_index]):

                successes += 1

        accuracy = successes / set_length

        return accuracy
    
    ################################################    AQUÍ ESTÁ EL PROBLEMA    #################################################