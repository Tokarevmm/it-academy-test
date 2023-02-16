def central(dist):

    mean = sum(dist) / len(dist)

    mode = max(set(dist), key=dist.count)

    sorted_dist = sorted(dist)

    if len(dist) % 2 == 1:
        median = dist[len(dist) // 2]
    else:
        mid = dist[len(dist) // 2]
        median = (sorted_dist[mid] + sorted_dist[mid + 1]) / 2


    if mean == median == mode:
        print("Распределение идеально симметрично")
    elif mean == median != mode:
        print("Распределение симметрично, но имеет моду")
    else:
        print("Распределение несимметрично")

    print("Среднее значение:", mean)
    print("Мода:", mode)
    print("Медиана:", median)

dist = [2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 10]
central(dist)
