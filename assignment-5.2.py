largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    #print(num)
    try:
        transform = int(num)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = transform
    elif transform < smallest:
        smallest = transform

    if largest is None:
        largest = transform
    elif transform > largest:
        largest = transform

print("Maximum is", largest)
print("Minimum is", smallest)
