def main(): # 2407905288
    num_list = get_numbers()
    print(len(num_list))
    _, count = sort_inversion_count(num_list)
    print(count)

def get_numbers():
    fh = open("PA2.txt", 'r')
    unsorted_list = []
    for line in fh:
        num = line.strip()
        unsorted_list.append(int(num))
    fh.close()
    return unsorted_list

def sort_inversion_count(array):
    n = len(array)
    if n <= 1: return array, 0
    half_idx = n // 2
    first_half = array[0:half_idx]
    second_half = array[half_idx:]
    (B, X) = sort_inversion_count(first_half)
    (C, Y) = sort_inversion_count(second_half)
    (D, Z) = count_split_inversion(B, C)
    
    return D, X+Y+Z
        

def count_split_inversion(B, C):
    # basic value
    i = 0
    j = 0
    
    # return values
    D = list()
    count = 0
    
    # merge
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            count += len(B) - i
    
    D.extend(B[i:])
    D.extend(C[j:])
            
    return D, count

main()