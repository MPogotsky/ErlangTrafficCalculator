class ErlangModelB:
    def __init__(self):
        pass

    def __erlang_model_B(self, A, N):
        if N == 0:
            return 1
        else:
            return (A * self.__erlang_model_B(A, N - 1)) / (A * self.__erlang_model_B(A, N - 1) + N)

    def __expand_amount_of_probes(self, array):
        first_value = array[0]
        last_value = array[1]
        position = 1
        for value in range(first_value + 1, last_value):
            array.insert(position, value)
            position += 1
        return array

    def calculateProbabilityOfBlocking(self, average_traffic, number_of_lines):
        probabilities_of_blocking = []
        if isinstance(average_traffic, list):
            average_traffic = self.__expand_amount_of_probes(average_traffic)
            for traffic in average_traffic:
                probability_of_blocking = round(self.__erlang_model_B(traffic, number_of_lines), 3)
                probabilities_of_blocking.append(probability_of_blocking)
        elif isinstance(number_of_lines, list):
            number_of_lines = self.__expand_amount_of_probes(number_of_lines)
            for line in number_of_lines:
                probability_of_blocking = round(self.__erlang_model_B(average_traffic, line), 3)
                probabilities_of_blocking.append(probability_of_blocking)
        else:
            probability_of_blocking = round(self.__erlang_model_B(average_traffic, number_of_lines), 3)
            probabilities_of_blocking.append(probability_of_blocking)

        return probabilities_of_blocking
