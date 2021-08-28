# password generator project 
import random 
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','*']

print('Welcome to the Password Generator!')
nr_letter = int(input('How many letters would you like in your password?\n'))

nr_symbol = int(input('How many symbols would you like?\n'))
nr_number = int(input('How many numbers would you like?\n'))

# strong password generator 
password_list = []

for char in range(1, nr_letter+1):
    password_list += random.choice(letter)

for char in range(1, nr_number+1):
    password_list += random.choice(number)

for char in range(1, nr_symbol+1):
    password_list += random.choice(symbol)

print(password_list)
# use random.shuffle() for random organise list character
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")