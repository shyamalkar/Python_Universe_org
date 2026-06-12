"""
What is json ? 

json full form is javaScript object Notation,it's widely accepted for text based format for data exchange.
json is an data interchange format that is language-independent and can be read, generated, and parsed by virtually every major programming language.  language where every programming language can understant.

"""

#Let's take an another example here
import json

students = {'student1': {'roll':101, 'name':'john', 'percent':38.5},
            'student2': {'roll':102, 'name':'milan', 'percent':58.5},
            'student3': {'roll':103, 'name':'shyamal', 'percent':88.5},
            'student4': {'roll':104, 'name':'jaharlal', 'percent':78.5},
            'student5': {'roll':105, 'name':'pocha', 'percent':48.5}}


print(students)
print(type(students)) 


"""
#dump()
with open("student_data_file.json",'x') as fh:
    json.dump(students, fh, indent=4)
"""
#Always remeber if you create a any file using with or any function then make sure you can't open this file where you create, because you create file already exist , so this message showing a error
#create file coding run gain so showing this error . so the right path is you can comment then and run this file 

#Let's open this file 

with open("student_data_file.json", 'r') as f:
    data = json.load(f)

print(data)
print(type(data))

#Let's Update this file 

with open("student_data_file.json",'r') as f:
    data = json.load(f)

#Update operation
data.update(students)

#dump - write the updated data in the json file
with open('student_data.json', 'w') as f:
    json.dump(data, f, indent=4) # Indent for space , you can add any number but 4 is recommed because you can read with good looking format.


try:
    #read the old data from the json file
    with open('student_data_file.json', 'r') as f:
        data = json.load(f)
    
except FileExistsError:
    with open ('student_data_file.json', 'w') as f:
        json.dump(students, f, indent=4)

else:
    #Update operation
    data.update(students)
    #dump - write the updated data in the json file
    with open('student_data_file.json', 'w') as f:
        json.dump(data, f, indent=4)