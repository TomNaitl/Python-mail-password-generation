import random

charsP='qwertyuiopasdfghjklzxcvbnm123456789'
charsM='qwertyuipasdfghjklzxcvbnm'

number = int(input('Кол-во паролей: '))
length = int(input('Длина строки: '))
file=open('password.txt', 'w')
for x in range(number):
    password=""
    mail=""

    for i in range(length):
        password+=random.choice(charsP)
        mail+=random.choice(charsM)
    
    print(password)
    if(x!=number):
        file.write('mail: '+ mail + '@mail.ru   &   password: ' + password + '\n')
    else:
        file.write('mail: '+ mail + '@mail.ru   &   password: ' + password)
file.close()