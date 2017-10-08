n=int(input('Minutes:'))
n%=24*60
hours=str(n//60)
if len(hours)==1:
    hours='0'+hours
minutes=str(n%60)
if len(minutes)==1:
    minutes='0'+minutes
print(hours+':'+minutes)
input()
