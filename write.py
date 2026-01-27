from supply_log import supply_log

def write_sshd_log():
    try:
        with open('sshd.log','w',encoding = 'utf-8') as line:
            for log in supply_log():
                line.write(log + '\n')
    except Exception as e:
        print("Error: ",e)
            
