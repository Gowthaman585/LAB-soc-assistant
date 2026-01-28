# Function Declaration
def read():
    # try block to ensure log file presence
    try:
        with open('auth.log','r',buffering=8192) as file:
            for log in file:
                # passing only sshd logs include's corrupted sshd logs
                if 'sshd[' in log:
                    yield log
    except FileNotFoundError:
        return "File does not exist"


