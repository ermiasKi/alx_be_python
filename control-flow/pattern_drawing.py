num = int(input('Enter the size of the pattern:'))

i = 0
while i < num:
    for j in range(num):
        print('*',end='')
    print('')
    i += 1