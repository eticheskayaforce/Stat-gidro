def read_data():
    a = []
    f = open('1.txt', 'r')
    for line in f:
        a.append(line)
    return [int(i) for i in a]

