'''
Author: Divija Saini
KUID: 3210396
Date: 3/5/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: Shopping List
'''
print ('Welcome to your Shopping List!')
choice = 0
grocery_list = []
print('1) Add Item \n2) Check off item \n3) Print list \n4) Exit')
choice = int(input('Enter a choice: '))
while choice != 4:
    if choice == 1:
        add_item = input ('What will you add to the list?: ')
        grocery_list.append(add_item)
    if choice == 2:
        check_off = int(input('Which item will you check off?: '))
        index = check_off - 1
        if check_off - 1 <= len(grocery_list):
            item = grocery_list[index]
            new_value = item[0] + ('-' * (len(item) - 2)) + item[-1]
            grocery_list.pop(index)
            grocery_list.insert(index, new_value)
    if choice == 3:
        print ('\nHere is your list: ')
        count = 1
        for item in grocery_list:
            print (str(count)+')', item)
            count = count + 1
    print('\n1) Add Item \n2) Check off item \n3) Print list \n4) Exit')
    choice = int(input('Enter a choice: '))
print('Goodbye!')
