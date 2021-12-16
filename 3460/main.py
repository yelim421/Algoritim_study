T = int(input())
for test_case in range(T):
    n = int(input())
    m = 1
    na = []
    while (m > 0):
        m = n//2
        na.append(n%2)
        n = m
    result = [i for i, value in enumerate(na) if value ==1]
    print(' '.join(str(_) for _ in result))