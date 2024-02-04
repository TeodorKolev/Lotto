def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for num in counter:
    print(num)