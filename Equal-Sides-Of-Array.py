'''
Created on Nov 27, 2020

@author: Salzaidy
'''

# divide the array into 2 by half
# then check if right side is bigger or left side
# based on that move left or right to find even index

def find_even_index(arr):

    evenList = arr

    i = 0
    while i < len(evenList):
        if sum(evenList[:i]) == sum(evenList[i+1:]):

            return i
            i += 1
            break

        i += 1
    else:

        return -1

 # Examples Below for testing
ss = find_even_index([1,100,50,-51,1,1])
print(ss)
dd = find_even_index([1,2,3,4,3,2,1])
print(dd)
ff = find_even_index([1,2,3,4,5,6])
print(ff)
gg = find_even_index(list(range(1,100)))
print(gg)