def subArraySumation(a,size):
    sum=0
    for i in range(size):
        sum+=a[i]

    max=sum
    left,right=0,size

    while right<len(a):
        sum-=a[left]
        sum+=a[right]
        left+=1
        right+=1
        if max < sum:
            max=sum
    return max

print(subArraySumation([1,2,3,4,5,6,7,8,9],4))