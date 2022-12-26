names = ['John','Bob','Mosh','Sarah','Fahim']
print(names[2]) # will print 2 index elemtn "Mosh"
print(names[2:]) # list start from 2 index
print(names[2:-1]) # list start from 2 index and end in sarah

# Largest number
numbers = [2,4,6,5,9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# three diamentional array
matrix = [
    [1,2,3],
    [5,6,7],
    [8,9,10]
]
print(matrix[0][1])