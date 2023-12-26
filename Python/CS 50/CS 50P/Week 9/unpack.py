# def total(galleons, sickles, knuts):
#     print(galleons, sickles, knuts)
#     return (galleons * 17 + sickles) * 29 + knuts

# coins =[100, 50, 25]
# print(total(*coins), "Knuts")

# coin_dict = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(**coin_dict), "Knuts")

def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)
    print(type(args)) # tuple
    print(type(kwargs)) # dict

f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)
f(25, something="something")