plndrm = input('Enter your potential pallindrome: ')
if str(plndrm.lower()) == str(plndrm.lower())[::-1]:
  print('True')
else:
  print('False')

