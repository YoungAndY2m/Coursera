def main():
    time = input("What time is it? ")
    timing = convert(time)
    if 7 <= timing <= 8:
        print("breakfast time")
    elif 12 <= timing <= 13:
        print("lunch time")
    elif 18 <= timing <= 19:
        print("dinner time")
    
    
def convert(time):
    hours, minutes = time.split(":")
    timing = float(hours) + float(int(minutes) / 60)
    return timing
    

if __name__ == '__main__':
    main()