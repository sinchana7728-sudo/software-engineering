import matplotlib.pyplot as plt
import numpy as np
import time
import copy

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key

array_size = [10, 50, 100, 200, 300, 500]
bubble_sort.perf_counter = []
selection_sort.perf_counter = []
insertion_sort.perf_counter = []

for size in array_size:

    arr = np.random.randint(0, 100, size).tolist()

arr_copy = copy.deepcopy(arr)
start = time.time()
bubble_sort(arr_copy)
bubble_sort.append(time.time() - start)

arr_copy = copy.deepcopy(arr)
start = time.time()
selection_sort(arr_copy)
selection_sort.append(time.time() - start)

arr_copy = copy.deepcopy(arr)
start = time.time()
insertion_sort(arr_copy)
insertion_sort.append(time.time() - start)

plt.figure(figsize = (10, 6))
plt.plot(array_size, bubble_sort, marker='o', label = "Bubble_sort")
plt.plot(array_size, selection_sort, marker='s', label = "Selection_sort")
plt.plot(array_size, insertion_sort, marker='m', label = "Insertion_sort")

plt.xlabel("Array Size(n)")
plt.ylabel("Execution Time(seconds)")
plt.tittle("Execution Time Comparision Of Simple Sorting Algorithm")
plt.grid(True)
plt.show()

                
