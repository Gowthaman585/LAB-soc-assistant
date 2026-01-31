# Function Declaration
def read_sshd():
    # try block to ensure log file presence
    try:
        with open('auth.log','r',buffering=8192) as file:
            for log in file:
                # passing only sshd logs include's corrupted sshd logs
                if 'sshd[' in log:
                    yield log
    except FileNotFoundError:
        return "File does not exist"

# Function Decalration for sudo logs
def read_sudo():
    try :
        with open('auth.log','r',buffering=8192) as file:
            for log in file:
                if 'sudo: ' in log:
                    yield log
    except FileNotFoundError :
        return 'File does not found'

