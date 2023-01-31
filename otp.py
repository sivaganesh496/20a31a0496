email="ganeshyadav5526@gmail.com"
pwd=123456
otp=3192
cemail=input("enter the email")
cpwd=int(input("enter the pwd"))
cotp=int(input("enter the cotp"))
if(email==cemail and pwd==cpwd):
   print("login successful")
   if(otp==cotp):
         print("order placed successfully")
   else:
         print("order rejected due to incorrect otp")
elif(email!=cemail and pwd==cpwd):
    print("login unsuccesful due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login unsuccessful due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login unsuccessful due to pwd and mail")
else:
   print("login failed")
