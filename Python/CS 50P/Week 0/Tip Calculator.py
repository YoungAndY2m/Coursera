def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = round(float(d[1:]), 1)
    print(d)
    return d


def percent_to_float(p):
    # TODO
    p = round(float(p[0:-1])/100, 2)
    # print(len(p) - 1)
    # p = round(float(p[0:{len(p) - 1}]), 2)
    print(p)
    return p


main()