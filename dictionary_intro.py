#Comma separated key-value pairs enclosed within {}

#{key1:value1, key2:value2, ......}

groceries = {
    "milk: 10": 60, 
    "Biscuits": 10, 
    "Rice": 100,
    "Bread": 30 
}  

print(groceries["milk: 10"])
  
groceries = {"milk":60, # Dictionary never work with strate line .
             "Biscuits":10,
             "Rice":100,
             "Bread":30}
groceries["eggs:"] = 10, # Dictionary are mutable so change are accepted, i hope you understand . 

#If you want to access with key, then use 
print(list(groceries.keys())[1])

#If you want to access with values, then use value()
print(list(groceries.values())[1]) 
