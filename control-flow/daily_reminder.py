task = input("Enter your task:")

priority = input('Priority (high/medium/low):')

time_bound = input('Is it time-bound? (yes/no):')


match priority:
    case 'high':
        if time_bound == 'yes':
            print(f'Reminder: {task} is a high priority task that requires immediate attention today!')
        elif time_bound == 'no':
            print(f'Note: {task} is a high priority task. Consider completing it when you have free time.')
    case 'medium':
        if time_bound == 'yes':
            print(f'Reminder: {task} is a medium priority task that should be completed soon.')
        elif time_bound == 'no':
            print(f'Note: {task} is a medium priority task. You can schedule it for later.')
    case 'low':
        if time_bound == 'yes':
            print(f'Reminder: {task} is a low priority task that can be done at your convenience.')
        elif time_bound == 'no':
            print(f'Note: {task} is a low priority task. It can be postponed without issues.')
    case _:
        if time_bound == 'yes':
            print(f'Reminder: {task} is a low priority task that can be done at your convenience.')
        elif time_bound == 'no':
            print(f'Note: {task} is a low priority task. It can be postponed without issues.')

