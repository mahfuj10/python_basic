# while loop

i = 1
while i <= 10:
    print('*' * i)
    i+= 1
print("Loop stoped")

# Guess game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print("You won...!")
        break
    else:
        print('You lost.')

# For loop
for char in 'Python':
    print(char)

for num in [1,2,3,4,54,5]:
    print(num)

for r in range(10, 20): # 10 to 20
    print(r)