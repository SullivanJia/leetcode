def result () :
    flag = 0
    a, b = input().split()
    c1 = list(map(int, input().split()))
    if int(b) == 0:
        return int(a)

    c=list(set(c1))



    for i in range(len(c)):
        j = i
        for j in range(j, len(c)):
            if abs(c[i] - c[j]) == int(b):
                flag += 1
    return flag


if __name__ == '__main__':

    print(result())


