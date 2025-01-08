import sys

w = sys.argv[1]
origin = f"/Users/mag1cian/Library/Application Support/Code/User/snippets/{w}.json"
dest = f"code/snippets/{w}.json"

with open(origin, "r") as f:
    with open(dest, "w") as f2:
        f2.write(f.read())
