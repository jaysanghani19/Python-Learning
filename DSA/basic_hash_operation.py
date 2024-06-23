def count_frequency(arr):
    freq_map = {}

    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else :
            freq_map[num] = 1
    return freq_map

def high_frequency_items(arr):
    count_items = count_frequency(arr)
    highest_frequency = max(count_items.values())
    high_frequency = [key for key, value in count_items.items() if value == highest_frequency]

    return high_frequency

arr = [1,1,2,3,5,1,2,5,7,2,3,2,1,1,2]
print(count_frequency(arr))
print(high_frequency_items(arr))