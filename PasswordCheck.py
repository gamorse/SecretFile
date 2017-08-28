passwordFile = open('SecretPassword.txt', 'r')
password = passwordFile.read()

access = False

enteredPassword = raw_input('Enter password: ')

if enteredPassword == password:
	access = True
	print 'Access granted.'
else:
	print 'DENIED'
