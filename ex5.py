def func(N, K):
    return (N + K - 1) // K

N = int(input())
K = int(input())

result = func(N, K)
print(result)