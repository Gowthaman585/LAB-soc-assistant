import sys

def argument_parsing():
    if len(sys.argv)!=2:
        print("Required two argument <script-name> <directory-name/file-name>")
        sys.exit(1)
    search_tag = sys.argv[1]
    return search_tag

def pass_sudolog():
    try:
        with open('sudo.log','r',buffering=8152) as file:
            for log in file:
                if 'COMMAND=' in log:
                    yield log
    except FileNotFoundError :
        print("File does not exist.First try to run write.py")

def split_command():
    for log in pass_sudolog():
        try:
            start_index = log.find('sudo: ')+6
            message = log[start_index:-1]
            message = message.split(':')
            username = message[0]
            core_message_parts = message[1].split(";")
            directory = core_message_parts[1]
            temp = core_message_parts[2]
            temp = temp.split('=')
            prev_level = temp[1]
            command = core_message_parts[3]
            yield username,directory,prev_level,command
        except Exception as e:
            print(e)

def find_access_to():
    for username,directory,prev_level,command in split_command():
        tag = argument_parsing()
        if tag in command:
            print(f"Accessed by {username.lstrip()}")
            print(f"    worked directory    : {directory.lstrip()}")
            print(f"    previlieage used    : {prev_level}")
            print(f"    command used        : {command.lstrip()}")
            print(f"=========================================")

find_access_to()

    
