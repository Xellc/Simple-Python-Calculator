#-*-coding:utf8;-*-
#qpy:3
#qpy:console


"""
My first ever Python Script. Yay?
Made by Xell/Vosik
made with Love
"""
Loop=input("Start Calculator? Y/N")
while Loop == "Y":
 Functions = "[Divide, Multi, Plus, Minus]"
 print(Functions)
 A1=input("You can Choose between the Functions above_")
 N1=float(input("Enter first Number"))
 N2=float(input("Enter second Number"))


 if A1 not in Functions:
  print("ERROR! NO VALID FUNCTION")
 elif A1 in Functions:
  print("vvv|Done|vvv")
 
 



 if A1 == "Divide":
  print(N1 / N2)

 if A1 == "Multi":
  print(N1 * N2)
 
 if A1 == "Plus":
  print(N1 + N2)

 if A1 == "Minus":
  print(N1 - N2)
  
 if A1 in Functions:
  print("^^^|Done|^^^")
  
 print("=======End of Calculation=======")
 
 print("Start new Calculation?")
 Loop=input("Y/N")