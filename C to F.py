celsius = float (input("Temperature value in degree Celsius: " ))  
Fahrenheit = (celsius * 9/5) + 32  
    
# print the result
print(" ")  
print ('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius, Fahrenheit))  
if (Fahrenheit < 33):
   print("")
   print("Its freezing")
elif (Fahrenheit > 122):
    print(" ")
    print("Its very hot")
else: 
    (Fahrenheit > 33 and Fahrenheit < 122 )
    print(" ")
    print("Normal")
   
