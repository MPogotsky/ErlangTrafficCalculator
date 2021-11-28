def erlang_model_B(A, N):
    if N == 0:
        return 1
    else:
        return (A * erlang_model_B(A, N - 1)) / (A * erlang_model_B(A, N - 1) + N)
