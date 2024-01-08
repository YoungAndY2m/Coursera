def count_substring(string, sub_string):
    sublength = len(sub_string)
    size = len(string)
    count = 0
    for i in range(size):
        print(i)
        if string[i] == sub_string[0]:
            if i + sublength - 1 < size and string[i:i+size] == sub_string:
                print(f"Here {i}")
                count += 1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)