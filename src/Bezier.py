import numpy as np

class Bezier:
    @staticmethod
    def Curve(t, points):
        n = len(points) - 1
        result = np.zeros((len(t), len(points[0])))
        for i in range(n + 1):
            binom = Bezier.binomial_coeff(n, i)
            result += binom * ((1 - t) ** (n - i))[:, None] * (t ** i)[:, None] * points[i]
        return result

    @staticmethod
    def binomial_coeff(n, k):
        from math import comb
        return comb(n, k)