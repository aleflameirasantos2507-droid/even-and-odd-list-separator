main_list = []
even_numbers = []
odd_numbers = []

while True:
    number = int(input('Enter a value: '))
    main_list.append(number)

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    response = input(
        'Would you like to continue? [Y/N] '
    ).upper().strip()[0]

    if response == 'N':
        break

    while response not in 'YN':
        response = input(
            'Invalid option. Would you like to continue? [Y/N] '
        ).upper().strip()[0]

print(f'Main list: {main_list}')
print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')
