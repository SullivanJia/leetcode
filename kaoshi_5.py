def get_data():
    a, b ,c = input().split()
    ans = 0
    values=[]
    for i in range(int(a)):
        values.append(int(input().strip()))
    return solution(ans,int(b),int(c),values)

def solution(ans,b,c,values):
    for j in range(int(b)):
        if values[j]-ans<=c:
            ans+=2*(values[j]-ans)
    return ans


if __name__ == '__main__':
    print(get_data())