# Python Program to check if a string is a pallindrome
plndrm = input('Enter your potential pallindrome: ')#User Input, defines variable
if str(plndrm.lower()) == str(plndrm.lower())[::-1]: #Changes string to lowercase and compares it to its inverse
  print('True')
else:
  print('False')# Prints outcome

