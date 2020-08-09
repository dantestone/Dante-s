from sys import argv

script, Todolist = argv

Todo = {
    
    }

def add_item():
    print('Add new todo list in the format key:value')
    
    print('Enter key')
    add_key = input('>')

    print('Enter value')
    value_added = []
    
    add_value = input('>')
    value_added.append(add_value)
    
    while add_value != "":
        add_value = input('>')
        value_added.append(add_value)
    
    
    return Todo.setdefault(add_key,value_added)

def move_item():
    print('Move item up the list')
    
    for i in Todo.keys():
        print(i)

    select = input('>')
    if select in Todo.keys():
        count = 1
        for i in Todo[select]:
            print(str(count) + '.' + i )
            count +=1

        num = input('>')
        pick = Todo[select][int(num)-1]
        move_to = input('What number should it be now  ')
        Todo[select].insert(int(move_to)-1,pick)
        Todo[select].pop(int(num))
        
        count =1
        for i in Todo[select]:
            print(str(count) + '.' + i )
            count +=1

def update_item():
    print('Update item in the list')
    
    for i in Todo.keys():
        print(i)


    select = input('>')
    if select in Todo.keys():
        count = 1
        for i in Todo[select]:
            print(str(count) + '.' + i )
            count +=1

        num = input('>')
        pick = Todo[select][int(num)-1]
        update_to = input('What should it be  ')
        Todo[select].insert(int(num)-1,update_to)
        Todo[select].pop(int(num))
        
        count =1
        for i in Todo[select]:
            print(str(count) + '.' + i )
            count +=1


def delete_item():
    print('Delete item from the list')
    
    for i in Todo.keys():
        print(i)

    select = input('>')
    if select in Todo.keys():
        count = 1
        for i in Todo[select]:
            print(str(count) + '.' + i )
            count +=1

        num = input('>')
        pick = Todo[select][int(num)-1]
        Todo[select].pop(int(num)-1)
        
        count =1
        for i in Todo[select]:
            print(str(count) + '.' + i )
            count +=1
    
            
        
print('Welcome to your to do list....')
target = open(Todolist,'w')
choice = input(
                   '''
                    1.View all items on the list
                    2.Add a new item to the list
                    3.Move an item up the list
                    4.Update an item on the list
                    5.Delete an item on the list
                    '''
            )

if choice == '1':
    print(target.read())
    
elif choice == '2':
    target.write(str(add_item()))
    print('Added!')
    for i,j in Todo.items():
        print(i,j)

elif choice == '3':
    target.write(move_item())

elif choice == '4':
    target.write(update_item())

elif choice == '5':
    target.write(delete_item())
