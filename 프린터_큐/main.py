for testcase in range(int(input())):
    N, M = map(int, input().split())
    order = list(map(int, input().split()))
    answer = 0
    dict = {}
    
    for i, number in enumerate(order):
        dict[i] = number
    while dict[M] > 0:
        for i in dict:
                
            if dict[i] == max(dict.values()):
                answer += 1
                dict[i] = 0
                if i == M:
                    print(answer)
                    dict[i] = 0
