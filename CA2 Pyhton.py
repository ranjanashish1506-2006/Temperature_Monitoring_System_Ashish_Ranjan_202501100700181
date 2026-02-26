import random
import time
max=int(input("Enter Maximum Temperature in Celcius : "))
min=int(input("Enter Minimum Temperature in Celcius : "))
timt=int(input("Enter Runtime : "))
mean=0
for i in range(timt//2):
  a=random.randint(min,max);
  print("READING",i," : The Temperature is :",float(a),"C")
  mean=mean+a
  time.sleep(2)
print("Experimental value obtained :",mean/5,"C");
