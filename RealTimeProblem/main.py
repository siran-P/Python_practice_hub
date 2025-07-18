'''RS->real time speed(int)0-140
>100 overspeed

CLI->climate(string)normal,water
if water >70 "ABS act"

sb->seat belt=On Off 30 seconds

temperature->20-60(Temp ok)
            60-70(Temp HIGH)
            >70(Over heat)'''
import time
while 1:
    rs=int(input("Speed:"))
    cli=input("Climate:")
    sb=input("Status of seat belt:")
    temp=int(input("Temperature:"))
    if(cli.lower() == 'water' and rs>70):
        print("ABS activate")
    elif(rs>100):
        print("Overspeed")
    if temp>20 and temp<=60:
        print("Temp ok")
    elif temp>=60:
        print("Temp High")
    elif temp>=70:
        print("Over heat")
    if sb.lower()!='on':
        for i in range(30):
            print('put your seat belt')
            time.sleep(1)
    
    
        
        
        