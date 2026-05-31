def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

def f(*args, **kargs):
    print(args)

print(total(100, 50, 25))

coins = [100,50,25]
print(total(*coins))

coins = {"galleons" : 100, "sickles" : 50, "knuts" : 25 }
print(total(**coins))


f(10,50,100)
f(coins)
