import random

# 1. Vytvoření pole s 10 náhodně přeházenými hodnotami od 0-100
arr = random.sample(range(101), 10)
print("Původní pole:", arr)

# 2. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 3. Bogo Sort
def bogo_sort(arr):
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# 4. Selection Sort 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 5. Insertion Sort (Vkládací třídění)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Použití jednotlivých algoritmů

# Kopírování původního pole pro každý algoritmus
arr_bubble = arr.copy()
arr_bogo = arr.copy()
arr_selection = arr.copy()
arr_insertion = arr.copy()

# Bubble Sort
print("\nBubble Sort:")
print(bubble_sort(arr_bubble))

# Bogo Sort
print("\nBogo Sort:")
print(bogo_sort(arr_bogo))

# Selection Sort
print("\nSelection Sort:")
print(selection_sort(arr_selection))

# Insertion Sort
print("\nInsertion Sort:")
print(insertion_sort(arr_insertion))