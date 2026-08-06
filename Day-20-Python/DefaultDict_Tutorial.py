from collections import defaultdict


N, M = map(int, input().split())


d = defaultdict(list)


for i in range(1, N + 1):
    word = input()
    d[word].append(i)


for _ in range(M):
    word = input()

    if word in d:
        print(*d[word])
    else:
        print(-1)