import random

store = {
    'name': '',
    'account number': '',
    'balance': '',
}

# Generating a random account number
def gen_acc_no():
    acc_number = random.randint(100, 999)
    return acc_number

 # Creating a new bank account
def create_account():
    num = gen_acc_no()
    user_info = open('userinfo.txt', 'r')
    data = user_info.read()
    name = input('Your name: ')
    while name in data:
        print('Name is already taken')
        name = input('Your name: ')
    store ['name'] = name
    store ['account number'] = num
    print(num)
    store ['balance'] = input('intial deposit: ')
    print(store)
    user_info = open('userinfo.txt', 'a')
    user_info.write(str(store))

# # saving user info
# user_info = open('userinfo.txt', 'a')
# user_info.write(str(store))



# checking validity
def validity():
    valid = input('Key in your account number: ')
    user_info = open('userinfo.txt', 'r')
    data = user_info.read()
    if valid in data:
        print('Your account is found in there')
        data = user_info.read(int(valid))
        print(data)
    else:
        print('You account could not be found in the database')