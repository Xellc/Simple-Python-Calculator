


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
 N1=float(input("First Number : "))
 if A1 == "Circumference":
  print("Second Number will be set forcefully to 3.14")
 N2=float(input("Second Number: "))

 if N1 == "0":
  end

 if N2 == "0":
  end
  
 if A1 not in Functions:
  print("ERROR! NO VALID FUNCTION")
 elif A1 in Functions:
  print("v-v-v|Done|v-v-v")
 
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
  print("^-^-^|Done|^-^-^")
  
 print("=======End of Calculation=======")
 
 print("Start new Calculation?")
 Loop=input("Y/N")