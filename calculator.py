nom1 = int(input('enter your number: '))

nom2 = int(input('enter your second number: '))

op = input ('enter operator (+, *, - or /)')


if op == '+':
    print (nom1 + nom2)
elif op == '*':
    print (nom1 * nom2)
elif op == '-':
    print (nom1 - nom2)
elif op == '/':
    print (nom1 / nom2)
elif op =='%':
    print (nom1 % nom2)
else:
    print ('this operation not allowed ')