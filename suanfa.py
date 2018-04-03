def kuaisu(a,l,r) :
    i =l
    j = r
    if i>=j :
        return
    key=a[i]
    while i<j :
        while a[j]>=key and i<j:
            j-=1
        if i<j:
            a[i]=a[j]
            i+=1
        while a[i]<=key and i<j :
            i+=1
        if i<j:
            a[j]=a[i]
            j-=1
    a[i]=key

    kuaisu(a,l,i-1)
    kuaisu(a,i+1,r)
    return a

def maopao(a):
    for  i  in range(len(a)):
        j=i+1
        for j in range(len(a)):
            if a[i]<a[j]:
                tmp=a[j]
                a[j]=a[i]
                a[i]=tmp
    return a


def xuanze (a):
    for i in range(len(a)):
        j=i
        key= i
        for j in range(len(a)):
            if a[key]<a[j]:
                key=j
            tmp=a[i]
            a[i]=a[key]
            a[key]=tmp
    return a

def charu (a):
    for i in range(len(a)):
        key=a[i]
        j=i
        while key<a[j-1] and j>0:
            a[j]=a[j-1]
            j-=1
        a[j]=key
    return a

def erfen(a ,key):
    low =0
    high=len(a)-1
    while a is not None:
        mid= (low +high)//2
        if a[mid]==key:
            return mid
        if a[mid]<key:
            low=mid+1
        if a[mid]>key:
            high=mid-1
    

if __name__ == '__main__':
    a=[2,3,4,5,6,1]
    print(erfen(a,5))