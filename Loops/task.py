#printing from 1 to 100

count = 1
while count <= 100:
    print(count)
    count += 1

print("Done!")

# printing from 100 to 1

count = 100
while count >= 1:
    print(count)
    count -= 1

print("Done!")

# printing table

table = int(input("Enter the number for table: "))

count = 1
while count <= 10:
    print(table, "x", count, "=", table*count)
    count += 1

print("Done!")
