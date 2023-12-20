def main():
    months = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12
    }
    print(prompt_date(months))

def prompt_date(months):
    while True:
        try:
            date = input("Date: ")
            if date.find("/") != -1:
                month, day, year = date.split("/")
                if int(day.strip()) > 31 or int(month.strip()) > 12: continue
                return f"{year.strip()}-{int(month.strip()):02}-{int(day.strip()):02}"
            elif date.find(",") != -1:
                month_day, year = date.split(",")
                month, day = month_day.strip().split(" ")
                if int(day.strip()) > 31: continue
                digit_month = months.get(month)
                return f"{year.strip()}-{digit_month:02}-{int(day.strip()):02}"
            else:
                continue
        except:
            pass


main()
