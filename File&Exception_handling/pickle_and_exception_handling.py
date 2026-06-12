"""import pickle 

students = {
    "student1": {"roll": 101,"name": "john","percent": 38.5},
    "student2": {"roll": 102,"name": "milan","percent": 58.5},
    "student3": {"roll": 103,"name": "shyamal","percent": 88.5},
    "student4": {"roll": 104,"name": "jaharlal","percent": 78.5},
    "student5": {"roll": 105,"name": "pocha","percent": 48.5}
    }

print(students)
print(type(students))

#Serialization

with open("student.bin",'bw') as f:
    for student in students:
        pickle.dump(student, f)


#Deserialization
with open("students.bin", 'rb') as f:
    data1 = pickle.load(f)
    print(data1, type(data1))
    data2 = pickle.load(f)
    print(data2, type(data2))
    data3 = pickle.load(f)
    print(data3, type(data3))

"""

"""What is pickle ?  --> pickle  use for save the python object in to a file

means:- 
list, dict, class, model, Data
store in to a file 
load the file again

#json take only text
#pickle append all file inside



Why use pickle ? 

Save the ML model
To store the python data
to save Session
To store complex object
"""
"""
#Import pickle
import pickle

#Save the Data(dump) -> Write Binary (wb)
#example: To store list
data = ["Shyamal", 22, 90]

with open("data.pkl", 'wb') as f: # (wb) write binary, create data.pkl file , Binary data store inside.
 
    pickle.dump(data, f) """

#Load the data
import pickle
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)


#Serialization 
with open('data.pkl', 'rb') as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
    