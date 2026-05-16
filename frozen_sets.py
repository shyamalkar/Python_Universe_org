fs1 = frozenset({10, 20, 30}) # Frozen set are not working because , frozing set are not changeable .
print(fs1, type(fs1))

fs1.add(40)  

print(fs1) #This is not working because frozen data are not working.
  
