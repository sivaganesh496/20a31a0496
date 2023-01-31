email="ganeshyadav5526@gmail.com"
pwd=123456
cemail=input("enter the email")
cpwd=int(input("enter the pwd"))
if(email==cemail and pwd==cpwd):
   print("login successful")
elif(email!=cemail and pwd==cpwd):
   print("loogin failed due to mail")
elif(email==cemail and pwd!=cpwd):
   print("loogin failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
   print("login failed due to email and pwd")
else:
   print("login failed")

