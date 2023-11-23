n = int(input())


for _ in range(n):
    str = input()
    score = 0
    checkpoint = 1

    for i in str:
        if i == 'O':
            score += checkpoint
            checkpoint += 1
        elif i == 'X':
            checkpoint = 1
    print(score)

