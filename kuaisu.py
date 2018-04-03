# 快速排序
def kuaisu (a,l,r):
    i=l
    j=r

    if i>j or i==j :
        return

    key = a[i]

    while i < j:
        while  a[j]>=key and i<j:
            j-=1
        if i<j:
            a[i]=a[j]
            i+=1
        while a[i]<=key and i<j:
            i+=1
        if i<j:
            a[j]=a[i]
            j-=1
    a[i]=key
    kuaisu(a, l, i - 1)
    kuaisu(a, i + 1, r)
    return a




if __name__ == '__main__':
    a=[3,4,5,6,1,2]
    print(kuaisu(a,0,5))




