
class ErlangModelB:
    def __init__(self):
        pass

    def __erlang_model_B(self, A, N):
        if N == 0:
            return 1
        else:
            return (A * self.__erlang_model_B(A, N - 1)) / (A * self.__erlang_model_B(A, N - 1) + N)

    def calculateProbabilityOfBlocking(self, average_traffic, number_of_lines):
        probability_of_blocking = round(self.__erlang_model_B(average_traffic, number_of_lines), 3)
        return probability_of_blocking