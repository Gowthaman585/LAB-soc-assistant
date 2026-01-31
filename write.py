from read import read_sshd
from read import read_sudo
# Method to write sshd-logs separately in a file 'sshd.log'
def write_sshd_log():
    try:
        with open('sshd.log','w',encoding = 'utf-8') as line:
            for log in read_sshd():
                line.write(log)
    except Exception as e:
        print("Error: ",e)

# Method to write sudo logs in separate file 'sudo.log'
def write_sudo_log():
    try:
        with open('sudo.log' , 'w',encoding='utf-8') as line:
            for log in read_sudo():
                line.write(log)
    except Exception as e:
        print(e)

# Calling both the function to complete the job
write_sshd_log()
write_sudo_log()
