import random
continue_game = 'y'
while continue_game == 'y':

    print('rock, paper, scissor')
    user_choice = input('write your choice ')
    values = ['rock', 'paper', 'scissor']
    if user_choice in values:
        pc_choice = random.choice(values)
        print(f'pc chose {pc_choice}')
        if user_choice == pc_choice:
            print('draw')
        elif user_choice == 'paper':
            if pc_choice == 'scissor':
                print('you lost')
            else:
                print('you won')
        elif user_choice == 'scissor':
            if pc_choice == 'paper':
                print('you won')
            else:
                print('you lost')
        else:
            if pc_choice == 'paper':
                print('you lost')
            else:
                print('you won')
    else:
        print('incorrect value')
    continue_game = input('continue y/n ')
