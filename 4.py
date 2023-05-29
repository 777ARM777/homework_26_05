def countYears(year, count):
    if y // 400 * 400 == y or y // 4 * 4 == y and y // 100 * 100 != y:
        print(y)
        count += 1
    return count

year = int(input("Enter the year\n"))
count = 0
if year == 0:
    print("The 0 year does not exist")
elif year > 1600:
    for y in range(1600, year + 1):
        count = countYears(y, count)
else:
    for y in range(year, 1601):
        count = countYears(y, count)
print(count - (year < 0))

