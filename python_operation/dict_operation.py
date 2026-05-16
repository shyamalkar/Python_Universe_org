dict_op = {"'a':1, 'b':2: 6"}
print(dict_op)
#Not allowed - list, set, dict => mutable datatypes 

#allowed keys - str, int, float, bool, tuple => immutable datatypes

#Keys of a dictionary can only be mutable datatypes!
student_1 = {"id":1001, "name":"john", "marks":[19.09, 90.10, 20.23, 79.98]}
print(student_1['marks'][1])

print(student_1.keys()) # Key usage for how many value in this variable ?

print(student_1.keys(), type(student_1.keys()))

#values()
print(student_1.values(), type(student_1.values()))

#Items
print(student_1.items(), type(student_1.items()))
