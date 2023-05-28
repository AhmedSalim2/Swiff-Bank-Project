import functions 

# Creating a new account / login
print('Do you have a Swift Bank account?')
print('Press [1] to create a new account\nPress [2] to login to account\n')
account = input('Key in your choice: ')
if account == '1':
    print('Input details to create your account')
    functions.create_account()
    functions.gen_acc_no()
    
#login
elif account == '2':
    functions.validity()
    print()



# Continuation
print('Press [1] to proceed to the main menu\nPress [2] to exit')
press = input('Key in your choice: ')
# Display menu

if press == '1':
    menu = open('menu.txt', 'r')
    data = menu.read()
    print(data)
elif press == '2':
    print('Exiting...')
    exit

# Options
choice = input('Key in your choice: ')

# Change user 
# if choice 


# # checking validity
# valid = input('Key in your account number: ')
# if valid in data:
#     print('Your account is found in there')
#     data = user_info.read(int(valid))
#     print(store)
# else:
#     print('You account could not be found in the database')
