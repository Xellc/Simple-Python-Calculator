


"""
My first ever Python Script. Yay?
Made by Xell/Vosik
made with Love
"""
import time
import sys
import sl4a
from android import Android
droid = sl4a.Android()
Functions = ['Divide', 'Multi', 'Plus', 'Minus', 'Circumference']
from math import pi
Loop=("Y")
while Loop == "Y":
 A1=droid.dialogGetInput("Divide, Multi, Plus, Minus or Circumfence").result
 N1=float(droid.dialogGetInput("Enter First Number").result)
 if A1 == "Circumference":
  N2=float(pi)
 else:
  N2=float(droid.dialogGetInput("Second Number: ").result)
 
 if A1 == "Circumference":
  Result = str(N1 * N2)
  droid.dialogCreateAlert("Result", Result)
  droid.dialogSetPositiveButtonText('Continue')
  droid.dialogSetNegativeButtonText('Exit')
  droid.dialogShow()

 if A1 == "Divide":
  Result = str(N1 / N2)
  droid.dialogCreateAlert("Result", Result)
  droid.dialogSetPositiveButtonText('Continue')
  droid.dialogSetNegativeButtonText('Exit')
  droid.dialogShow()

 if A1 == "Multi":
  Result = str(N1 * N2)
  droid.dialogCreateAlert("Result", Result)
  droid.dialogSetPositiveButtonText('Continue')
  droid.dialogSetNegativeButtonText('Exit')
  droid.dialogShow()
 
 if A1 == "Plus":
  Result = str(N1 + N2)
  droid.dialogCreateAlert("Result", Result)
  droid.dialogSetPositiveButtonText('Continue')
  droid.dialogSetNegativeButtonText('Exit')
  droid.dialogShow()

 if A1 == "Minus":
  Result = str(N1 - N2)
  droid.dialogCreateAlert("Result", Result)
  droid.dialogSetPositiveButtonText('Continue')
  droid.dialogSetNegativeButtonText('Exit')
  droid.dialogShow()
  
 if A1 not in Functions:
  droid.dialogCreateAlert("ERROR", "NO VALID FUNCTION!")
  droid.dialogSetPositiveButtonText('Continue')
  droid.dialogSetNegativeButtonText('Exit')
  droid.dialogShow()

 response = droid.dialogGetResponse().result
 droid.dialogDismiss()
 
 if not 'which' in response or response['which'] != 'positive': sys.exit()