def erlang_model_B(A, N):
    if N == 0:
        return 1
    else:
        return (A * erlang_model_B(A, N - 1)) / (A * erlang_model_B(A, N - 1) + N)


def calculateProbabilityOfBlocking(average_traffic, number_of_lines):
    probability_of_blocking = round(erlang_model_B(average_traffic, number_of_lines), 3)
    return probability_of_blocking

