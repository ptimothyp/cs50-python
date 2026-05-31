def say_camel(n):
    for i in range(n):
        yield "🐪"*i

no_of_camels = int(input("how many camels? "))
for c in say_camel(no_of_camels):
    print(c)
