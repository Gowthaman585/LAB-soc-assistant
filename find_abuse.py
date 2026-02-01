
# =====================IMPORTS======================
from auth_fail import failed_auth_attempts
import sys
import itertools
# =======================================================================================================
#                                                                                                       #
# A dictinary from the failed_max_auth file.                                                            #
# Which has a key part as tuple : (ip,username) and value : count of the same ip and username detected  #
# Using the result as global for both linear_kiddies and top_kiddies                                    #
result = failed_auth_attempts()                                                                         #
#                                                                                                       #
# =======================================================================================================


# the check_valid_argument check the presence of nessecary arguments in order to run
def check_valid_argument():
    if len(sys.argv)!=3:
        print("The argument must include <limit> <linear|top>")
        sys.exit(1)
    return True
# ==================================================================
def argument_parsing():
    # starting with try block to handle integer converion issues to <limit>
    try:
        # parsing with index value
        # integer converion
        limit = int(sys.argv[1])
        # methodName parsing
        methodName = sys.argv[2]
        # checkpoint to enusure only valid range of limits is entered
        if limit >= len(result):
            print("The limit range is exceeded")
            limit = len(result)
        if limit < 0:
            print("Negative value's are not allowed")
            sys.exit(1)
        # checking only two valid arguments are passed <top> or <linear>
        if methodName not in ['linear' , 'top']:
            print("Only <linear> or <top> argument is allowed")
            sys.exit(1)
        return limit,methodName
    except ValueError:
        print("The limit should be (int)")
# ===================================================================

def return_count(record):
    # returning only the count part
    # boht ip ans username is tuple so it share same index as '0' and the count <value-part> index must be '1'
    return record[1]

def linear_auth_abuse(limit):
    if limit:
        # The itertools.islice() is used to limit how much data to be print in linear manner limit-value
        for item in itertools.islice(result.items(), limit):
            # the key is tuple set on auth_faile script method is : failed_auth_attempts
            (ip,username), counts = item
            print(f"ip : {ip:15}    username : {username:15}    attempts : {counts}")

def top_auth_abuse(limit):
    # sorting the result dict in descending order to to get top 10 or top 20 
    sorted_dict = sorted(result.items(), key=return_count, reverse=True)
    if limit:
        # same itertools to limit how much need to print
        for item in itertools.islice(sorted_dict, limit):
            (ip,username) , counts = item
            print(f"ip : {ip:15}    username : {username:15}    attempts : {counts}")
# ===================================================================

# ============================ RESULTING =============================
def print_result():
    try :
        # calling and gether the argument limit , and which method 
        # the method here helps to detect which method we need to call 
        # wheathe it is linear_auth_abuse or top_auth_abuse by the methodName argument
        limit , methodName = argument_parsing()
        if methodName == 'top':
            top_auth_abuse(limit)
        elif methodName == 'linear':
            linear_auth_abuse(limit)
    except Exception as e:
        print(e)
# =======================================================================
if check_valid_argument():
    print_result()
# =======================================================================
