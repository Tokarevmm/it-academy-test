import math

def prob(n: int, m: int, s: int, p: float) -> float:

    cdf = 0
    # for i in range(m, n + 1):
    #     cdf += math.factorial(n) / (math.factorial(i) * math.factorial(n-i)) * p ** i * (1 - p) ** (n - i)
    # return cdf
    cdf += math.factorial(n) / (math.factorial(m) * math.factorial(n-m)) * p ** m * (1 - p) ** (n - m)
    return cdf

n = 10
m = 5
s = 3
p = 1 - s/6

result = prob(n, m, s, p)

print(f"Вероятность того, что выпадет число не менее {s} ровно {m} раз в {n} бросках кубика равна {result:.4f}")
