file = input("Enter log file path: ")

try:
    with open(file) as f:
        for line in f:
            if "deny" in line.lower():
                print("Deny log:", line.strip())
except:
    print("File not found")
