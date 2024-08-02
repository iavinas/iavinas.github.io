# Binomial Coefficient

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def binomialCoeff_bruteForce(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def binomialCoeff_DP(n, k):
    C = [[0 for j in range(k + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

result_brute = binomialCoeff_bruteForce(n, k)
result_DP = binomialCoeff_DP(n, k)

print(f"Binomial Coefficient (Brute Force): {result_brute}")
print(f"Binomial Coefficient (Dynamic Programming): {result_DP}")
