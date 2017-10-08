a=[int(input('First group:')),int(input('Second group:')),int(input('Third group:'))]
s=0
for i in a:
    s+=i//2+i%2
print('Tables:'+str(s))
input()
