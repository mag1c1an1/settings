origin = "/Users/mag1cian/Library/Application Support/Code/User/settings.json"
dest = "code/settings.json"

with open(origin, "r") as f:
    with open(dest, "w") as f2:
        f2.write(f.read())