from read import read

def write_sshd_log():
    try:
        with open('sshd.log','w',encoding = 'utf-8') as line:
            for log in read():
                line.write(log)
    except Exception as e:
        print("Error: ",e)
            
