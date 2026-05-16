"""import os 
try:
    f = open("example_.txt", 'rt') 

    data = f.read()
    f.close()

    print(data)

except FileNotFoundError as file_error:

    print("File that you are trying to open does not exist! ")
    print(file_error)


#If there is a no code block in this coding then use else

#else:
else:

    print("else block")
    print(data)


finally:
    print("Finally block")


#Try + except (Recap)
try:
    x = int(input("Enter number: "))
    print(10 / x)

except:
    print("Error occurred")"""
#If error happen except will continue runing 
#else = If no error , else run this time , when no error happen in try bock .
#example:-
try:
    x = int(input("Enter a number:"))
    y = 10 / x
except:
    print("Wrong input")
else:
    print("Result:", y)

# finally = Always run 
#finally block run always -> it's does't matter error happen or not happen , whether the programm exit or not

try:
    x = int(input("Enter number: "))
    print(10 / x)

except:
    print("Error")

finally:
    print("Thank You!")



#Always remember 
"""try     = Try continue
except  = If problem happen
else    = If problem not happen  
finally = Whether error happen or not it's does't matter it add always.
"""