import move

global direction_command, turn_command

command = ''

while (command != 'exit')
    command = input("Enter a command: ")

    if 'forward' == command:
        direction_command = 'forward'
        move.move(speed_set, direction_command, turn_command, rad)
    elif 'backward' == command:
        direction_command = 'backward'
        move.move(speed_set, direction_command, turn_command, rad)
    elif 'DS' in command:
        direction_command = 'no'
        move.move(speed_set, direction_command, turn_command, rad)

    elif 'left' == command:
        turn_command = 'left'
        move.move(speed_set, direction_command, turn_command, rad)
    elif 'right' == command:
        turn_command = 'right'
        move.move(speed_set, direction_command, turn_command, rad)
    elif 'TS' in command:
        turn_command = 'no'
        move.move(speed_set, direction_command, turn_command, rad)

    else:
        sleep(100)
        pass