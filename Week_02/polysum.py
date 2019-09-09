from math import tan, pi


def polysum(n, s):
    radians = pi / n
    regular_area = (0.25 * n * (s**2)) / tan(radians)
    perimeter = s * n
    answer = regular_area + perimeter ** 2
    answer = round(answer, 4)
    return answer


polysum(67, 95)
