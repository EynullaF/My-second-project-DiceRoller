import random
import time

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]

while True:
    a1=random.choice(a)
    b1=random.choice(b)
    print(a1 , b1)
    print("\033[31mDo you want to continue?\033[0m")
    n=input("\033[35mPress Enter to continue, otherwise press SPACE and then Enter...\033[0m")
    if n=="":
        print("\033[32mThe program is starting in 5 seconds...\033[0m")
        time.sleep(5)
        print("\033[34mStarted!\033[0m")
    else:
        print("\033[34mProgram stopped!\033[0m")
        break

