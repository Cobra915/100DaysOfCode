def prime_checker(number):
    count = 0
    #i=1
    list = []

    # Using a while loop
    '''
    while i <= number:
        if number % i == 0:
            list.append(i)
            count +=1
        i += 1
    '''

    
    for i in range(1,number+1):
        if number % i == 0:
            list.append(i)
            count +=1

    if count <= 2:
        print(f'The number you input is divisible by: {list}')
        print('It\'s a prime number.')
    elif count > 2:
        print(f'The number you input is divisible by: {list}')
        print('It\'s not a prime number.')
    
n = int(input("Check this number: "))
prime_checker(number=n)