def query_dist(queries):
    word_counts = {}
    for query in queries:
        words = query.split()
        count = len(words)
        if count in word_counts:
            word_counts[count] += 1
        else:
            word_counts[count] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])
    total_count = sum(word_counts.values())
    for count, query_count in sorted_word_counts:
        percentage = query_count / total_count * 100
        print(f"{count} слов{'о' if str(count)[-1] == '1' else 'а' if str(count)[-1] in {'2', '3', '4'} else ''}: {percentage:.2f}%")

queries = ["watch new movies", "coffee near me", "how to find the determinant", "python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing","foreign exchange rates USD/BYN", "Netflix movies watch online free", "Statistics courses online from top universities"]
query_dist(queries)