def oddNumbers(l, r):
    result = 0
    results = []
    while l <= r:
        result = l % 2
        if result  != 0:
            results.append(l)
        l+=1
    return results

print(oddNumbers(2,5))