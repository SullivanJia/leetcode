def maopao(a):
    for i in range(len(a)):
        j=i+1
        for j in range(j,len(a)):
            if a[i]>a[j]:
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
    return a

def kuaisu(a,l,r):
    i=l
    j=r
    if (i>j):
        return
    key=a[i]
    while i<j :
        while a[j]>key and i<j:
            j-=1
        if i<j :
            a[i]=a[j]
            i+=1
        while a[i]<key and i<j:
            i+=1
        if i<j:
            a[j]=a[i]
            j-=1
    a[i]=key
    kuaisu(a,l,i-1)
    kuaisu(a,i+1,r)
    return a

def charu(a):
    for i in range(len(a)):
        j=i
        key=a[i]
        while a[j-1]>key and j>0:
            a[j]=a[j-1]
            j-=1
        a[j]=key
    return a

def xuanze(a):
    for i in range(len(a)):
        j=i
        key=i
        for j in range(j+1,len(a)):
            if a[j]<a[key]:
                key=j
        tmp=a[key]
        a[key]=a[i]
        a[i]=tmp
    return a


if __name__ == '__main__':
    a=[1,6,2,3,5,4]
    print(charu(a))
    # print(kuaisu(a,0,5))
    # print(xuanze(a))
    # print(maopao(a))
