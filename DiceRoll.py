import random
 
 
x = "y"
  
while x == "y":
     
    dice = random.randint(1,6)
     
    if dice == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if dice == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    if dice == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    if dice == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if dice == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if dice == 6:
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
         
    x=input("press r to roll again and n to exit:")
    print("\n")
    
