#Import library
import random

#Will continue to loop

x = "r"

while x == "r":
     
    dice = random.randint(1,6)
 
#Returns a print of an actual dice number
    if dice == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if dice == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    if dice == 3:
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")
    if dice == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if dice == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if dice == 6:
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")

 #Press r key to roll again
    x=input("press r again and n to exit:")
    print("\n")
