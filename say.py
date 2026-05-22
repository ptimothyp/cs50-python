# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.32.5",
#     "cowsay>=6.1",
# ]
# ///
import cowsay
import sys
from sayings import hello

if len(sys.argv) == 2:
    # cowsay.cow("helly, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
    hello(sys.argv[1])
