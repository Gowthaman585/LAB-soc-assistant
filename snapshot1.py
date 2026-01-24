import re

# Opening the file in read mode to analyze
with open("sample.log",'r') as file:
	lines = file.readlines()

# var for counting successful ssh-login attemnpts
successful_logins = 0

# var for failed ssh-login attempts
failed_logins = 0

# var for counting active sessions
active_sessions = 0

# var for particulary counting the events
accepted_pubkey = 0
accepted_password = 0
failed_password = 0
failed_pubkey = 0
connection_drop = 0
session_open = 0
session_close = 0

# snippet to count the ssh-log lines particularly
for i in lines:
	if re.search("sshd",i):
		if re.search("Accepted publickey",i):
			accepted_pubkey = accepted_pubkey + 1
		if re.search("Accepted password",i):
			accepted_password = accepted_password + 1
		if re.search("Failed password",i):
			failed_password = failed_password + 1
		if re.search("Failed publickey",i):
			failed_pubkey = failed_pubkey + 1
		if re.search("Connection closed by authenticating user",i):
			connection_drop = connection_drop + 1
		if re.search("session opened",i):
			session_open = session_open + 1
		if re.search("session closed ",i):
			session_close = session_close + 1

# statement for total successful logins
successful_logins = accepted_pubkey + accepted_password

# statement for total no of failed ssh-login attemps
failed_logins = failed_password + connection_drop + failed_pubkey

# statement for calculating active sessions
active_sessions = session_open - session_close

# displaying  the detials for ssh-login event details
print(f"This mini ssh-log analysis tool is most suitable  on auth.log or sshd daemon logs")
print(f"Any other kind of logs may be result in inaccuracy")
print(f"===================== LOG ANALYSIS COMPLETED =====================")
print(f"Total no of ssh-login attempts 		: {successful_logins + failed_logins}")
print("-------------------------------------------------------------------")
print(f"Total no of successful ssh-logins	: {successful_logins}")
print(f"	└─ password based logins 	: {accepted_password}")
print(f"	└─ key based logins 		: {accepted_pubkey}")
print(f"Total no of failed ssh-login attempts 	: {failed_logins}")
print(f"	└─ password failed attempts 	: {failed_password}")
print(f"	└─ key failed attempts 		: {failed_pubkey}")
print(f"	└─ connection drop out 		: {connection_drop}")
print("-------------------------------------------------------------------")
print(f"Total no of ssh-logouts : {session_close}")
print(f"Total no of active ssh-sessions : {active_sessions}")
