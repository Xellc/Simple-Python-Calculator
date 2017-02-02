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
 Functions = "[Divide, Multi, Plus, Minus, Circumference]"
 print(Functions)
 A1=input("You can Choose between the Functions above_")
 N1=float(input("Enter first Number"))
 if A1 == "Circumference":
  print("Second Number will be set to 3.14 after all")
 N2=float(input("Enter second Number"))


 if A1 not in Functions:
  print("ERROR! NO VALID FUNCTION")
 elif A1 in Functions:
  print("vvv|Done|vvv")
 
 if A1 == "Circumference":
  N2=float("3.14")
  print(N1 * N2)



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