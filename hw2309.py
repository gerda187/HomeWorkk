import random 
import time 
 
# Генерация массива из 50 миллионов случайных чисел 
array = [random.randint(0, 999999) for _ in range(50000000)] 
 
# Встроенная функция сортировки Python 
start_time = time.time() 
sorted_array = sorted(array) 
end_time = time.time() 
execution_time = end_time - start_time 
print("Встроенная функция сортировки Python: %s секунд" % execution_time) 
 
# Метод sort() для списка Python 
start_time = time.time() 
array.sort() 
end_time = time.time() 
execution_time = end_time - start_time 
print("Метод sort() для списка Python: %s секунд" % execution_time) 
 
# Быстрая сортировка (quick sort) 
def quick_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + middle + quick_sort(right) 
 
start_time = time.time() 
sorted_array = quick_sort(array) 
end_time = time.time() 
execution_time = end_time - start_time 
print("Быстрая сортировка (quick sort): %s секунд" % execution_time) 
 
# Сортировка слиянием (merge sort) 
def merge_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    mid = len(arr) // 2 
    left = arr[:mid] 
    right = arr[mid:] 
    return merge(merge_sort(left), merge_sort(right)) 
 
def merge(left, right): 
    result = [] 
    i = j = 0 
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
    result.extend(left[i:]) 
    result.extend(right[j:]) 
    return result 
 
start_time = time.time() 
sorted_array = merge_sort(array) 
end_time = time.time() 
execution_time = end_time - start_time 
print("Сортировка слиянием (merge sort): %s секунд" % execution_time)
