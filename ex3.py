def charu(a):
    for i in range(len(a)):
        j=i
        no=a[i]
        while a[j-1]>no and j>0:
            a[j]=a[j-1]
            j-=1
        a[j]=no
    return a

if __name__ == '__main__':
    a=[5,4,3,6,2,1]
    print(charu(a))