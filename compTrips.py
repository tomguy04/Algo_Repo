def compareTriplets(a,b):
    results = [0,0]
    for i in range(len(a)):
        if(a[i]>b[i]):
            results[0]+=1
        elif(b[i]>a[i]):
            results[1]+=1
    return results


# a = map(int,'1 2 3'.rstrip().split())
a = [1,2,3]
b = [2,1,6]
print(compareTriplets(a,b))
