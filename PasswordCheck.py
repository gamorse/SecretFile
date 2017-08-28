passwordFile = open('SecretPassword.txt')
password = (passwordFile.read()).strip()

access = False
print password
enteredPassword = raw_input('Enter password: ')
print enteredPassword
if enteredPassword == password:
	access = True
	print 'Access granted.'
else:
	print 'DENIED'
