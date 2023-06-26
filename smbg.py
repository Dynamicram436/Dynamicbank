import math
from datetime import datetime

def bill_cal():
    a = True
    total_price = 0
    list_item_price = []

    while a:
        print('''
        1. List of items
        2. Choose item
        3. Exit
        ''')

        choice = int(input('Enter your choice: '))
        choices = [1, 2, 3]

        if choice in choices:
            d = {'dal': 65, 'oil': 70, 'mirchi': 45, 'paste': 20, 'shampoo': 10}

            if choice == 1:
                c = 1
                for i, j in d.items():
                    print('\t', c, '.', i, '₹', j)
                    c += 1
            elif choice == 2:
                q = True
                while q:
                    print("Press 'q' to see the main menu.")
                    item = input('Enter item: ')

                    if item in d.keys():
                        qnt = input('Enter Quantity: ')
                        if qnt.isdigit():
                            qnt = int(qnt)
                            price = float(d[item] * qnt)
                            list_item_price.append((item, qnt, price))
                            total_price += price
                        else:
                            print('Invalid input for quantity.')
                    elif item == 'q':
                        q = False
                    else:
                        print('Item not found.')

            elif choice == 3:
                a = False
        else:
            print('Invalid input. Please enter a valid choice.')

    return total_price, 'Thank you. Please visit again.', list_item_price


name = input("Enter your name: ")
total, msg, item_price = bill_cal()

if total != 0:
    print('\n')
    print('''
                DYNAMIC STORES
            Guntur, Andhrapradesh, 522004
    ''')
    print('Customer Name:', name, '\t', 'Date:', datetime.now())
    print(20 * '==')

    for j in item_price:
        print('Item:', j[0], '\tQuantity:', j[1], 'Price:', j[2])

    gst = total * 0.01
    gst = math.ceil(gst)
    print(20 * '==')
    print('GST: Rs.', float(gst))
    print('Total payable amount: Rs.', float(gst + total))
    print(20 * '==')
    print('🙏🏻🙏🏻🙏🏻', msg, '🙏🏻🙏🏻🙏🏻')
else:
    print("Hey, you haven't purchased anything. Please buy something you want.")
    bill_cal()
