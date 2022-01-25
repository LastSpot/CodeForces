def firstHalf(snapLength, array):
    del array[0:snapLength]
    return array

def secondHalf(snapLength, array):
    del array[snapLength:len(array)]
    return array

def thanos(array):
    snapLength = int(len(array)/2)
    while not sorted(array):
        array1 = array.copy()
        array2 = array.copy()
        a = firstHalf(snapLength,array1)
        b = secondHalf(snapLength,array2)
        len_a = thanos(a)
        len_b = thanos(b)
        if len_a > len_b:
            return len_a
        else:
            return len_b
    return len(array)

def sorted(array):
    for x in range(len(array)-1):
        if array[x] > array[x+1]:
            return False
    return True
lenArray = int(input())
array = list(map(int, input().split()))
print(thanos(array))