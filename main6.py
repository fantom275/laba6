n = int(input())

files = {}

for i in range(n):
    data = input().split()
    files[data[0]] = data[1:]

m = int(input())

operations = []

for i in range(m):
    operations.append(input().split())

for operation, filename in operations:

    if operation == "read":
        permission = "R"
    elif operation == "write":
        permission = "W"
    else:
        permission = "X"

    if permission in files[filename]:
        print("OK")
    else:
        print("Access denied")