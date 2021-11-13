def erlang_model_B(A, N):
    if N == 0:
        return 1
    else:
        return (A * erlang_model_B(A, N - 1)) / (A * erlang_model_B(A, N - 1) + N)


if __name__ == '__main__':
    average_traffic = int(input('Please, enter the average traffic value in erlangs: '))
    lines = int(input('Please, enter the number of lines: '))
    probability_of_blocking = round(erlang_model_B(average_traffic, lines), 3)
    print(f'The probability of blocking is : {probability_of_blocking}')


