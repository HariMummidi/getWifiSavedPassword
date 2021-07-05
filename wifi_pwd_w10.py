"""
Name: getWifiPasswordsWin10.py
Author: Hari Mummidi
Email: harivenkatmummidi@gmail.com
Date: 05/July/2021

Updates:


"""

# importing check_output module from sub process
from subprocess import check_output, CalledProcessError

# getting data , decoding and spliting to get the profile names
data = check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')


# creating a list of profiles
profiles = []

# capturing the profile names.
for i in data:
	
	# find "All User Profile" in each item
	if "All User Profile" in i :
		
		# if found
		# split the item
		i = i.split(":")
		
		# item at index 1 will be the wifi name
		i = i[1]
		
		# formatting the name
		# first and last character is not required
		i = i[1:-1]
		
		# appending the wifi name in the list
		profiles.append(i)
		

# printing heading	
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

# traversing the profiles	
for i in profiles:
	
	# try catch block begins
	# try block
	try:
		# getting data with password using wifi name, decoding and splitting data line by line
		results = check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
		
		# finding password from the result list
		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		
		# if there is password it will print the pass word
		try:
			print("{:<30}| {:<}".format(i, results[0]))
		
		# else it will print blank in fornt of pass word
		except IndexError:
			print("{:<30}| {:<}".format(i, ""))
			
			
	# called when this process get failed
	except CalledProcessError:
		print("Encoding Error Occured")
