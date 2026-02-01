import sys
# #################################################################################
def argument_parsing():
    if len(sys.argv)==2:
        # if only two argument passed only the presenc of command must be there
        command = sys.argv[1]
        # it return only as string
        return command 
    elif len(sys.argv) == 3:
        # if three arguments are passes cmd + username
        command = sys.argv[1]
        username = sys.argv[2]
        # returns a tuple consites two elements
        return command , username
    else:
        print("Invalid attempt of argument parsing")
        print("python3 <script> <file/dir name>")
        print("python3 <script> <file/dir name> <username>")
        sys.exit(1)
# ##################################################################################

# ##################################################################################
def pass_sudolog():
    try:
        with open('sudo.log','r',buffering=8152) as file:
            for log in file:
                # handling only the sudo.log which has command in it 
                if 'COMMAND=' in log:
                    yield log
    except FileNotFoundError :
        print("File does not exist.First try to run write.py")
# ###################################################################################


# ******************************************************************************************************#
def split_command():                                                                                    #
    for log in pass_sudolog():                                                                          #
        try:                                                                                            #
            start_index = log.find('sudo: ')+6                                                          #
            # Actual message log after the sudo: "__entire_message__"                                   #
            message = log[start_index:-1]                                                               #
            # Separating the username : and remaining (;semicolon;separated;terms;)                     #
            # Example after 'sudo:' (ubuntu : tty;pwd;prev;command)                                     #
            # Now message has separated with  [":",";,;,;,;"] two parts                                 # 
            message = message.split(':')                                                                #
            # Extracting the user name ubunt                                                            #
            username = message[0].lstrip()                                                              #
            # Now remaiing message[1] contains the "tty;pwd;prev;command" as same one message           #
            # Spitting the four ";" separated sequence into four parts                                  #
            semi_sep_parts = message[1].split(";")                                                      #
            # The semi_sep_parts[1] contains the info about the PWD which is the directory where used.  #
            directory = semi_sep_parts[1]                                                               #
            # The temp variable is used to hold the previlege details like "USER=root"                  #
            temp = semi_sep_parts[2]                                                                    #
            # Again spliting the with '=' to extract only the after = 'root'                            #
            # This helps to extract only the what previliage the log has holds                          #
            temp = temp.split('=')                                                                      #
            # the temp[0] = USER which always same. the temp[1] has the prev_level which is 'root'      #
            prev_level = temp[1]                                                                        #
            # The semi_sep_parts[3] holds the entire command which run by the user or program           #
            command = semi_sep_parts[3]                                                                 #
            yield username,directory,prev_level,command                                                 #
        except Exception as e:                                                                          #
            print(e)                                                                                    #
# *******************************************************************************************************

# =======================================================================================================
def get_value(record):
    return record[1]
# _______________________________________________________________________________________________________
def find_top_user():
    try :
        # declaring a new dict to calculate the freqency of the user access
        userfreq = {}
        arguments = argument_parsing()
        arguments = arguments.strip()
        for username,directory,prev,command in split_command():
            if username not in userfreq and arguments in command :
                # intializing the new new user value part with 0
                userfreq[username] = 1
            elif username in userfreq and arguments  in command:
                # incrementing for repeated user access with same user name
                userfreq[username] = userfreq[username] + 1
            else:
                continue
        # Sorting the frequency of user access using the same dict and storing on the same dict 
        # Key point to remember we need to call the get_value without () 
        userfreq = dict(sorted(userfreq.items() , key=get_value, reverse=True))
        return userfreq
    except Exception as e:
        print("find_top_user()",e)
# ______________________________________________________________________________________________________
def print_top_user():
    userfreq = find_top_user()
    if userfreq:
        for key , val in userfreq.items():
            print(f"{key:5}accessed {val} times")
    else:
        print("No user acceses this file/directory")
# ======================================================================================================
# ======================================================================================================
def find_prev_cmd_used(arguments):
    # Declaring a new list to collect the user differnt privilieges by the same user.
    # Assuming the a user has less differnt number of previleges so list in choosen.
    priv_list = []
    # another list to store the different cmd used by the same user
    cmd_list = []
    for username,directory,priv,command in split_command():
        if username.strip() == arguments[1].strip() and arguments[0] in command:
            command = command.split('=')
            # storing only unique element in both the lists
            if priv not in priv_list:
                priv_list.append(priv)
            if command[1] not in cmd_list:
                cmd_list.append(command[1])
    return list(priv_list) , list(cmd_list)
# ______________________________________________________________________________________________________
def print_prev_cmd_used():
    arguments = argument_parsing()
    try:
        priv_list , cmd_list = find_prev_cmd_used(arguments)
        # printing the different privilege used by the same user
        print("privileages used : ",end="")
        for prev in priv_list:
            print(f"{prev} ",end=" ")
        print(f'\n=================================================')
        print("COMMANDS :")
        # listing out all the commands used by the particular used
        for cmd in cmd_list:
            print(f" └─ {cmd}")
    except Exception as e:
        print("On find_prev_cmd_used() : ",e)
# =======================================================================================================


# ======================================================================================================================================#
                                                                                                                                        #
def right_caller():                                                                                                                     #
    arguments = argument_parsing()                                                                                                      #
    # the argument parser return a string when it sys.argv contains only two argument                                                   # 
    # so we need check is this a string or not to call the print_top_user()                                                             #
    if (type(arguments)) == str:                                                                                                        #
        print_top_user()                                                                                                                #
    # the argumet parser return a tuple (username,command) so we can able to get the length it indictes that it has username + cmd      #
    elif len(arguments) == 2:                                                                                                           #
        print_prev_cmd_used()                                                                                                           #
    else:                                                                                                                               #
        print(f"Invalid arguments Error")                                                                                               #
# ======================================================================================================================================#
right_caller()
