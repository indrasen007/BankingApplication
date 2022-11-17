# Users List to store all the accounts along with their info.
# This List will contain user objects i.e in Dictionary format.
users = []

# Used to represent error message in case of incorrect input
invalid_input = '''
                Invalid Command! 
                Correct Commands (These commands are case insensitive):

                 To Create a new Account:                   create <account code> <account holders name in single word>
                 To Deposit into an existing account:       deposit <account code> <amount>
                 To Withdraw from an existing account:      withdraw <account code> <amount>
                 To Exit from this CLI application:         quit'''

# To guide the user about what commands he/she can use.
print('''
                Commands (These commands are case insensitive):

                 To Create a new Account:                   create <account code> <account holders name in single word>
                 To Deposit into an existing account:       deposit <account code> <amount>
                 To Withdraw from an existing account:      withdraw <account code> <amount>
                 To Exit from this CLI application:         quit
''')

# A While loop which terminates only when the user inputs "quit" in cli.
# This allows the program to constantly take inputs until exitted.
while True:
    # Splits the input into separate strings.
    command = list(input('> ').split())

    # This block handles the input for "CREATE" command.
    if command[0].upper() == 'CREATE' and len(command) == 3:
        
        user_exists = False

        # Checks if the user already exists.
        for user in users:           
            if user['account_code'] == command[1]:
                user_exists = True
                print('User already exists!')
                break     

        # If the user doesnt exist, create a new one and append it to the list.
        if user_exists == False:
            acc_code = command[1]
            acc_name = command[2]

            new_user = {'account_code' : acc_code, 'account_holder_name' : acc_name, 'account_balance' : 0}
            users.append(new_user)      # New user is added to the list users.

    # This block handles the input for "DEPOSIT" command.
    elif command[0].upper() == 'DEPOSIT' and len(command) == 3:
        # The number part of the input is type casted to int to prevent string values from being entered.
        try:
            command[2] = int(command[2])

        except:
            print(invalid_input)
            continue
            
        # Entered amount is added to the users account only if user exists.
        if type(command[2]) == int:
            user_found = False

            for user in users:
                if user['account_code'] == command[1]:
                    user_found = True
                    user['account_balance'] = user['account_balance'] + int(command[2])
            
            if user_found == False:
                print('User Account not found! Please create a new account or try again with different account code.')
        
        else:
            print(invalid_input)

    # This block handles the input for "WITHDRAW" command.
    elif command[0].upper() == 'WITHDRAW' and len(command) == 3:
        # The number part of the input is type casted to int to prevent string values from being entered.
        try:
            command[2] = int(command[2])

        except:
            print(invalid_input)
            continue
        
        # Entered amount is subtracted from the users account if the user has sufficient balance and only if user exists.
        if type(command[2]) == int:
            user_found = False

            for user in users:
                if user['account_code'] == command[1]:
                    user_found = True

                    if user['account_balance'] >= int(command[2]):
                        user['account_balance'] = user['account_balance'] - int(command[2])
                        
                    else:
                        print('Cannot Withdraw due to Insufficient Balance!')

            if user_found == False:
                print('User Account not found! Please create a new account or try again with different account code.')
        
        else:
            print(invalid_input)

    # This block handles the input for "BALANCE" command.
    elif command[0].upper() == 'BALANCE' and len(command) == 2:
        user_found = False

        for user in users:
            if user['account_code'] == command[1]:
                user_found = True
                print(user['account_code'],user['account_balance'])
            
        if user_found == False:
            print('User Account not found! Please create a new account or try again with different account code.')
   
    # To exit from the main loop and quit the program.
    elif command[0].upper() == 'QUIT':
        break

    else:
        print(invalid_input)