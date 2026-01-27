def failed_max_auth_attempts():
    try:
        
        ip_username_count = {}

        with open('sshd.log','r',buffering=8128,encoding='utf-8') as file:
            for log in file:
                if 'error: ' in log and 'for ' in log and 'from ' in log:
                    start_index = log.find('for ')+4
                    end_index = log.find(' ',start_index)
                    # username
                    username = log[start_index:end_index]
                    start_index = log.find('from ')+5
                    end_index = log.find(' ',start_index)
                    #ip address
                    ipaddr = log[start_index:end_index]
                    # tuple declaration to pair ip and username together
                    key = (ipaddr,username)
                    # storing the ip and username couple into a dictinary to get each number of attempts
                    # ==================================================================
                    # SYNTAX : dict_name.get('key_name',default_value)+ increment_value
                    # ==================================================================
                    # the default value is used for the first time when no matching key or new key if found
                    ip_username_count[key] = ip_username_count.get(key,0)+1

        return ip_username_count


    except Exception as e:
        print(e)

