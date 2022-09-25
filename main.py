import string
import random
up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
numbers = string.digits
punct = string.punctuation
# print(numbers)
# print(punct)
all = up_letters+low_letters+numbers+punct
num_of_pass = int(input("Tell the Number of Passwords you want to Add :=> "))
listAll = []
listAll.extend(list(up_letters))
listAll.extend(list(low_letters))
listAll.extend(list(numbers))
listAll.extend(list(punct))
pass_dict = {} # it saves all the passwords in a dictionary
i = 0
while i<num_of_pass-1:
    app_name = input("Tell the name of the app you want this password for :=> ")
    pass_length = int(input('What is the length of password you want :=> '))
    # print(listAll)
    random.shuffle(listAll)
    password = ""
    password = password.join(listAll[0:pass_length])
    details = {app_name : password}
    add_to_database = 0 # ask in YES/NO whether user wants to add the password in database or not.
    addPass = input("If you want to add this pass to Database Press 'y' else press 'n' :=> ")
    if addPass == 'y':
        pass_dict.update(details)
    else:
        continue
    # print(password)
    # print(pass_dict)
    i += 1
file = open('pass_save.txt','w')
file.write("These are the saved passwords \n")
file.write(str(pass_dict))
file.close()





