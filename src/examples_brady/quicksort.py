def quicksort(arr):
    # Base case: arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    # Pick a pivot
    pivot = arr[0]
    # Separate all vals smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # Sort smaller and larger
    # Concatenate smaller + pivot + larger
    return quicksort(smaller) + [pivot] + quicksort(larger)
################################
# MERGESORT
​
[2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
​
# (base case) If the array is empty or length 1, return
​
# Split the arrays into half
arr1 = [2, 0, 1, 3, 6]
arr2 = [9, 8, 5, 7, 4]
​
# Sort each half
arr1 = [0,1,2,3,6]
arr2 = [4,5,7,8,9]
​
# Merge them back together
# Compare the first values of each array, add smaller of the 2 to result
merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
​
########################
# RULES FOR RECURSION
# 1. Must have a base case.
# 2. Must change state toward the base case.
# 3. Must call itself, recursively.
########################


def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total
​
​
​
# n! = n * (n-1)!
def factorial_r(n):
    if n <= 1:
        return 1
    return n * factorial_r(n-1)
​
​
factorial(5)
factorial_r(5)

####################
def shuff(n=10):
    arr = list(range(n))
    random.shuffle(arr)
    return arr

###################
def selection_sort( arr ):
    # loop through n-1 elements
    # (n-1 because after the sort, the one remaining will be the largest)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

#########################
import time
import random
from sort_solutions import bubble_sort, selection_sort, insertion_sort, quicksort, merge_sort
​
l1 = list(range(1000))
random.shuffle(l1)
l2 = list(range(2000))
random.shuffle(l2)
l3 = list(range(3000))
random.shuffle(l3)
l4 = list(range(4000))
random.shuffle(l4)
l5 = list(range(5000))
random.shuffle(l5)
l6 = list(range(6000))
random.shuffle(l6)
l7 = list(range(7000))
random.shuffle(l7)
l8 = list(range(8000))
random.shuffle(l8)
l9 = list(range(9000))
random.shuffle(l9)
l10 = list(range(10000))
random.shuffle(l10)
​
shuffled_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
​
​
results = []
for shuffled_list in shuffled_lists:
    l_copy = shuffled_list.copy()
    start_time = time.time()
    bubble_sort(l_copy)
    end_time = time.time()
    print(f"runtime: {end_time - start_time}")
    results.append(end_time - start_time)
​
for result in results:
    print(result)
##########################        
def fib(n, cache=None):
    if cache is None:
        cache = {}
    # Base case
    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        # Recursive call, should move toward base case
        return answer
#######################

# What is time and space complexity?
# the way time and space requirements scale with input size
###########################