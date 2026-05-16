dict_op = {"'a':1, 'b':2: 6"}
print(dict_op)
#Not allowed - list, set, dict => mutable datatypes 

#allowed keys - str, int, float, bool, tuple => immutable data types

#Keys of a dictionary can only be mutable datatypes!
student_1 = {"id":1001, "name":"john", "marks":[19.09, 90.10, 20.23, 79.98]} 
print("Student", student_1['marks'][0])  
  
print("Student keys:", student_1.keys()) # Key usage for how many value in this variable ?
  
print("student keys and type", student_1.keys(), type(student_1.keys()))

#values()
print("Dict values", student_1.values(), type(student_1.values()))

#Items
print("Dict_items", student_1.items(), type(student_1.items()))
