# 朴素串匹配
def pusu (a,b):
    # a是母串，b是子串
    i,j=len(a),len(b)
    m,n=0,0
    while m<i and n<j:
        if a[m]==b[n]:
            m,n=m+1,n+1
        else:
            m,n=m-n+1,0  #n是记录子串匹配过得数量
    if n==j:
        return m-n

    return -1

if __name__ == '__main__':
    a="abbcabcabdcbajsbajshajapsdasdsdadasdjspsdsadasdnasda"
    b="jsp"
    print(pusu(a,b))