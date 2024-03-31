name_1 = 'Umid'
name_2 = 'Aziz'
current_name = name_1
while True:
    print(current_name)
    name = input('Enter command: ')
    if current_name == name_1 and name == 'next':
        current_name = name_2
    elif current_name == name_2 and name == 'next':
        current_name = name_1