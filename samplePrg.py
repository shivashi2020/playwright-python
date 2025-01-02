# Given an array of integers, find the sum of its elements.
'''
def sumofInt(listvalue):
    sum = 0
    for value in listvalue:
        sum = sum + value
    return sum

print(sumofInt({12, 3, 4, 15}))

'''

#Solution 02

arr = [12, 3, 4, 15]

print(sum(arr))