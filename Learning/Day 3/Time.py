import time

from datetime import datetime

c = datetime.now().time()

# current_time = c.strftime("%H:%M:%S")
current_time = c.strftime("%H")
timestamp = time.strftime("%H")

print(timestamp)

if (int(timestamp) >= 2):
    print("Good Morning")
  
elif(int(timestamp)  <= 2 or int(timestamp)  >= 8):
   print("Good Afternoon")

else:
    print("Good night")
  


