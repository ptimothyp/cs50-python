# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.32.5",
#     "cowsay>=6.1",
# ]
# ///
import requests
import sys
import json


def print_songs(res):
    print(json.dumps(res, indent=2))
    o = res["results"]
    for result in o:
        print("TrackName: ", result["trackName"])
        print("Artist: ", result["artistName"])


def main():
    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
    )
    print_songs(response.json())


response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
if __name__ == "__main__":
    main()
# print(json.dumps(response.json(), indent=2))
