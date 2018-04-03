def bin_search(arry, num):
    low = 0                         # 最小数下标
    high = len(arry) - 1       # 最大数下标
    while low<=high:
        mid = int((low + high) / 2 )    # 中间数下标
        if arry[mid] == num:   # 如果中间数下标等于val, 返回
            return mid
        elif  num< arry[mid]:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:                       # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return None# val不存在, 返回None
ret = bin_search(list(range(1, 10)), 8)
print(ret)