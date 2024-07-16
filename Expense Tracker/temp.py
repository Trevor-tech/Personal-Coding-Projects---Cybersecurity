def add_expenses(expenses, amount, category):
    expenses.append({'amount':amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses: #make with lambda?
        print(f'Amount: ${expense["amount"]} Category: {expense['category']}')

def sum_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category']==category, expenses)

def main(): #what if put parameter
    expenses = []
    
    while True:
        print("\nWelcome to Trevski's Expense Tracker")
        print('\n1. Add an expense')
        print('\n2. Show all expenses')
        print('\n3. Show total expenses')
        print('\n4. Filter expenses by selected category')
        print('\n5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expenses(expenses, amount, category)
            print(f'Added ${amount} under {category}')
        
        elif choice == '2':
            print_expenses(expenses)
        
        elif choice == '3':
            print(f'Total expenses: ${sum_expenses(expenses)}')
        elif choice == '4':
            category = input('Enter your category: ')
            print(f'Showing expenses under {category}:')
            selected_category = filter_expenses_by_category(expenses, category)
            print_expenses(selected_category)
        
        elif choice == '5':
            print("Exiting Trevski's Expense Tracker...")
            break

main()

