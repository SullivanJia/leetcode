def maopao(a):
    for i in range(len(a)):
        j=1+i
        for j in range(len(a)):
            if a[i]<a[j]:
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
    return a


if __name__ == '__main__':
    a=[5,4,3,6,2,1]
    print(maopao(a))