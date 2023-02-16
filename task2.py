import math

def cos_distance(v1, v2):

    if len(v1) == 0 or len(v2) == 0:
        print("Получен пустой вектор")
        return
    if len(v1) != len(v2):
        print("Векторы должны быть одинаковой длины")
        return


    dot_prod = sum([v1[i] * v2[i] for i in range(len(v1))])
    len_v1 = math.sqrt(sum([x ** 2 for x in v1]))
    len_v2 = math.sqrt(sum([x ** 2 for x in v2]))


    if len_v1 == 0 or len_v2 == 0:
        print("один или оба вектора имеют нулевую величину.")
        return
    cos_dist = dot_prod / (len_v1 * len_v2)


    print(f"Косинусное расстояние между {v1} и {v2}: {cos_dist}")

v1 = [1, 2, 3]
v2 = [4, 5, 6]
cos_distance(v1, v2)
