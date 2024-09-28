import math

class Math_tools():

    def compute_euclidian_distance(x1, y1, x2, y2):

        return math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )
    

    def compute_vector_centroid(array: list):

        # Save lenghts of general array and vectos
        length_array = len(array)
        length_array_vectors = len(array[0])

        # Initialize centroid list
        centroid = [0] * length_array_vectors

        # Calculate sum of values for every vector
        for i in range(length_array):

            for j in range(length_array_vectors):

                centroid[j] += array[i][j]

        # Calculate average of every vector
        for i in range(length_array_vectors):

            centroid[i] /= length_array

        return centroid
