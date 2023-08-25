def main():
    num = input("m: ")
    print("E:", einstein(int(num)))
    
    return 0

def einstein(num):
    c = 300000000
    return num * pow(c, 2)


main()