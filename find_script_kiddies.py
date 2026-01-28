from failed_max_auth import failed_max_auth_attempts


# A dictinary from the failed_max_auth file.
# Which has a key part as tuple : (ip,username) and value : count of the same ip and username detected
# Using the result as global for both linear_kiddies and top_kiddies
result = failed_max_auth_attempts()

def return_count(record):
    # returning only the count part
    # boht ip ans username is tuple so it share same index as '0'
    return record[1]

def linear_auth_abuse():
    for (ip,username) , counts  in result.items():
        yield(ip,username), counts

def top_auth_abuse():
    sorted_dict = dict(sorted(result.items(), key=return_count, reverse=True))
    for (ip,username) , counts in sorted_dict.items():
        yield (ip,username) , counts

