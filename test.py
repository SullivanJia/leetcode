# 生成器的使用

def test():
    for i in range(10):
        x= {"number": i}
        yield x

for i in test():
    print(i)
# print(test(1,2,3,5,8))