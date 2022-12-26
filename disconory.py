student = {
    "name":"Mahfujur Rahnan",
    "id":1
}
print(student.get('name'))
print(student.get('birthday','september 2005')) # set default value

phones = input("Type the number:- ")
number_digits = {
    "1":"One", 
    "2":"Two",
    "3":"Three",
    "4":"Four"
} 
outputs = ''
for char in phones:
   outputs += number_digits.get(char, ' Not get') + ' '
print(outputs)