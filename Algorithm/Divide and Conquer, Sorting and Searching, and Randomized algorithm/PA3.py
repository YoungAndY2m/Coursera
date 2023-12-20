def main(): 
    num_list = get_numbers()
    num_list, count = quick_sort(num_list, 0, len(num_list)-1)
    print(count)

def get_numbers():
    fh = open("PA3.txt", 'r')
    unsorted_list = []
    for line in fh:
        num = line.strip()
        unsorted_list.append(int(num))
    fh.close()
    return unsorted_list

def quick_sort(arr, left, right):
    # increase count num
    num = right - left
    
    # base case
    if right <= left: return arr, 0
    
    # pick element of the array
    pivot = partition(arr, left, right)
    
    # Recursively sort the left partition part
    arr_left, count_left = quick_sort(arr, left, pivot-1)
    
    # Recursively sort the right partition part
    arr_right, count_right = quick_sort(arr, pivot+1, right)
    
    # add all counts
    num += count_left + count_right
    
    return arr, num

def partition(arr, left, right):
    pivot = arr[left] # p:= A[l]
    i = left + 1 # i:= l+1
    for j in range(left+1, right+1):
        if arr[j] < pivot: 
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[left], arr[i-1] = arr[i-1], arr[left]
    return i-1

main()