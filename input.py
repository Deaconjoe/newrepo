#user_input = input("Enter your name : ")
# message = "Hello %s!" % user_input for python2 and python3 belo only python3
#this called place holder 
#message = f"Hello {user_input}"
#print (message)

#an other example !!
name = input("Enter your name : ")
surname = input("Enter your surname : ")
when = "today"

#message ="Hello %s %s" % (name ,surname )
message = f"Hello {name} {surname}. What's up {when}"
print(message)