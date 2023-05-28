import random
import json

USER_INFO_FILE = 'userinfo.json'

def gen_acc_no():
    acc_number = random.randint(100, 999)
    return acc_number

def create_account():
    user_info = load_user_info()
    name = input('Your name: ')
    
    while name in user_info:
        print('Name is already taken')
        name = input('Your name: ')
    
    account_number = gen_acc_no()
    balance = float(input('Initial deposit: '))
    
    user_info[name] = {
        'account_number': account_number,
        'balance': balance
    }
    
    save_user_info(user_info)
    
    print(f'Account created successfully. Account number: {account_number}')

def load_user_info():
    try:
        with open(USER_INFO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_info(user_info):
    with open(USER_INFO_FILE, 'w') as file:
        json.dump(user_info, file)

def check_validity():
    account_holder = input('Enter your name: ')
    user_info = load_user_info()
    
    if account_holder in user_info:
        print('Your account is found in the database')
        data = user_info[account_holder]
        print(f'Account number: {data["account_number"]}')
        print(f'Balance: {data["balance"]}')
    else:
        print('Your account could not be found in the database')

# Main execution flow
def main():
    while True:
        print('1. Create an account')
        print('2. Check account validity')
        print('3. Exit')
        
        choice = input('Enter your choice: ')
        
   sup
        
        if choice == '1':
            create_account()
        elif choice == '2':
            check_validity()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
