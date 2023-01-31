days=int(input("Enter no.of Days"))
if(days>84):
    print("Plan has Expired")
else:
    calls=int(input("Enter no.of Calls: "))
    msg=int(input("Enter no.of msg: "))
    data=float(input("Enter the data Used: "))
    
    Remainingdays=84-days
    print("Remainingdays",Remainingdays)
    if(calls>3000):
        print("Calls limit exceeded")
    else:
        Remainingcalls=3000-calls
        print("Remainingcalls",Remainingcalls)
        
    
    if(msg>100):
        print("Msg limit is exceeded")
    else:
        Remainingmsg=100-msg
        print("Remainingmsg",Remainingmsg)
    
    if(data>2.0):
        print("Speed reduces due to completion of data")
    else:
        Remainingdata=2.0-data
        print("Remainingdata",Remainingdata)
