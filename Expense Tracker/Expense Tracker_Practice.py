def append_expense(expenses, amount, category):
    expenses.append({'Amount:': amount, 'Category:': category})
    print(f'\nExpenses added: {expenses}')

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense['Amount:']}   Category: {expense['Category:']}')

def sum_expenses(expenses):
    return sum(map(lambda expense: expense['Amount:'], expenses))

def filter_expenses(expenses, category):
    return filter(lambda expense: expense['Category:'] == category, expenses)

def main():
    expenses = []
    while True:
        print('\nTrevski Expense Tracker')
        print('1. Add an expense')
        print('2. Show all your expenses')
        print('3. Display your total expenses')
        print('4. Filter your expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1': 
            amount = input('Enter amount: ')
            category = input('Enter Category: ')
            append_expense(expenses, amount, category)
        
        elif choice == '2':
            print_expenses(expenses)

        elif choice == '3':
            sum_expenses(expenses)

        elif choice == '4':
            category = input('Enter category:')
            print(f'Expenses for {category}')
            filtered_category = filter_expenses(expenses, category)
            print_expenses(filtered_category)

        elif choice == '5':
            print('Exiting Trevski Expense Tracker')
            break


