import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    name = sys.argv[1]
    print("hello, my name is", name)


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Array slice
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

print("argv[-1]", sys.argv[-1])
