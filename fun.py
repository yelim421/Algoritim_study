with open("input.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line.replace('_',' ')
        fd = line[:3] + ' (' + line[4:-1] + ')' + ';'
        print(fd)

