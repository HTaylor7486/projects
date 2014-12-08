#equation solver
import time

print ("lets do a calculation")
time.sleep(0.5)
t = input("what type of sum woul;d you like to do?")
num = int(input("please enter a number --- "))
num2 = int(input("Please enter another number --- "))
if t == ("+"):
    print ((num)+(num2))
elif t == ("-"):
    print ((num)-(num2))
elif t == ("*"):
    print ((num)*(num2))
elif t == ("/"):
    print ((num)/(num2))
else:
    print ("what?")
