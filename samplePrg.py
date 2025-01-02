# Given an array of integers, find the sum of its elements.
'''
def sumofInt(listvalue):
    sum = 0
    for value in listvalue:
        sum = sum + value
    return sum

print(sumofInt({12, 3, 4, 15}))

'''


'''
#Solution 02

arr = [12, 3, 4, 15]

print(sum(arr)) '''

#method 03

list1 = [12, 3, 4, 15,1,1];s=0
for i,a in enumerate(list1):
  s+=a
print(s)