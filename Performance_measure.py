class Performance_measure():

    def measure_accuracy(self, original_test_set, classified_test_set):

        set_length = len(original_test_set)
        pattern_length = len(original_test_set[0])

        successes = 0

        for i in range(set_length):

            if (classified_test_set[i][pattern_length-1] == original_test_set[i][pattern_length-1]):

                successes += 1

        accuracy = successes / set_length

        return accuracy
    
    