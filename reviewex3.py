def maopao(a):
    for i in range(len(a)):
        j=i+1
        for j in range(j,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

def kuaisu(a,l,r):
    i=l
    j=r
    if i>=j:
        return
    key=a[i]
    while i<j:
        while a[j]>key and i<j:
            j-=1
        if i<j:
            a[i]=a[j]
            i+=1
        while a[i]<key and i<j:
            i+=1
        if i<j:
            a[j]=a[i]
            j-=1
    a[j]=key
    kuaisu(a,l,i-1)
    kuaisu(a,i+1,r)
    return a


def xuanze(a):
    for i in range(len(a)):
        j=i
        key=i
        for j in range(j,len(a)):
            if a[j]<a[key]:
                key=j
        a[i],a[key]=a[key],a[i]

    return a


def charu(a):
    for i in range(len(a)):
        j=i
        key=a[i]
        while j>0 and a[j-1]>key:
            a[j]=a[j-1]
            j-=1
        a[j]=key
    return a

if __name__ == '__main__':
    a=[3,4,2,6,5,1]
    print(kuaisu(a,0,5))



